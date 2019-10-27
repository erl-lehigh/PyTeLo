'''
 Copyright (C) 2019 Noushin Mehdipour <noushinm@bu.edu> and 
 2015-2019 Cristian Ioan Vasile <cvasile@bu.edu,cvasile@lehigh.edu> , 
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 See license.txt file for license information.
'''

import itertools as it

import numpy as np
from scipy.interpolate import interp1d
from antlr4 import InputStream, CommonTokenStream

from stlLexer import stlLexer
from stlParser import stlParser
from stlVisitor import stlVisitor


class Operation(object):
    '''STL operations'''
    NOP, NOT, OR, AND, EVENT, ALWAYS, PRED, BOOL = range(8)
    opnames = [None, '!', '||', '&&', '=>', 'U', 'F', 'G', 'predicate', 'bool']
    opcodes = {'!': NOT, '&&': AND, '||' : OR,  'F': EVENT, 'G': ALWAYS}
    # negation closure of operations
    negop = (NOP, NOP, AND, OR, ALWAYS, EVENT, PRED, BOOL)

    @classmethod
    def getCode(cls, text):
        ''' Gets the code corresponding to the string representation.'''
        return cls.opcodes.get(text, cls.NOP)

    @classmethod
    def getString(cls, op):
        '''Gets custom string representation for each operation.'''
        return cls.opnames[op]


class RelOperation(object):
    '''Predicate relationship operations'''
    NOP, LT, LE, GT, GE, EQ, NQ = range(7)
    opnames = [None, '<', '<=', '>', '>=', '=', '!=']
    opcodes = {'<': LT, '<=': LE, '>' : GT, '>=': GE, '=': EQ, '!=': NQ}
    # negation closure of operations
    negop = (NOP, GE, GT, LE, LT, NQ, EQ)

    @classmethod
    def getCode(cls, text):
        ''' Gets the code corresponding to the string representation.'''
        return cls.opcodes.get(text, cls.NOP)

    @classmethod
    def getString(cls, rop):
        '''Gets custom string representation for each operation.'''
        return cls.opnames[rop]


class STLFormula(object):
    '''Abstract Syntax Tree representation of an STL formula'''

    def __init__(self, operation, **kwargs):
        '''Constructor'''
        self.op = operation

        if self.op == Operation.BOOL:
            self.value = kwargs['value']
        elif self.op == Operation.PRED:
            self.relation = kwargs['relation']
            self.variable = kwargs['variable']
            self.threshold = kwargs['threshold']
        elif self.op in (Operation.AND, Operation.OR):
            self.children = kwargs['children']
        elif self.op == Operation.NOT:
            self.child = kwargs['child']
        elif self.op in(Operation.ALWAYS, Operation.EVENT):
            self.low = kwargs['low']
            self.high = kwargs['high']
            self.child = kwargs['child']

        self.__string = None
        self.__hash = None

    def robustness(self, s, t, maximumRobustness=1):
        '''Computes the robustness of the STL formula.'''
        if self.op == Operation.BOOL:
            if self.value:
                return maximumRobustness
            else:
                return -maximumRobustness
        elif self.op == Operation.PRED:
            value = s.value(self.variable, t)
            Range=s.varrange(self.variable)
            if self.relation in (RelOperation.GE, RelOperation.GT):
                return  1.0/Range*(value - self.threshold)
            elif self.relation in (RelOperation.LE, RelOperation.LT):
                return 1.0/Range*(self.threshold - value)
            elif self.relation == RelOperation.EQ:
                return 1.0/Range*(-abs(value - self.threshold))
            elif self.relation == RelOperation.NQ:
                return 1.0/Range*(abs(value - self.threshold))
        elif self.op == Operation.AND:
            return 1.0/len(self.children)*np.sum([child.robustness(s, t) for child in self.children if child.robustness(s, t) <= 0]) if any(child.robustness(s, t) <= 0 for child in self.children) else np.prod([child.robustness(s, t)+1 for child in self.children])**(1.0/len(self.children))-1
            
        elif self.op == Operation.OR:
            return 1.0/len(self.children)*np.sum([child.robustness(s, t) for child in self.children if child.robustness(s, t) > 0]) if any(child.robustness(s, t) > 0 for child in self.children) else -(np.prod([1-child.robustness(s, t) for child in self.children])**(1.0/len(self.children)))+1
                  
        elif self.op == Operation.NOT:
            return -self.child.robustness(s, t)
 
        elif self.op == Operation.ALWAYS:
            return 1.0/(self.high+1-self.low)*np.sum([self.child.robustness(s, t+tau)
                                for tau in np.arange(self.low, self.high+1) if self.child.robustness(s, t+tau) <= 0]) if any(self.child.robustness(s, t+tau) <= 0 for tau in np.arange(self.low, self.high+1)) else np.prod([self.child.robustness(s, t+tau)+1
                                for tau in np.arange(self.low, self.high+1)])**(1.0/(self.high+1-self.low))-1
            
        elif self.op == Operation.EVENT:
            return 1.0/(self.high+1-self.low)*np.sum([self.child.robustness(s, t+tau)
                                for tau in np.arange(self.low, self.high+1) if self.child.robustness(s, t+tau) > 0]) if any(self.child.robustness(s, t+tau) > 0 for tau in np.arange(self.low, self.high+1)) else -(np.prod([1-self.child.robustness(s, t+tau)
                                for tau in np.arange(self.low, self.high+1)])**(1.0/(self.high+1-self.low)))+1


    def negate(self):
        '''Computes the negation of the STL formula by propagating the negation
        towards predicates.
        '''
        if self.op == Operation.PRED:
            self.relation = RelOperation.negop[self.relation]
        elif self.op in (Operation.AND, Operation.OR):
            self.left = self.left.negate()
            self.right = self.right.negate()
        elif self.op == Operation.NOT:
            return self.child
        elif self.op in (Operation.ALWAYS, Operation.EVENT):
            self.child = self.child.negate()
        self.op = Operation.negop[self.op]
        return self

    def pnf(self):
        '''Computes the Positive Normal Form of the STL formula, potentially
        adding new variables.

        Note: The tree structure is modified in-place.
        '''
        if self.op == Operation.PRED:
            if self.relation in (RelOperation.LE, RelOperation.LT):
                self.variable = '{variable}_neg'.format(variable=self.variable)
            elif self.relation == RelOperation.EQ:
                children = [STLFormula(Operation.PRED, relation=RelOperation.GE,
                              variable=self.variable, threshold=self.threshold),
                            STLFormula(Operation.PRED, relation=RelOperation.GE,
                              variable='{variable}_neg'.format(self.variable),
                              threshold=-self.threshold)]
                return STLFormula(Operation.AND, children=children)
            elif self.relation == RelOperation.NQ:
                children = [STLFormula(Operation.PRED, relation=RelOperation.GT,
                              variable=self.variable, threshold=self.threshold),
                            STLFormula(Operation.PRED, relation=RelOperation.GT,
                              variable='{variable}_neg'.format(self.variable),
                              threshold=-self.threshold)]
                return STLFormula(Operation.OR, children=children)
        elif self.op in (Operation.AND, Operation.OR):
            self.children = [child.pnf() for child in self.children]
        elif self.op == Operation.NOT:
            return self.child.negate().pnf()
        elif self.op in (Operation.ALWAYS, Operation.EVENT):
            self.child = self.child.pnf()
        return self

    def bound(self):
        '''Computes the bound of the STL formula.'''
        if self.op == Operation.PRED:
            return 0
        elif self.op in (Operation.AND, Operation.OR):
            return max([ch.bound() for ch in self.children])
        elif self.op == Operation.NOT:
            return self.child.bound()
        elif self.op in (Operation.ALWAYS, Operation.EVENT):
            return self.high + self.child.bound()

    def variables(self):
        '''Computes the set of variables involved in the STL formula.'''
        if self.op == Operation.PRED:
            return {self.variable}
        elif self.op in (Operation.AND, Operation.OR):
            return set.union(*[child.variables() for child in self.children])
        elif self.op in (Operation.NOT, Operation.ALWAYS, Operation.EVENT):
            return self.child.variables()

    def identifier(self):
        h = hash(self)
        if h < 0:
            h = hex(ord('-'))[2:] + hex(-h)[1:]
        else:
            h = hex(ord('+'))[2:] + hex(h)[1:]
        return h

    def __hash__(self):
        if self.__hash is None:
            self.__hash = hash(str(self))
        return self.__hash

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        if self.__string is not None:
            return self.__string

        opname = Operation.getString(self.op)
        if self.op == Operation.PRED:
            s = '({v} {rel} {th})'.format(v=self.variable, th=self.threshold,
                                    rel=RelOperation.getString(self.relation))
        elif self.op in (Operation.AND, Operation.OR):
            children = [str(child) for child in self.children]
            s = '(' + ' {op} '.format(op=opname).join(children) + ')'
        elif self.op == Operation.NOT:
            s = '{op} {child}'.format(op=opname, child=self.child)
        elif self.op in (Operation.ALWAYS, Operation.EVENT):
            s = '({op}[{low}, {high}] {child})'.format(op=opname,
                                 low=self.low, high=self.high, child=self.child)
        self.__string = s
        return self.__string


class STLAbstractSyntaxTreeExtractor(stlVisitor):
    '''Parse Tree visitor that constructs the AST of an STL formula'''

    def visitFormula(self, ctx):
        op = Operation.getCode(ctx.op.text)
        ret = None
        low = -1
        high = -1
        if op in (Operation.AND, Operation.OR):
            left = self.visit(ctx.left)
            right = self.visit(ctx.right)
            assert op != right.op
            if left.op == op:
                children = left.children
            else:
                children = [left]
            children.append(right)
            ret = STLFormula(op, children=children)
        elif op == Operation.NOT:
            ret = STLFormula(op, child=self.visit(ctx.child))
        elif op in (Operation.ALWAYS, Operation.EVENT):
            low = float(ctx.low.text)
            high = float(ctx.high.text)
            ret = STLFormula(op, child=self.visit(ctx.child),
                             low=low, high=high)
        else:
            print('Error: unknown operation!')
        return ret

    def visitBooleanPred(self, ctx):
        return self.visit(ctx.booleanExpr())

    def visitBooleanExpr(self, ctx):
        return STLFormula(Operation.PRED,
            relation=RelOperation.getCode(ctx.op.text),
            variable=ctx.left.getText(), threshold=float(ctx.right.getText()))

    def visitParprop(self, ctx):
        return self.visit(ctx.child);


class Trace(object):
    '''Representation of a system trace.'''

    def __init__(self, variables, timePoints, data, varranges, kind='nearest'):
        '''Constructor'''
        # self.timePoints = list(timePoints)
        # self.data = np.array(data)
        for variable, var_data in zip(variables, data):
            print(variable, var_data, timePoints)
        self.data = {variable : interp1d(timePoints, var_data, kind=kind)
                            for variable, var_data in zip(variables, data)}
        self.range={variable : varranges[variable]
                            for variable in variables}

    def value(self, variable, t):
        '''Returns value of the given signal component at time t.'''
        return self.data[variable](t)

    def values(self, variable, timepoints):
        '''Returns value of the given signal component at desired timepoint.'''
        return self.data[variable](np.asarray(timepoints))

    def varrange(self, variable):
        '''Return the range for each parameter'''
        return self.range[variable]
    
    def __str__(self):
        raise NotImplementedError

if __name__ == '__main__':
    lexer = stlLexer(InputStream("!(x < 10) && F[0, 2] y > 2 || G[1, 3] z<=8 && G[4, 6] z>8 "))
    #lexer = stlLexer(InputStream("G[4, 6] z>8"))
    tokens = CommonTokenStream(lexer)

    parser = stlParser(tokens)
    t = parser.stlProperty()
    print(t.toStringTree())

    ast = STLAbstractSyntaxTreeExtractor().visit(t)
    #print('AST:', ast)

    varnames = ['x', 'y', 'z']
    #data = [[11, 11, 11, 11, 11], [2, 3, 1, 2, 2], [3, 8, 7, 9, 9]]
    data = [[8, 8, 11, 11, 11,1,1], [1, 3, 2, 2,2,0,0], [3, 9, 8, 9, 9,9,9]]
    timepoints = [0, 1, 2, 3, 4,5,6]
    varranges={'x':20,'y':10,'z':10}
    s = Trace(varnames, timepoints, data, varranges)

    print('r:', ast.robustness(s, 0))

    pnf = ast.pnf()
    print(pnf)

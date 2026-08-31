'''
 Copyright (c) 2015-2020
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab (ERL), Lehigh University
 @author: Cristian Ioan Vasile <cvasile@lehigh.edu>
 
 Copyright (c) 2026, Explainable Robotics Lab (ERL), Lehigh University
 @contributor: Crockett L. Hensley
 See license.txt file for license information.
'''

import itertools as it
import warnings

import numpy as np

from antlr4 import InputStream, CommonTokenStream

from pytelo._internal.stlLexer import stlLexer
from pytelo._internal.stlParser import stlParser
from pytelo._internal.stlVisitor import stlVisitor

class Operation(object):
    '''Representation of all possible operations in an STL formula.
    
    This class provides necessary mapping interfaces for use of enumeration 
    codes as a representation of the operations defined in stl.g4 grammar.
    
    Class Attributes
    ----------
    NOP (int): 0
    NOT (int): 1
    OR (int): 2
    AND (int): 3
    IMPLIES (int): 4
    UNTIL (int): 5
    EVENT (int): 6
    ALWAYS (int): 7
    PRED (int): 8
    BOOL (int): 9
    opnames (list): mapping from opcodes to default MILP variable prefixes
    opcodes (dict): inverse mapping of opnames
    opstrnames (list): mapping from opcodes to user-friendly string names
    negop (tuple): mapping from opcodes to opcodes of negatory operations (where defined)
    '''
    NOP, NOT, OR, AND, IMPLIES, UNTIL, EVENT, ALWAYS, PRED, BOOL = range(10)
    opnames = [None, '!', '||', '&&', '=>', 'U', 'F', 'G', 'predicate', 'bool']
    opcodes = {'!': NOT, '&&': AND, '||' : OR, '=>': IMPLIES,
               'U': UNTIL, 'F': EVENT, 'G': ALWAYS}
    opstrnames = [None, 'not', 'or', 'and', 'imply', 'until', 'event', 'always',
                  'predicate', 'bool']
    # negation closure of operations
    negop = (NOP, NOP, AND, OR, AND, NOP, ALWAYS, EVENT, PRED, BOOL)

    @classmethod
    def getCode(cls, text):
        ''' Gets the code corresponding to the string representation.'''
        return cls.opcodes.get(text, cls.NOP)

    @classmethod
    def getString(cls, op):
        '''Gets custom string representation for each operation.'''
        return cls.opnames[op]

    @classmethod
    def getName(cls, op):
        '''Gets custom long string name for each operation.'''
        return cls.opstrnames[op]


class RelOperation(object):
    '''Representation of all possible predicate relationships in an STL formula.
    
    This class provides necessary mapping interfaces for use of enumeration 
    codes as a representation of the boolean expressions defined in stl.g4 grammar.
    
    Class Attributes
    ----------
    NOP (int): 0
    LT (int): 1
    LE (int): 2
    GT (int): 3
    GE (int): 4
    EQ (int): 5
    NQ (int): 6
    opnames (list): mapping from opcodes to string values for formula inline representation
    opcodes (dict): inverse mapping of opnames
    negop (tuple): mapping from opcodes to opcodes of complementary operations (where defined, e.g. LT <-> GE)
    invop (tuple): mapping from opcodes to opcodes of inverse operations (where defined, e.g. LT <-> GT)
    '''
    NOP, LT, LE, GT, GE, EQ, NQ = range(7)
    opnames = [None, '<', '<=', '>', '>=', '=', '!=']
    opcodes = {'<': LT, '<=': LE, '>' : GT, '>=': GE, '=': EQ, '!=': NQ}
    # negation closure of operations
    negop = (NOP, GE, GT, LE, LT, NQ, EQ)
    invop = (NOP, GT, GE, LT, LE, EQ, NQ)

    @classmethod
    def getCode(cls, text):
        ''' Gets the code corresponding to the string representation.'''
        return cls.opcodes.get(text, cls.NOP)

    @classmethod
    def getString(cls, rop):
        '''Gets custom string representation for each operation.'''
        return cls.opnames[rop]


class STLFormula(object):
    '''Abstract Syntax Tree representation of an STL formula
    
    Contains nested STLFormula objects for child subformulae. Also contains
    interval definitions for temporal operators.
    
    Instance Attributes
    ----------
    op (int): opcode for the STL operation represented by this object
    child (STLFormula): object associated with nested subformula of a unary operator - defined 
                        only for ALWAYS, EVENT, and NOT operations
    children (list): list of STLFormula objects associated with each nested subformula - defined
                     only for AND and OR operations
    left (STLFormula): object associated with the left subformula of a binary non-commutative 
                       operator - defined only for UNTIL and IMPLIES operations
    right (STLFormula): object associated with the right subformula of a binary non-commutative 
                        operator - defined only for UNTIL and IMPLIES operations
    low (int or float): time value associated with the interval start of a temporal operator - 
                        defined only for ALWAYS, EVENT, and UNTIL operations
    high (int or float): time value associated with the interval end of a temporal operator - 
                         defined only for ALWAYS, EVENT, and UNTIL operations
    value (bool): representation of 0/1 literals passed in to the STL formula - defined only for 
                  BOOL operations
    variable (str): name of variable passed in to STL formula - defined only for PRED operations
    relation (int): opcode for the relationship between variable and threshold - defined only for
                    PRED operations
    threshold (int or float): threshold value for signal satisfaction - defined only for PRED operations
    '''

    def __init__(self, operation, **kwargs):
        '''Construct formula object from key word arguments passed by formula tree visitor
        Parameters:
        ----------
        operation (int): opcode for the STL operation at the root of the subtree.
        '''
        self.op = operation

        if self.op == Operation.BOOL:
            self.value = kwargs['value']
        elif self.op == Operation.PRED:
            self.relation = kwargs['relation']
            self.variable = kwargs['variable']
            self.threshold = kwargs['threshold']
        elif self.op in (Operation.AND, Operation.OR):
            self.children = kwargs['children']
        elif self.op == Operation.IMPLIES:
            self.left = kwargs['left']
            self.right = kwargs['right']
        elif self.op == Operation.NOT:
            self.child = kwargs['child']
        elif self.op in(Operation.ALWAYS, Operation.EVENT):
            self.low = kwargs['low']
            self.high = kwargs['high']
            self.child = kwargs['child']
        elif self.op == Operation.UNTIL:
            self.low = kwargs['low']
            self.high = kwargs['high']
            self.left = kwargs['left']
            self.right = kwargs['right']

        self.__string = None
        self.__hash = kwargs['UUID'] if 'UUID' in kwargs else None

    def robustness(self, s, t, max_robustness=1):
        '''Computes the robustness of a trajectory with respect to the STL formula at time t.
        Recursively evaluates the robustness of all necessary subformulae.
        
        Parameters:
        ----------
        s (Trace or TraceBatch): trajectory (or trajectories) to evaluate.
        t (int or float): time at which to evaluate the robustness.
        max_robustness (int or float): default=1 - robustness to be used for satisfaction of
                                                   boolean predicates.
        
        Returns:
        ----------
        res (np.ndarray or np.float64): robustness of the trajectory with respect to the STL 
                                        formula at time t. If s is a TraceBatch, res is a 1D 
                                        array of robustness values for each trace. Otherwise,
                                        res is a float.
        '''
        no_signals = s.number_signals()
        if self.op == Operation.BOOL:
            ret = np.array([max_robustness] * no_signals)
            if self.value:
                return ret
            else:
                return -ret
        elif self.op == Operation.PRED:
            value = s.value(self.variable, t)
            if self.relation in (RelOperation.GE, RelOperation.GT):
                return  value - self.threshold
            elif self.relation in (RelOperation.LE, RelOperation.LT):
                return self.threshold - value
            elif self.relation == RelOperation.EQ:
                return -np.abs(value - self.threshold)
            elif self.relation == RelOperation.NQ:
                return np.abs(value - self.threshold)
        elif self.op == Operation.AND:
            res = np.array([child.robustness(s, t, max_robustness)
                                        for child in self.children])
            return np.amin(res, axis=0)
        elif self.op == Operation.OR:
            res = np.array([child.robustness(s, t, max_robustness)
                                        for child in self.children])
            return np.amax(res, axis=0)
        elif self.op == Operation.IMPLIES:
            return np.maximum(-self.left.robustness(s, t, max_robustness),
                              self.right.robustness(s, t, max_robustness))
        elif self.op == Operation.NOT:
            return -self.child.robustness(s, t, max_robustness)
        elif self.op == Operation.UNTIL:
            res = np.array([self.left.robustness(s, t+tau, max_robustness)
                                              for tau in np.arange(self.low+1)])
            r_acc = np.amin(res, axis = 0)
            rleft = (self.left.robustness(s, t+tau, max_robustness)
                                    for tau in np.arange(self.low, self.high+1))
            rright = (self.right.robustness(s, t+tau, max_robustness)
                                    for tau in np.arange(self.low, self.high+1))
            value = -np.array([max_robustness] * no_signals)
            for rl, rr in zip(rleft, rright):
                r_acc = np.minimum(r_acc, rl)
                r_conj = np.minimum(r_acc, rr)
                value = np.maximum(value, r_conj)
            return value
        elif self.op == Operation.ALWAYS:
            res = np.array([self.child.robustness(s, t+tau, max_robustness)
                                for tau in np.arange(self.low, self.high+1)])
            return np.amin(res, axis=0)
        elif self.op == Operation.EVENT:
            res = np.array([self.child.robustness(s, t+tau, max_robustness)
                                for tau in np.arange(self.low, self.high+1)])
            return np.amax(res, axis=0)

    def negate(self):
        '''Computes the negation of the STL formula by propagating the negation towards predicates. 
        Modifies tree structure in place.
        '''
        self.__string = None
        if self.op == Operation.BOOL:
            self.value = not self.value
        elif self.op == Operation.PRED:
            self.relation = RelOperation.negop[self.relation]
        elif self.op in (Operation.AND, Operation.OR):
            [child.negate() for child in self.children]
        elif self.op == Operation.IMPLIES:
            self.right = self.right.negate()
        elif self.op == Operation.NOT:
            return self.child
        elif self.op == Operation.UNTIL:
            raise NotImplementedError
        elif self.op in (Operation.ALWAYS, Operation.EVENT):
            self.child = self.child.negate()
        self.op = Operation.negop[self.op]
        return self

    def pnf(self, insert_inverse_variables=False):
        '''Computes the Positive Normal Form of the STL formula. Modifies the tree structure in place.
        
        Parameters:
        ----------
        insert_negation_variables: default=False - if truthy, any predicate variables requiring negation
                                                   will be replaced by new variables named <var_name>_neg
                                                   in place of the negation operation.
        '''
        self.__string = None
        flag = insert_inverse_variables
        if self.op == Operation.PRED:
            if self.relation in (RelOperation.LE, RelOperation.LT):
                if insert_inverse_variables:
                    self.relation = RelOperation.invop[self.relation]
                    self.variable = f'{self.variable}_neg'
                    self.threshold = -self.threshold
            elif self.relation in (RelOperation.EQ, RelOperation.NQ):
                if self.relation == RelOperation.EQ:
                    op = Operation.AND
                    rel1 = RelOperation.GE
                else: # self.relation == RelOperation.NQ
                    op = Operation.OR
                    rel1 = RelOperation.GT
                if insert_inverse_variables:
                    if self.relation == RelOperation.EQ:
                        rel2 = RelOperation.GE
                    else: # self.relation == RelOperation.NQ
                        rel2 = RelOperation.GT
                    var_neg = f'{self.variable}_neg'
                    thr = -self.threshold
                else:
                    if self.relation == RelOperation.EQ:
                        rel2 = RelOperation.LE
                    else: # self.relation == RelOperation.NQ
                        rel2 = RelOperation.LT
                    var_neg = self.variable
                    thr = self.threshold
                children = [STLFormula(Operation.PRED, relation=rel1,
                              variable=self.variable, threshold=self.threshold),
                            STLFormula(Operation.PRED, relation=rel2,
                              variable=var_neg, threshold=thr)]
                return STLFormula(op, children=children)
        elif self.op in (Operation.AND, Operation.OR):
            self.children = [child.pnf(flag) for child in self.children]
        elif self.op == Operation.IMPLIES:
            self.left = self.left.negate().pnf(flag)
            self.right = self.right.pnf(flag)
            self.op = Operation.OR
        elif self.op == Operation.NOT:
            return self.child.negate().pnf(flag)
        elif self.op == Operation.UNTIL:
            raise NotImplementedError
        elif self.op in (Operation.ALWAYS, Operation.EVENT):
            self.child = self.child.pnf(flag)
        return self

    def bound(self):
        '''Computes an upper bound for the maximum time with could affect the satisfaction or 
        violation of the STL formula at t=0.
        
        Returns:
        ----------
        t (int or float): Latest relevant time for analysis of self.formula at t=0.
        '''
        if self.op in (Operation.BOOL, Operation.PRED):
            return 0
        elif self.op in (Operation.AND, Operation.OR):
            return max([ch.bound() for ch in self.children])
        elif self.op == Operation.IMPLIES:
            return max(self.left.bound(), self.right.bound())
        elif self.op == Operation.NOT:
            return self.child.bound()
        elif self.op == Operation.UNTIL:
            return self.high + max(self.left.bound(), self.right.bound())
        elif self.op in (Operation.ALWAYS, Operation.EVENT):
            return self.high + self.child.bound()

    def variables(self):
        '''Finds all variables used in the STL formula specification.
        
        Returns:
        ----------
        vars (set): The set of variable names (str) used in the STL formula.
        '''
        if self.op == Operation.BOOL:
            return set()
        elif self.op == Operation.PRED:
            return {self.variable}
        elif self.op in (Operation.AND, Operation.OR):
            return set.union(*[child.variables() for child in self.children])
        elif self.op in (Operation.IMPLIES, Operation.UNTIL):
            return self.left.variables() | self.right.variables()
        elif self.op in (Operation.NOT, Operation.ALWAYS, Operation.EVENT):
            return self.child.variables()

    def identifier(self):
        '''Computes the subformula ID in a manner safe for use as a gurobi variable name.
        
        Returns:
        ----------
        id (int): A gurobi-safe hash ID (64-bit) for the subformula stored in self.formula.
        '''
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
        if self.op == Operation.BOOL:
            s = '{value}'.format(value=self.value)
        elif self.op == Operation.PRED:
            s = '({v} {rel} {th})'.format(v=self.variable, th=self.threshold,
                                    rel=RelOperation.getString(self.relation))
        elif self.op == Operation.IMPLIES:
            s = '{left} {op} {right}'.format(left=self.left, op=opname,
                                             right=self.right)
        elif self.op in (Operation.AND, Operation.OR):
            children = [str(child) for child in self.children]
            s = '(' + ' {op} '.format(op=opname).join(children) + ')'
        elif self.op == Operation.NOT:
            s = '{op} {child}'.format(op=opname, child=self.child)
        elif self.op == Operation.UNTIL:
            s = '({left} {op}[{low}, {high}] {right})'.format(op=opname,
                 left=self.left, right=self.right, low=self.low, high=self.high)
        elif self.op in (Operation.ALWAYS, Operation.EVENT):
            s = '({op}[{low}, {high}] {child})'.format(op=opname,
                                 low=self.low, high=self.high, child=self.child)
        self.__string = s
        return self.__string


class STLAbstractSyntaxTreeExtractor(stlVisitor):
    '''Parse tree visitor that constructs the AST of an STL formula.
    Relies on inherited functionality from antlr to populate context.
    Recursively populates STLFormula objects using data extracted from 
    formula parser.
    '''
    def __init__(self, UUID=False):
        '''Override of stlVisitor constructor to allow for optional generation of unique identifiers for 
        subformulae.

        Parameters:
        ----------
        UUID (boolean): whether to generate unique identifiers for subformulae
        '''
        super().__init__()
        self._trackUUID = UUID
    def visit(self, ctx):
        '''Override of stlVisitor visit method to allow propagation of unique identifiers for subformulae.
        Assigns the first identifier at the root of the parse tree. All other subformula ID's are derived
        from this one.

        Parameters:
        ----------
        ctx (antlr4.ParserRuleContext): Context generated by antlr for this operation in the parse tree.
        '''
        if self._trackUUID and not hasattr(ctx, 'ID'):
            ctx.ID = hash(str(ctx))
        return super().visit(ctx)
    def visitFormula(self, ctx):
        '''Extract data from contexts that have been identified as subformulae by antlr.
        
        Parameters:
        ----------
        ctx (stlParser.FormulaContext): Context generated by antlr for this operation in the parse tree.
        '''
        op = Operation.getCode(ctx.op.text)
        ret = None
        low = -1
        high = -1
        UUID = (ctx.ID if self._trackUUID else None)
        if op in (Operation.AND, Operation.OR):
            if self._trackUUID:
                ctx.left.ID = hash(str(ctx.left)) ^ ctx.ID
                ctx.right.ID = hash(str(ctx.right)) ^ ctx.ID
            left = self.visit(ctx.left)
            right = self.visit(ctx.right)
            assert op != right.op
            if left.op == op:
                children = left.children
            else:
                children = [left]
            children.append(right)
            ret = STLFormula(op, children=children, UUID = UUID)
        elif op == Operation.IMPLIES:
            if self._trackUUID:
                ctx.left.ID = hash(str(ctx.left)) ^ ctx.ID
                ctx.right.ID = hash(str(ctx.right)) ^ ctx.ID
            ret = STLFormula(op, left=self.visit(ctx.left),
                             right=self.visit(ctx.right), UUID = UUID)
        elif op == Operation.NOT:
            if self._trackUUID:
                ctx.child.ID = hash(str(ctx.child)) ^ ctx.ID
            ret = STLFormula(op, child=self.visit(ctx.child), UUID = UUID)
        elif op == Operation.UNTIL:
            if self._trackUUID:
                ctx.left.ID = hash(str(ctx.left)) ^ ctx.ID
                ctx.right.ID = hash(str(ctx.right)) ^ ctx.ID
            low = float(ctx.low.text)
            high = float(ctx.high.text)
            ret = STLFormula(op, left=self.visit(ctx.left),
                             right=self.visit(ctx.right), low=low, high=high, UUID = UUID)
        elif op in (Operation.ALWAYS, Operation.EVENT):
            if self._trackUUID:
                ctx.child.ID = hash(str(ctx.child)) ^ ctx.ID
            low = float(ctx.low.text)
            high = float(ctx.high.text)
            ret = STLFormula(op, child=self.visit(ctx.child),
                             low=low, high=high, UUID = UUID)
        else:
            print('Error: unknown operation!')
        return ret

    def visitBooleanPred(self, ctx):
        expr = ctx.booleanExpr()
        if self._trackUUID:
            expr.ID = hash(str(expr)) ^ ctx.ID
        return self.visit(expr)

    def visitBooleanExpr(self, ctx):
        '''Extract data from contexts that have been identified as predicates by antlr
        
        Parameters:
        ----------
        ctx (mtlParser.BooleanExprContext): Context generated by antlr for this operation in the parse tree.
        '''
        UUID = (ctx.ID if self._trackUUID else None)
        if ctx.op.text.lower() in ('true', 'false'):
            value = ctx.op.text.lower() == 'true'
            return STLFormula(Operation.BOOL, value=value, UUID = UUID)
        return STLFormula(Operation.PRED,
            relation=RelOperation.getCode(ctx.op.text),
            variable=ctx.left.getText(), threshold=float(ctx.right.getText()), UUID = UUID)

    def visitParprop(self, ctx):
        if self._trackUUID:
            ctx.child.ID = hash(str(ctx.child)) ^ ctx.ID
        return self.visit(ctx.child)


def to_ast(formula, UUID=False):
    '''Transforms a formula string to an Abstract Syntax Tree in one shot.
    Parses formula with antlr and then generates STLFormula objects.
    
    Parameters:
    ----------
    formula (str): A string representation of the STL formula.
    UUID (boolean): default=False - If truthy, identical subtrees will be uniquely identifiable
                                    via their ID. This is needed for some optimization problems
                                    where the ancestry of a subtree matters with respect to its
                                    priority for satisfaction.
    
    Returns:
    ----------
    ast (STLFormula): Root node of the generated AST.
    '''
    lexer = stlLexer(InputStream(formula))
    tokens = CommonTokenStream(lexer)
    parser = stlParser(tokens)
    t = parser.stlProperty()
    ast = STLAbstractSyntaxTreeExtractor(UUID).visit(t)
    return ast

if __name__ == '__main__':
    from pytelo._internal.Trace import Trace, TraceBatch
    
    formula = ("!(x > 10) && F[0, 2] y > 2 && G[1, 3] z<=8")

    ast = to_ast(formula)
    print('AST:', str(ast))

    varnames = ['x', 'y', 'z']
    data = [[8, 8, 11, 11, 11], [2, 3, 1, 2, 2], [3, 9, 8, 9, 9]]
    timepoints = [0, 1, 2, 3, 4]
    s = Trace(varnames, timepoints, data)

    print('r:', ast.robustness(s, 0, 20))

    varnames = ['x', 'y', 'z']
    data = [[[8, 8, 11, 11, 11], [2, 3, 1, 2, 2], [3, 9, 8, 9, 9]],
            [[10, 9, 11, 11, 11], [2, 3, 1, 2, 2], [3, 9, 8, 9, 9]],
            [[8, 8, 11, 11, 11], [2, 3, 1, 2, 2], [3, 5, 8, 7, 9]]
           ]
    timepoints = [0, 1, 2, 3, 4]
    s = TraceBatch(varnames, timepoints, data)

    print('r batch:', ast.robustness(s, 0, 20))

    pnf = ast.pnf()
    print(pnf)
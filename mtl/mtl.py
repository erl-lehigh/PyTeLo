"""
 Copyright (c) 2023, Explainable Robotics Lab (ERL)
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
"""

from antlr4 import InputStream, CommonTokenStream

from mtlLexer import mtlLexer
from mtlParser import mtlParser
from mtlVisitor import mtlVisitor


class Operation(object):
    '''MTL operations'''
    NOP, NOT, OR, AND, IMPLIES, UNTIL, EVENT, ALWAYS, PRED, BOOL = range(10)
    opnames = [None, '!', '||', '&&', '=>', 'U', 'F', 'G', 'predicate', 'bool']
    opcodes = {'!': NOT, '&&': AND, '||' : OR, '=>': IMPLIES,
               'U': UNTIL, 'F': EVENT, 'G': ALWAYS}
    opstrnames = [None, 'not', 'or', 'and', 'imply', 'until', 'event', 'always',
                  'predicate', 'bool']
    # negation closure of operations
    negop = (NOP, NOP, AND, OR, AND, NOP, ALWAYS, EVENT, NOP, BOOL)

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


class MTLFormula(object):
    '''Abstract Syntax Tree representation of an MTL formula'''

    def __init__(self, operation, **kwargs):
        '''Constructor'''
        self.op = operation

        if self.op == Operation.BOOL:
            self.value = kwargs['value']
        elif self.op == Operation.PRED:
            self.variable = kwargs['variable']
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
        self.__hash = None

    def negate(self):
        '''Computes the negation of the MTL formula by propagating the negation
        towards predicates.
        '''
        self.__string = None
        if self.op == Operation.BOOL:
            self.value = not self.value
        elif self.op == Operation.PRED:
            return MTLFormula(Operation.NOT, child=self)
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

    def pnf(self, insert_negation_variables=False):
        '''Computes the Positive Normal Form of the MTL formula.

        Note: The tree structure is modified in-place.
        '''
        self.__string = None
        if self.op in (Operation.AND, Operation.OR):
            self.children = [child.pnf() for child in self.children]
        elif self.op == Operation.IMPLIES:
            self.left = self.left.negate().pnf()
            self.right = self.right.pnf()
            self.op = Operation.OR
        elif self.op == Operation.NOT:
            if self.child.op != Operation.PRED:
                return self.child.negate().pnf()
            elif insert_negation_variables:
                self.child.variable = f'{self.child.variable}_neg'
                return self.child
        elif self.op == Operation.UNTIL:
            raise NotImplementedError
        elif self.op in (Operation.ALWAYS, Operation.EVENT):
            self.child = self.child.pnf()
        return self

    def bound(self):
        '''Computes the bound of the MTL formula.'''
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
        '''Computes the set of variables involved in the MTL formula.'''
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
            s = '{v}'.format(v=self.variable)
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


class MTLAbstractSyntaxTreeExtractor(mtlVisitor):
    '''Parse Tree visitor that constructs the AST of an MTL formula'''

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
            ret = MTLFormula(op, children=children)
        elif op == Operation.IMPLIES:
            ret = MTLFormula(op, left=self.visit(ctx.left),
                             right=self.visit(ctx.right))
        elif op == Operation.NOT:
            ret = MTLFormula(op, child=self.visit(ctx.child))
        elif op == Operation.UNTIL:
            low = float(ctx.low.text)
            high = float(ctx.high.text)
            ret = MTLFormula(op, left=self.visit(ctx.left),
                             right=self.visit(ctx.right), low=low, high=high)
        elif op in (Operation.ALWAYS, Operation.EVENT):
            low = float(ctx.low.text)
            high = float(ctx.high.text)
            ret = MTLFormula(op, child=self.visit(ctx.child),
                             low=low, high=high)
        else:
            print('Error: unknown operation!')
        return ret

    def visitBooleanPred(self, ctx):
        return self.visit(ctx.booleanExpr())

    def visitBooleanExpr(self, ctx):
        if ctx.op.text.lower() in ('true', 'false'):
            value = ctx.op.text.lower() == 'true'
            return MTLFormula(Operation.BOOL, value=value)
        return MTLFormula(Operation.PRED, variable=ctx.op.text)

    def visitParprop(self, ctx):
        return self.visit(ctx.child)


if __name__ == '__main__':
    lexer = mtlLexer(InputStream("!x && F[0, 2] y || G[1, 3] z"))
    # lexer = mtlLexer(InputStream("x"))
    tokens = CommonTokenStream(lexer)

    parser = mtlParser(tokens)
    t = parser.mtlProperty()
    print(t.toStringTree())

    ast = MTLAbstractSyntaxTreeExtractor().visit(t)
    print('AST:', str(ast))

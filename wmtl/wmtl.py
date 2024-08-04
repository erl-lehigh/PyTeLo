'''
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
 @author: Gustavo A. Cardona, Cristian-Ioan Vasile
'''

import numpy as np

from antlr4 import InputStream, CommonTokenStream
from wmtlLexer import wmtlLexer
from wmtlParser import wmtlParser
from wmtlVisitor import wmtlVisitor
from mtl import Operation, MTLFormula

class WMTLFormula(MTLFormula):
    '''Abstract Syntax Tree representation of an WMTL formula. The class is
    derived from MTLFormula.
    '''

    def __init__(self, operation, **kwargs):
        '''Constructor

        Parameters
        ----------
        operation (mtl.Operation) operation code.
        value (bool, optional) value of a Boolean constant.
        variable (string, optional) name of a predicate's variable.
        left (WMTLFormula, optional) left AST subtree of binary operations.
        right (WMTLFormula, optional) right AST subtree of binary operations.
        child (WMTLFormula, optional) child AST subtree of unary operations.
        children (WMTLFormula, optional) children AST subtrees of n-ary
            operations (i.e., disjuction and conjuction).
        low (int, optional) lower bound of the time interval associate with a
            temporal operator.
        high (int, optional) upper bound of the time interval associate with a
            temporal operator.
        weight (function, optional, default: None) weight function associated
            with weighted operators.
        '''
        MTLFormula.__init__(self, operation, **kwargs)

        if self.op in (Operation.AND, Operation.OR, Operation.ALWAYS, 
                       Operation.EVENT, Operation.UNTIL):
            self.weight = kwargs.get('weight', None)

        self.__string = None # string representation cache for quick lookup

    def bound(self):
        '''Computes the bound of the WTL formula.'''
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
            
    def __str__(self):
        '''Computes the string representation. The result is cached internally
        for quick subsequent calls.

        Returns
        -------
        (string) formula string
        '''
        if self.__string is not None:
            return self.__string

        opname = Operation.getString(self.op)
        if self.op == Operation.BOOL:
            s = str(self.value)
        elif self.op == Operation.PRED:
           s = '{v}'.format(v=self.variable)
        elif self.op == Operation.IMPLIES:
            s = '{left} {op} {right}'.format(left=self.left, op=opname,
                                             right=self.right)
        elif self.op == Operation.NOT:
            s = '{op} {child}'.format(op=opname, child=self.child)
        else:
            if self.weight is None:
                op_weight = ''
            else:
                op_weight = '^{weight}'.format(weight=self.weight.__name__)

            if self.op in (Operation.AND, Operation.OR):
                children = [str(child) for child in self.children]
                join_str = ' {op}{weight} '.format(op=opname, weight=op_weight)
                s = '(' + join_str.join(children) + ')'
            elif self.op == Operation.UNTIL:
                s = '({left} {op}[{low}, {high}]{weight} {right})'.format(
                      op=opname, weight=op_weight, left=self.left,
                      right=self.right, low=self.low, high=self.high)
            elif self.op in (Operation.ALWAYS, Operation.EVENT):
                s = '({op}[{low}, {high}]{weight} {child})'.format(op=opname,
                      weight=op_weight, low=self.low, high=self.high,
                      child=self.child)
        self.__string = s
        return self.__string


class WMTLAbstractSyntaxTreeExtractor(wmtlVisitor):
    '''Parse Tree visitor that constructs the AST of an WMTL formula'''

    def __init__(self, predicate_weights):
        '''Constructor

        Parameters
        ----------
        predicate_weights (dictionary) maps the names of predicate weights to
            funtions implementing them.
        '''
        wmtlVisitor.__init__(self)
        self.predicate_weights = predicate_weights

    def getWeight(self, ctx):
        '''Returns the weight function from the node/rule context.

        Parameters
        ----------
        ctx (ParseRuleContext) the context of a rule.

        Returns
        -------
        weight (function) the implementation of weight
        '''
        if ctx.weight is None:
            weight = None
        else:
            weight = self.predicate_weights[ctx.weight.text]
            # make sure the function retains the name from the specification
            if weight.__name__ != ctx.weight.text:
                weight.__name = ctx.weight.text
        return weight

    def visitFormula(self, ctx):
        '''Transforms a parse tree associated with Boolean and temporal
        operators into an AST of the associated WMTL formula.

        Parameters
        ----------
        ctx (ParseRuleContext) the context of a rule.

        Returns
        -------
        (wmtl.WMTLFormula) AST of the WMTL formula.
        '''
        op = Operation.getCode(ctx.op.text)
        ret = None
        low = -1
        high = -1
        if op in (Operation.AND, Operation.OR):
            left = self.visit(ctx.left)
            right = self.visit(ctx.right)
            weight = self.getWeight(ctx)
            assert op != right.op
            if left.op == op and left.weight == weight:
                children = left.children
            else:
                children = [left]
            children.append(right)
            ret = WMTLFormula(op, children=children, weight=weight)
        elif op == Operation.IMPLIES:
            ret = WMTLFormula(op, left=self.visit(ctx.left),
                             right=self.visit(ctx.right))
        elif op == Operation.NOT:
            ret = WMTLFormula(op, child=self.visit(ctx.child))
        # elif op in (Operation.UNTIL):
        #     low = float(ctx.low.text)
        #     high = float(ctx.high.text)
        #     weight = self.getWeight(ctx)
        #     ret = WMTLFormula(op, weight=weight, left=self.visit(ctx.left),
        #                      right=self.visit(ctx.right), low=low, high=high)
        elif op in (Operation.ALWAYS, Operation.EVENT):
            low = float(ctx.low.text)
            high = float(ctx.high.text)
            ret = WMTLFormula(op, weight=self.getWeight(ctx),
                              child=self.visit(ctx.child), low=low, high=high)
        else:
            raise ValueError('Error: unknown operation {}!'.format(ctx.op.text))
        return ret

    def visitLongFormula(self, ctx):
        '''Transforms a parse tree associated with Boolean disjuction and
        conjuction operators in long format into an AST of the associated WMTL
        formula.

        Parameters
        ----------
        ctx (ParseRuleContext) the context of a rule.

        Returns
        -------
        (wmtl.WMTLFormula) AST of the WMTL formula.
        '''
        op = Operation.getCode(ctx.op.text)
        assert op in (Operation.AND, Operation.OR)
        # extract child sub-formulae
        children = (self.visit(child) for child in ctx.getChildren())
        children = [child for child in children if child is not None]
        return WMTLFormula(op, children=children, weight=self.getWeight(ctx))

    def visitBooleanPred(self, ctx):
        '''Parses Boolean predicates.

        Parameters
        ----------
        ctx (ParseRuleContext) the context of a rule.

        Returns
        -------
        (wmtl.WMTLFormula) AST of the WMTL predicate.
        '''
        return self.visit(ctx.booleanExpr())

    def visitBooleanExpr(self, ctx):
        '''Transforms a parse tree associated with Boolean expression of a
        predicate into an AST terminal leaf.

        Parameters
        ----------
        ctx (ParseRuleContext) the context of a rule.

        Returns
        -------
        (wmtl.WMTLFormula) AST of the WMTL predicate.
        '''
        return WMTLFormula(Operation.PRED, variable=ctx.op.text)

    def visitParprop(self, ctx):
        '''Parses properties within parantheses.

        Parameters
        ----------
        ctx (ParseRuleContext) the context of a rule.

        Returns
        -------
        (wmtl.WMTLFormula) AST of the WMTL predicate.
        '''
        return self.visit(ctx.child)

def to_ast(formula, weights):
    '''Transforms a formula string to an Abstract Syntax Tree.'''
    lexer = wmtlLexer(InputStream(formula))
    tokens = CommonTokenStream(lexer)
    parser = wmtlParser(tokens)
    t = parser.wmtlProperty()
    ast = WMTLAbstractSyntaxTreeExtractor(weights).visit(t)
    return ast

if __name__ == '__main__':
    formula = "&&^p1 (x, y)"
    weights = {
        'p1': lambda i: i + 1,
        'p2': lambda i: 2 - i,
        'w1': lambda x: 2 - np.abs(x - 1),
        'w2': lambda x: 1 + (x-2)**2
    }
    
    ast = to_ast(formula, weights)
    print('AST:', ast)

    varnames = ['x', 'y', 'z']
    data = [[8, 8, 11, 11, 11], [2, 3, 1, 2, 2], [3, 9, 8, 9, 9]]
    timepoints = [0, 1, 2, 3, 4]
    
    pnf = ast.pnf()
    print(pnf)
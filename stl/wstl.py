'''
 Copyright (C) 2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
'''

import itertools as it

import numpy as np
from antlr4 import InputStream, CommonTokenStream

from stl import Operation, RelOperation, STLFormula, Trace
from wstlLexer import wstlLexer
from wstlParser import wstlParser
from wstlVisitor import wstlVisitor


class WSTLFormula(STLFormula):
    '''Abstract Syntax Tree representation of an WSTL formula. The class is
    derived from STLFormula.
    '''

    def __init__(self, operation, **kwargs):
        '''Constructor

        Parameters
        ----------
        operation (stl.Operation) operation code.
        value (bool, optional) value of a Boolean constant.
        variable (string, optional) name of a predicate's variable.
        relation (stl.RelOperation, optional) relation of a predicate.
        threshold (number, optional) threshold of a predicate.
        left (WSTLFormula, optional) left AST subtree of binary operations.
        right (WSTLFormula, optional) right AST subtree of binary operations.
        child (WSTLFormula, optional) child AST subtree of unary operations.
        children (WSTLFormula, optional) children AST subtrees of n-ary
            operations (i.e., disjuction and conjuction).
        low (int, optional) lower bound of the time interval associate with a
            temporal operator.
        high (int, optional) upper bound of the time interval associate with a
            temporal operator.
        weight (function, optional, default: None) weight function associated
            with weighted operators.
        '''
        STLFormula.__init__(self, operation, **kwargs)

        if self.op in (Operation.AND, Operation.OR, Operation.ALWAYS,
                       Operation.EVENT, Operation.UNTIL):
            self.weight = kwargs.get('weight', None)

        self.__string = None # string representation cache for quick lookup

    def robustness(self, s, t, maximumRobustness=1):
        '''Computes the robustness of the STL formula.

        Parameters
        ----------
        s (stl.Trace) a signal
        t (number) time instant

        Returns
        -------
        (number) the traditional robustness of signal `s` at time `t` with
            respect to the formula `self`
        '''
        if self.op in (Operation.BOOL, Operation.PRED, Operation.NOT,
                       Operation.IMPLIES):
            return STLFormula.robustness(self, s, t, maximumRobustness)
        elif self.weight is None:
            return STLFormula.robustness(self, s, t, maximumRobustness)
        elif self.op == Operation.AND:
            return min(child.robustness(s, t) * self.weight(k)
                       for k, child in enumerate(self.children))
        elif self.op == Operation.OR:
            return max(child.robustness(s, t) * self.weight(k)
                       for k, child in enumerate(self.children))
        elif self.op == Operation.UNTIL:
            r_acc = min(self.left.robustness(s, t+tau)
                                               for tau in np.arange(self.low+1))
            rleft = (self.left.robustness(s, t+tau)
                                    for tau in np.arange(self.low, self.high+1))
            rright = (self.right.robustness(s, t+tau) * self.weight(tau)
                                    for tau in np.arange(self.low, self.high+1))
            value = -maximumRobustness
            for rl, rr in zip(rleft, rright):
                r_acc = min(r_acc, rl)
                r_conj = min(r_acc, rr)
                value = max(value, r_conj)
            return value
        elif self.op == Operation.ALWAYS:
            return min(self.child.robustness(s, t+tau) * self.weight(tau)
                       for tau in np.arange(self.low, self.high+1))
        elif self.op == Operation.EVENT:
            return max(self.child.robustness(s, t+tau) * self.weight(tau)
                       for tau in np.arange(self.low, self.high+1))

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
            s = '({v} {rel} {th})'.format(v=self.variable, th=self.threshold,
                                    rel=RelOperation.getString(self.relation))
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


class WSTLAbstractSyntaxTreeExtractor(wstlVisitor):
    '''Parse Tree visitor that constructs the AST of an WSTL formula'''

    def __init__(self, predicate_weights):
        '''Constructor

        Parameters
        ----------
        predicate_weights (dictionary) maps the names of predicate weights to
            funtions implementing them.
        '''
        wstlVisitor.__init__(self)
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
        operators into an AST of the associated WSTL formula.

        Parameters
        ----------
        ctx (ParseRuleContext) the context of a rule.

        Returns
        -------
        (wstl.WSTLFormula) AST of the WSTL formula.
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
            ret = WSTLFormula(op, children=children, weight=weight)
        elif op == Operation.IMPLIES:
            ret = WSTLFormula(op, left=self.visit(ctx.left),
                             right=self.visit(ctx.right))
        elif op == Operation.NOT:
            ret = WSTLFormula(op, child=self.visit(ctx.child))
        elif op == Operation.UNTIL:
            low = float(ctx.low.text)
            high = float(ctx.high.text)
            weight = self.getWeight(ctx)
            ret = WSTLFormula(op, weight=weight, left=self.visit(ctx.left),
                             right=self.visit(ctx.right), low=low, high=high)
        elif op in (Operation.ALWAYS, Operation.EVENT):
            low = float(ctx.low.text)
            high = float(ctx.high.text)
            ret = WSTLFormula(op, weight=self.getWeight(ctx),
                              child=self.visit(ctx.child), low=low, high=high)
        else:
            raise ValueError('Error: unknown operation {}!'.format(ctx.op.text))
        return ret

    def visitLongFormula(self, ctx):
        '''Transforms a parse tree associated with Boolean disjuction and
        conjuction operators in long format into an AST of the associated WSTL
        formula.

        Parameters
        ----------
        ctx (ParseRuleContext) the context of a rule.

        Returns
        -------
        (wstl.WSTLFormula) AST of the WSTL formula.
        '''
        op = Operation.getCode(ctx.op.text)
        assert op in (Operation.AND, Operation.OR)
        # extract child sub-formulae
        children = (self.visit(child) for child in ctx.getChildren())
        children = [child for child in children if child is not None]
        return WSTLFormula(op, children=children, weight=self.getWeight(ctx))

    def visitBooleanPred(self, ctx):
        '''Parses Boolean predicates.

        Parameters
        ----------
        ctx (ParseRuleContext) the context of a rule.

        Returns
        -------
        (wstl.WSTLFormula) AST of the WSTL predicate.
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
        (wstl.WSTLFormula) AST of the WSTL predicate.
        '''
        return WSTLFormula(Operation.PRED,
            relation=RelOperation.getCode(ctx.op.text),
            variable=ctx.left.getText(), threshold=float(ctx.right.getText()))

    def visitParprop(self, ctx):
        '''Parses properties within parantheses.

        Parameters
        ----------
        ctx (ParseRuleContext) the context of a rule.

        Returns
        -------
        (wstl.WSTLFormula) AST of the WSTL predicate.
        '''
        return self.visit(ctx.child);


if __name__ == '__main__':
    lexer = stlLexer(InputStream("!(x < 10) &&^p1 F[0, 2]^w1 y > 2"
                                 " ||^p2 G[1, 3]^w2 z<=8"))
    tokens = CommonTokenStream(lexer)

    parser = stlParser(tokens)
    t = parser.stlProperty()
    print(t.toStringTree())

    predicate_weights = {
        'p1': lambda i: i + 1,
        'p2': lambda i: 2 - i,
        'w1': lambda x: 2 - np.abs(x - 1),
        'w2': lambda x: 1 + (x-2)**2
    }
    ast = WSTLAbstractSyntaxTreeExtractor().visit(t)
    print('AST:', ast)

    varnames = ['x', 'y', 'z']
    data = [[8, 8, 11, 11, 11], [2, 3, 1, 2, 2], [3, 9, 8, 9, 9]]
    timepoints = [0, 1, 2, 3, 4]
    s = Trace(varnames, timepoints, data)

    print('r:', ast.robustness(s, 0))

    pnf = ast.pnf()
    print(pnf)

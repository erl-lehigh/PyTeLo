'''
Copyright (C) 2019 Noushin Mehdipour <noushinm@bu.edu> and
2015-2019 Cristian Ioan Vasile <cvasile@bu.edu,cvasile@lehigh.edu>,
Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
See license.txt file for license information.
'''
from __future__ import print_function

import numpy as np
from antlr4 import InputStream, CommonTokenStream

from stlLexer import stlLexer
from stlParser import stlParser

from stl import Operation, RelOperation, STLAbstractSyntaxTreeExtractor, Trace


def powermean(vector, order):
    '''Computes the power mean of a vector.'''
    alpha = 1. / len(vector)
    if order == 'inf':
        return np.max(vector)
    elif order == '-inf':
        return np.min(vector)
    if order != 0:
        return np.sum(alpha * abs(vector)**order)**(1./order)
    else:
        # FIXME: should be: np.prod(abs(vector)) ** alpha
        return np.prod(1 + abs(vector)) ** alpha - 1

def conjunction_function(r_children, pos_order, neg_order):
    '''Computes the conjuction robustness value from children values.'''
    r_non_pos = r_children <= 0
    if np.any(r_non_pos):
        eta = -powermean(r_children * r_non_pos, order=neg_order)
    else:
        eta = powermean(r_children, order=pos_order)
    return eta

def disjunction_function(r_children, pos_order, neg_order):
    '''Computes the disjuction robustness value from children values.

    Note: Returns the same value as:
        -conjunction_function(-r_children, pos_order, neg_order)
    '''
    r_pos = r_children > 0
    if np.any(r_pos):
        eta = powermean(r_children * r_pos, order=neg_order)
    else:
        eta = -powermean(r_children, order=pos_order)
    return eta

def powermean_robustness(formula, trace, time, pos_order=0, neg_order=1,
                         maximum_robustness=1):
    '''Computes the powermean robustness of the STL formula.'''
    if formula.op == Operation.BOOL:
        if formula.value:
            return maximum_robustness
        else:
            return -maximum_robustness
    elif formula.op == Operation.PRED:
        value = trace.value(formula.variable, time)
        if formula.relation in (RelOperation.GE, RelOperation.GT):
            eta = value - formula.threshold
        elif formula.relation in (RelOperation.LE, RelOperation.LT):
            eta = formula.threshold - value
        elif formula.relation == RelOperation.EQ:
            eta = -abs(value - formula.threshold)
        elif formula.relation == RelOperation.NQ:
            eta = abs(value - formula.threshold)
        return eta / trace.range(formula.variable)

    if formula.op in (Operation.AND, Operation.OR):
        r_children = np.array([powermean_robustness(child, trace, time)
                               for child in formula.children],
                              dtype=np.float)
    elif formula.op in (Operation.ALWAYS, Operation.EVENT):
        r_children = np.array(
            [powermean_robustness(formula.child, trace, time + tau)
             for tau in np.arange(formula.low, formula.high + 1)],
            dtype=np.float)
    if formula.op in (Operation.AND, Operation.ALWAYS):
        eta = conjunction_function(r_children, pos_order, neg_order)
        return eta
    elif formula.op in (Operation.OR, Operation.EVENT):
        eta = disjunction_function(r_children, pos_order, neg_order)
        return eta

    if formula.op == Operation.NOT:
        return -powermean_robustness(formula.child, trace, time)
    elif formula.op in (Operation.IMPLIES, Operation.UNTIL):
        raise NotImplementedError
    else:
        raise ValueError('Unknown operation code {}!'.format(formula.op))


class BoundedTrace(Trace):
    '''Representation of a bounded system trace.'''

    def __init__(self, variables, time_points, data, bounds, kind='nearest'):
        '''Constructor'''
        Trace.__init__(self, variables, time_points, data, kind)
        self.bounds = bounds

    def range(self, variable):
        '''Return the range for each parameter'''
        var_bounds = self.bounds[variable]
        return var_bounds[1] - var_bounds[0]


if __name__ == '__main__':
    lexer = stlLexer(InputStream('!(x < 10) && F[0, 2] y > 2 || G[1, 3] z<=8'
                                 ' && G[4, 6] z>8'))
    #lexer = stlLexer(InputStream("G[4, 6] z>8"))
    tokens = CommonTokenStream(lexer)

    parser = stlParser(tokens)
    parse_tree = parser.stlProperty()
    print(parse_tree.toStringTree())

    ast = STLAbstractSyntaxTreeExtractor().visit(parse_tree)
    print('AST:', ast)

    var_names = ['x', 'y', 'z']
    var_values = [[8, 8, 11, 11, 11, 1, 1],
                  [1, 3, 2, 2, 2, 0, 0],
                  [3, 9, 8, 9, 9, 9, 9]]
    time_points = [0, 1, 2, 3, 4, 5, 6]
    data_bounds = {'x': (0, 20), 'y': (0, 10), 'z': (0, 10)}
    s = BoundedTrace(var_names, time_points, var_values, data_bounds)

    print('r:', powermean_robustness(ast, s, 0))

    pnf = ast.pnf()
    print(pnf)

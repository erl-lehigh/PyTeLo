#!/usr/bin/env python3

"""
 Copyright (C) 2022 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.

 @author: Cristian-Ioan Vasile
"""
from antlr4 import InputStream, CommonTokenStream

import sys
sys.path.append('..')

from stl import Operation, RelOperation, STLFormula
from stlLexer import stlLexer
from stlParser import stlParser
from stlVisitor import stlVisitor

from stl import STLAbstractSyntaxTreeExtractor

from stl2milp import stl2milp
from stl_distance import stl_dist_milp, stl_directed_distance, stl_distance


def formula_distance(formula1, formula2, ranges, return_directed=False):
    '''
    '''
    ast = []
    for formula in [formula1, formula2]:
        lexer = stlLexer(InputStream(formula))
        tokens = CommonTokenStream(lexer)
        parser = stlParser(tokens)
        t = parser.stlProperty()
        print(t.toStringTree())
        ast.append(STLAbstractSyntaxTreeExtractor().visit(t))
        print('AST:', str(ast[-1]))
    return stl_distance(ast[0], ast[1], ranges, return_directed)

if __name__ == '__main__':
    # formula = "(x > 10) && F[0, 2] y > 2 || G[1, 6] z > 8"
    # formula = "G[2,4] F[1,3](x>=3)"
    # formula = "(x <= 10) && F[0, 2] y > 2 && G[1, 6] (z < 8) && G[1,6] (z > 3)"
    formula1 = 'x <= 4'
    formula2 = 'x <= 2'

    ranges={'x': [-4, 5], 'rho': [0, 100]}
    print('STLF Dist:', formula_distance(formula1, formula2, ranges))

    # stl_milp1 = stl_dist_milp(ast1, ranges={'x': [-4, 5]}, robust=False)
    # stl_milp1.translate(satisfaction=True)
    #
    # stl_milp2 = stl_dist_milp(ast2, ranges={'x': [-4, 5], 'rho': [0, 100]},
    #                           robust=True,
    #                           prefix='ext_', model=stl_milp1.model,
    #                           variables=stl_milp1.variables)
    # z = stl_milp2.translate(satisfaction=False)
    # stl_milp2.model.addConstr(z == 0, 'formula2_violation')
    #
    # stl_milp1.model.optimize()
    # model = stl_milp1.model
    #
    # print('Vars')
    # for var in model.getVars():
    #     print(var.VarName, ':', var.x)
    #
    # print('Constraints')
    # for constr in model.getConstrs():
    #     print(':', str(constr))
    #
    # print('Objective')
    # obj = model.getObjective()
    # print(str(obj), ':', obj.getValue())
    #
    # model.write('stl_dist.lp')
    #
    # print('STL d Dist:', stl_directed_distance(ast1, ast2, ranges))
    # print('STL Dist:', stl_distance(ast1, ast2, ranges))

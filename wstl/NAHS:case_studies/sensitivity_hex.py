from antlr4 import InputStream, CommonTokenStream
import time
import numpy as np
import matplotlib.pyplot as plt
import gurobipy as grb
import sys
import sensitivity
sys.path.append('../')

from stl import Operation, RelOperation, STLFormula
from wstlLexer import wstlLexer
from wstlParser import wstlParser
from wstlVisitor import wstlVisitor

from wstl import WSTLAbstractSyntaxTreeExtractor
from stl import STLAbstractSyntaxTreeExtractor
from long_wstl2milp import long_wstl2milp
from wstl2milp import wstl2milp
from stl2milp import stl2milp
# from gurobipy import *
from stlLexer import stlLexer
from stlParser import stlParser
from stlVisitor import stlVisitor
from stl import STLAbstractSyntaxTreeExtractor
from environment import environment, stl_zone, wstl_zone



def wstl_synthesis_control(wstl_formula, weights, A, B, vars_ub, vars_lb,
                           control_ub, control_lb, type='short'):
    lexer = wstlLexer(InputStream(wstl_formula))
    tokens = CommonTokenStream(lexer)
    parser = wstlParser(tokens)
    t = parser.wstlProperty()
    ast = WSTLAbstractSyntaxTreeExtractor(weights).visit(t)
    if type == 'long':
        wstl_milp = long_wstl2milp(ast)
    elif type == 'short':
        wstl_milp = wstl2milp(ast)
    else:
        raise NotImplementedError

    time_bound = int(ast.bound()) + 1
    # system variables and the time period
    x = dict()
    y = dict()
    z = dict()
    u = dict()
    v = dict()
    w = dict()

    for k in range(time_bound):
        name = "x_{}".format(k)
        x[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb,
                                      ub=vars_ub, name=name)
        name = "y_{}".format(k)
        y[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb,
                                      ub=vars_ub, name=name)
        name = "z_{}".format(k)
        z[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb,
                                      ub=vars_ub, name=name)
        name = "u_{}".format(k)
        u[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=control_lb,
                                      ub=control_ub, name=name)
        name = "v_{}".format(k)
        v[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=control_lb,
                                      ub=control_ub, name=name)
        name = "w_{}".format(k)
        w[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=control_lb,
                                      ub=control_ub, name=name)

    # use system variables in STL spec encoding
    wstl_milp.variables['x'] = x
    wstl_milp.variables['y'] = y
    wstl_milp.variables['z'] = z
    wstl_milp.variables['u'] = u
    wstl_milp.variables['v'] = v
    wstl_milp.variables['w'] = w

    # system constraints
    for k in range(time_bound - 1):
        wstl_milp.model.addConstr(x[k + 1] == A[0][0] * x[k] + A[0][1] * y[k] +
                                  A[0][2] * z[k] + B[0][0] * u[k] +
                                  B[0][1] * v[k] + B[0][2] * w[k])

        wstl_milp.model.addConstr(y[k + 1] == A[1][0] * x[k] + A[1][1] * y[k] +
                                  A[1][2] * z[k] + B[1][0] * u[k] +
                                  B[1][1] * v[k] + B[1][2] * w[k])

        wstl_milp.model.addConstr(z[k + 1] == A[2][0] * x[k] + A[2][1] * y[k] +
                                  A[2][2] * z[k] + B[2][0] * u[k] +
                                  B[2][1] * v[k] + B[2][2] * w[k])

    wstl_milp.model.addConstr(x[0] == -9)
    wstl_milp.model.addConstr(y[0] == -9)
    wstl_milp.model.addConstr(z[0] == 0)
    wstl_milp.model.addConstr(u[0] == 0)
    wstl_milp.model.addConstr(v[0] == 0)
    wstl_milp.model.addConstr(w[0] == 0)

    z_formula, rho_formula = wstl_milp.translate(satisfaction=True)
    wstl_milp.model.setObjective(rho_formula, grb.GRB.MAXIMIZE)
    wstl_milp.model.update()

    if type == 'long':
        wstl_milp.model.write('long_milp.lp')
    else:
        wstl_milp.model.write('short_milp.lp')

    # Solve problem
    wstl_milp.model.optimize()
    return wstl_milp


if __name__ == '__main__':
    # Formulas
    # formula = 'G[5,10] x >= 3 && G[5,10] (y <= -2) && G[5, 10] (z >= 1)'
    # wstl_formula = "&&^weight2 ( G[5,10]^weight0  (x>=3),G[5,10]^weight3 \
    #                 (y<=-2), G[5,10]^weight3 (z>=1) )"
    obstacle = "&&" + stl_zone("O", "G", 0, 30, "x", "y")
    formula = '(' + stl_zone("C", "G", 10, 15, "x", "y") + ' && ' + \
              stl_zone("D", "G", 25, 30, "x", "y") + ' && ' + \
              stl_zone("A", "G", 0, 1, "x", "y") + obstacle + ')'

    # formula = '(' + stl_zone("C", "F", 5, 6, "x", "y") + obstacle + ')'
    # wstl_formula=
    wstl_obs = wstl_zone("O", "G", 0, 30, "x", "y")
    wstl_formula = '&&^weight2 (' + wstl_zone("C", "G", 10, 15, "x", "y") + \
                   ',' + wstl_zone("D", "G", 25, 30, "x", "y") + \
                   ',' + wstl_zone("A", "G", 0, 1, "x", "y") + ',' + wstl_obs + ')'

    # wstl_formula = '&&^weight2 ('+','+wstl_zone("C", "F", 5, 6, "x", "y")+','+wstl_obs+')'
    # wstl_formula = '&&^weight0 ( G[0,2]^weight0 (||^weight0 ( ) ), F[2,2] )'

    # NOTE: Case same weights wstl=stl
    # weights = {'weight0': lambda x: 1, 'weight1': lambda x:10,
    #            'weight2': lambda k:[1, 1, 1, 1][k], 'weight3': lambda x: 1}

    # NOTE: case where there is higher weight to areas than avoiding the obstacle
    # weights = {'weight0': lambda x: 1, 'weight1': lambda x:10,
    #            'weight2': lambda k:[.1, .1, .1, .8][k], 'weight3': lambda x: 1}

    # NOTE: case where there is higher weight to avoiding the obstacle
    weights = {'weight0': lambda x: 1, 'weight1': lambda x: 10,
               'weight2': lambda k: [.9, .9, .9, .1][k], 'weight3': lambda x: 1}

    # Define the matrixes that used for linear system
    A = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    vars_ub = 9
    vars_lb = -9
    control_ub = 3
    control_lb = -3

    wstl_start = time.time()
    wstl_milp = wstl_synthesis_control(wstl_formula, weights, A, B, vars_ub,
                                       vars_lb, control_ub, control_lb)
    wstl_end = time.time()
    wstl_time = wstl_end - wstl_start






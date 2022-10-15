from __future__ import division
from antlr4 import InputStream, CommonTokenStream

import numpy as np
import matplotlib.pyplot as plt

import sys

sys.path.append('../')

from stl import Operation, RelOperation, STLFormula
from wstlLexer import wstlLexer
from wstlParser import wstlParser
from wstlVisitor import wstlVisitor

from wstl import WSTLAbstractSyntaxTreeExtractor
from stl import STLAbstractSyntaxTreeExtractor
from long_wstl2milp import long_wstl2milp
from short_wstl2milp import short_wstl2milp
from stl2milp import stl2milp
from gurobipy import *
from stlLexer import stlLexer
from stlParser import stlParser
from stlVisitor import stlVisitor
from stl import STLAbstractSyntaxTreeExtractor

def wstl_solve(wstl_formula, weights, type='short', varname='x', end_time=15):
    # Get/create state variables
    lexer = wstlLexer(InputStream(wstl_formula))
    tokens = CommonTokenStream(lexer)
    parser = wstlParser(tokens)
    t = parser.wstlProperty()
    ast = WSTLAbstractSyntaxTreeExtractor(weights).visit(t)
    if type == 'long':
        wstl_milp = long_wstl2milp(ast)
    elif type == 'short':
        wstl_milp = short_wstl2milp(ast)
    else:
        raise NotImplementedError
    z_formula, rho_formula = wstl_milp.translate()
    # x = [wstl_milp.variables[varname].get(time, wstl_milp.model.addVar(lb=-GRB.INFINITY,
    #                                                      ub=GRB.INFINITY))
    #      for time in range(end_time + 1)]
    wstl_milp.model.update()

    # Add dynamics constraints
    # for time in range(end_time): # example of state transition (system dynamics)
    #     m.addConstr(x[time+1] == x[time] + 0.1)

    # for time in range(end_time + 1):  # example if state constraints (e.g., safety)
    #     wstl_milp.model.addConstr(x[time] >= 0)

    # Set objective
    # reward = z_formula + rho_formula
    # wstl_milp.model.setObjectiveN(-rho_formula, 0, weight =2, name = 'robustness')
    # wstl_milp.model.setObjectiveN(z_formula, 1, weight =100, name = 'satis')
    # wstl_milp.model.setObjective(z_formula, GRB.MAXIMIZE)
    print(rho_formula, 'AQUI')
    wstl_milp.model.setObjective(rho_formula, GRB.MAXIMIZE)
    wstl_milp.model.update()
    if type == 'long':
        wstl_milp.model.write('long_milp.lp')
    else:
        wstl_milp.model.write('short_milp.lp')

    # Solve problem
    wstl_milp.model.optimize()

    # if (wstl_milp.model.status == 2):
    #     y = np.array([x[i].X for i in range(end_time + 1)], dtype=np.float)
    # else:
    #     print("cannot solve...")
    #     y = None
    y = [var.X for var in wstl_milp.variables['x'].values()]
    return wstl_milp


def stl_solve(stl_formula, varname='x', end_time=15):
    lexer = stlLexer(InputStream(stl_formula))
    tokens = CommonTokenStream(lexer)
    parser = stlParser(tokens)
    t = parser.stlProperty()
    print(t.toStringTree())
    ast = STLAbstractSyntaxTreeExtractor().visit(t)
    print("AST:", ast)

    stl_milp = stl2milp(ast, ranges={'x': [0, 10]}, robust=True)

    stl_milp.translate(satisfaction=True)
    x = [stl_milp.variables[varname].get(time, stl_milp.model.addVar(lb=-GRB.INFINITY,
                                                                     ub=GRB.INFINITY))
         for time in range(end_time + 1)]
    stl_milp.model.update()
    # Set objective
    stl_milp.model.write('stl_milp.lp')
    # Solve problem
    stl_milp.model.optimize()
    y = [var.X for var in stl_milp.variables['x'].values()]
    # print("y_stl:", y)
    # return wstl_milp


def visualize(end_time, x1, x2, x3):
    t = [i for i in range(0, end_time + 1)]
    # print("t;", t)
    # Print solution
    fig, ax = plt.subplots()
    ax.grid()
    ax.plot(t, x1, '-r', label='long')
    ax.plot(t, x2, '--b', label='short')
    t_stl = np.arange(len(x3))
    ax.plot(t_stl, x3, '*g', label='the OG')
    ax.legend()
    ax.set_title('x vs t')
    plt.show()

def simple_vis(t,x, wstl_x):
    # fig, ax = plt.subplots()
    # ax.grid()
    # ax.plot(t, x, '-g', label='the OG')
    # ax.legend()
    # ax.set_title('x vs t')
    # plt.show()
    x_upper = [7 for i in range(len(t))]
    x_lower = [1 for i in range(len(t))]
    plt.plot(t,x, '-k', label='x_ref')
    plt.plot(t,x_upper, '--g',  label='x_upper')
    plt.plot(t,x_lower, '--b',  label='x_lower')
    plt.plot(t,wstl_x, '-c', label='x_wstl')
    plt.legend()
    plt.show()

def get_weights(T,t):
    w = 1-(t/T)
    return [w, 1-w]

def reference_func(T): 
    t = np.arange(T)
    step1 = int(np.floor(T/3))
    x = []
    print(step1)
    x[0:step1] = [2 for i in range(step1)]
    step2 = int(np.floor(2*T/3))
    x[step1+1:step2] = [4 for i in range(step1,step2)]
    x[step2+1:T] = [6 for i in range(step2,T)]
    return t,x


if __name__ == '__main__':
    T = 20
    t = 5
    sol = []
    for t in range(0,T):
        # weight2 = get_weights(T,t)
        w1 = t/T
        print("weights:", 5/20)

        wstl_formula = " &&^weight2 ((x<= 7), (x>=4))"
        weights = {'weight1': lambda x: 0.5, 'weight2': lambda k: [t/T, 1-(t/T)][k], 'weight3': lambda x: 5}
        # weights = {'weight1': lambda x: 0.5, 'weight2': lambda k: [0.5, 0.5][k], 'weight3': lambda x: 5}

        # Translate WSTL to MILP and retrieve integer variable for the formula
        # x1=wstl_solve(wstl_formula, weights, type='long')
        wstl_milp = wstl_solve(wstl_formula, weights, type='short')
        y = [var.X for var in wstl_milp.variables['x'].values()]
        sol.append(y)

    steps,x_ref = reference_func(T)
    simple_vis(steps,x_ref,sol)
    # x3 = stl_solve(stl_formula)
    # print("long", x1)
    # print("short:", x
    # print("stl:", x3)
    # visualize(end_time, x1,x2,x3)
    print("sol:",sol)
    # for var in wstl_milp.model.getVars():
    #     print(var.VarName, ':', var.x)
    #
    # print('Constraints')
    # for constr in wstl_milp.model.getConstrs():
    #     print(':', str(constr))
    #
    # print('Objective')
    # obj = wstl_milp.model.getObjective()
    # print(str(obj), ':', obj.getValue())

# Parse the WSTL formula string
# lexer = wstlLexer(InputStream("<>[1, 3]^weight1 (y <= 2)"))
# lexer = wstlLexer(InputStream("[][1, 3]^weight1 (y <= 2)"))
# lexer = wstlLexer(InputStream("(y > 1) U[1, 3]^weight1 (y <= 2)"))
# lexer = wstlLexer(InputStream("(y > 1) &^weight1 (y <= 2)"))
# lexer = wstlLexer(InputStream("(y > 1) &^weight1 (y <= 2) &^weight2 (y > 3)"))
# lexer = wstlLexer(InputStream("(y > 1) |^weight1 (y <= 2) |^weight2 (y > 3)"))
# lexer = wstlLexer(InputStream("(y > 1) |^weight1 (y <= 2)"))
# lexer = wstlLexer(InputStream("(y > 1) &^weight1 (y <= 2) |^weight2 (y > 3)"))
# lexer = wstlLexer(InputStream("&&^weight1 (F[2, 5] (y <= 2), y > 3, x < 0.2)"))
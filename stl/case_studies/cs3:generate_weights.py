from __future__ import division
from antlr4 import InputStream, CommonTokenStream
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, spline
import sys
from scipy.interpolate import make_interp_spline
import scipy
sys.path.append('../')
import random
from stl import Operation, RelOperation, STLFormula
from wstlLexer import wstlLexer
from wstlParser import wstlParser
from wstlVisitor import wstlVisitor
import math
from wstl import WSTLAbstractSyntaxTreeExtractor
from stl import STLAbstractSyntaxTreeExtractor
# from long_wstl2milp import long_wstl2milp
from short_wstl2milp import short_wstl2milp
from pswstl2milp import pswstl2milp
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
        wstl_milp = pswstl2milp(ast)
    else:
        raise NotImplementedError
    rho_formula = wstl_milp.translate()
    wstl_milp.model.update()

    print(rho_formula, 'AQUI')
    wstl_milp.model.setObjective(rho_formula, GRB.MAXIMIZE)
    wstl_milp.model.update()
    if type == 'long':
        wstl_milp.model.write('long_milp.lp')
    else:
        wstl_milp.model.write('short_milp.lp')

    # Solve problem
    wstl_milp.model.optimize()
    y = [var.X for var in wstl_milp.variables['x'].values()]
    return wstl_milp


def stl_solve(stl_formula, varname='x', end_time=15):
    lexer = stlLexer(InputStream(stl_formula))
    tokens = CommonTokenStream(lexer)
    parser = stlParser(tokens)
    t = parser.stlProperty()
    print(t.toStringTree())
    ast = STLAbstractSyntaxTreeExtractor().visit(t)

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

    return y


def simple_vis(t,x, wstl_x, y1, y2):

    plt.plot(t,x, '-sk', label='x_ref')
    plt.plot(t,wstl_x, '--sb', label='x_wstl')
    plt.plot(t,y1, '--g', label='A')
    plt.plot(t,y2, '--c', label='B')
    plt.legend()
    plt.grid()
    plt.grid(color='lightgrey')
    plt.show()

def get_weights(T,t):
    w = 1-(t/T)
    return [w, 1-w]

def reference_func(T, deg):
    t = np.arange(T)
    x = []
    ## crazy curve
    x[0:T] = [ 0.1 * np.tan(t[i]) +  0.01 * (t[i]/T) * ( 3 * np.sin(math.sqrt((t[i])**1.5/T))) + 3 * np.exp(-0.5*t[i]) + 6 for i in range(T)]
    poly1 = np.poly1d(np.polyfit(t,x,deg))
    x = poly1(t)
    return t,x


if __name__ == '__main__':
    T = 15
    sol1 = []
    # sol2 = []
    degree = 5
    # create DataFrame
    df = pd.DataFrame({'x_t': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                       'y1': [3, 3, 3, 3, 3, 3, 9, 9, 9, 9, 9, 8, 8, 8, 8],
                       'y2': [12, 12, 12, 12, 10, 10, 10, 2, 2, 2, 2, 2, 2, 12, 12], })
    steps,x_ref = reference_func(T,degree)
    increments = np.arange(0,T)

    for t in range(0,T):

        if t <= 5:
            wstl_formula = " /F[0,5]^weight1 (&^weight2 ((x<= 12), (x>=3)))"
        elif (t > 5 & t <= 10):
            wstl_formula = " /F[6,10]^weight1 (&^weight2 ((x<= 9), (x>=2)))"
        else:
            wstl_formula = " /F[10,15]^weight1 (&^weight2 ((x<= 12), (x>=2)))"

        gamma = (x_ref[t] - df.y2[t]) / (df.y2[t] - df.y1[t])
        weights = {'weight1': lambda x: 0.9,
               'weight2': lambda k: [(gamma), (1 - gamma)][k],
               'weight3': lambda x: 5}
    #
    #     # Translate WSTL to MILP and retrieve integer variable for the formula
    #     # x1=wstl_solve(wstl_formula, weights, type='long')
        wstl_milp = wstl_solve(wstl_formula, weights, type='short')
        x = [var.X for var in wstl_milp.variables['x'].values()]
        sol1.append(x[0])

    poly1 = np.poly1d(np.polyfit(increments,sol1,degree))
    wstl_x = poly1(increments)

    simple_vis(steps,x_ref,wstl_x, df.y1, df.y2)

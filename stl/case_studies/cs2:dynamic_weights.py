from __future__ import division
from antlr4 import InputStream, CommonTokenStream
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

    wstl_milp.model.update()
    wstl_milp.model.setObjective(rho_formula, GRB.MAXIMIZE)
    wstl_milp.model.update()
    # if type == 'long':
    #     wstl_milp.model.write('long_milp.lp')
    # else:
    #     wstl_milp.model.write('short_milp.lp')

    # Solve problem
    wstl_milp.model.optimize()
    y = [var.X for var in wstl_milp.variables['x'].values()]
    return y


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
    return y

def simple_vis(t,x, wstl_x, stl_x):

    x_upper = [8 for i in range(len(t))]
    x_lower = [1 for i in range(len(t))]
    plt.plot(t,x, '-sk', label='x_ref')
    plt.plot(t,x_upper, '--g')
    plt.plot(t,x_lower, '--c')
    plt.plot(t,wstl_x, '--sb', label='wstl')
    plt.plot(t,stl_x, '-sr', label='stl')
    plt.legend()
    plt.grid(color='lightgrey')
    plt.show()

def get_weights(T,t):
    w = 1-(t/T)
    return [w, 1-w]

def reference_func(T): 
    t = np.arange(T)
    x = []

    ## A simple monotonically increasing curve
    step1 = int(np.floor(T/4))
    x[0:step1] = [1.2 + 0.1 * random.random() for i in range(step1)]
    step2 = int(np.floor(T/3))
    x[step1+1:step2] = [3 + np.sin(math.sqrt(t[i])) for i in range(step1,step2)]
    step3 = int(np.floor(2*T/3))
    increments = np.linspace(0,1,step3-step2)
    x[step2+1:step3] = [5 + increments[i] for i in range(step3-step2)]
    x[step3+1:T] = [7 + 0.2* np.cos((t[i]/2))**2 for i in range(T-step3)]
    poly1 = np.poly1d(np.polyfit(t,x,4))
    x = poly1(t)


    return t,x


if __name__ == '__main__':
    T = 20
    sol1 = []

    ## Cannot use G[a, b] since the weights are time-varying
    for t in range(0,T):

        wstl_formula = " &&^weight2 ((x<= 7), (x>=1))"
        weights = {'weight1': lambda x: 0.5, 'weight2': lambda k: [(t**1.5/T), 1-(t/T)][k], 'weight3': lambda x: 5}

        # Translate WSTL to MILP and retrieve integer variable for the formula
        wstl_x = wstl_solve(wstl_formula, weights, type='short')
        sol1.append(wstl_x[0])


    ## Equivalent STL formula
    stl_formula = "G[0,19] ((x<= 7) && (x>=1))"
    stl_x = stl_solve(stl_formula)

    ## Desired signal
    steps,x_ref = reference_func(T)

    ## Curve fitting through obtained discrete values
    increments = np.arange(0,T)
    poly1 = np.poly1d(np.polyfit(increments,sol1,4))
    wstl_x = poly1(increments)

    poly2 =  np.poly1d(np.polyfit(increments,stl_x,4))
    stl_x = poly2(increments)

    simple_vis(steps,x_ref,wstl_x, stl_x)
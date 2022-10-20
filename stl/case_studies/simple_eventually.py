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
from long_wstl2milp import long_wstl2milp
from short_wstl2milp import short_wstl2milp
from stl2milp import stl2milp
from gurobipy import *
from stlLexer import stlLexer
from stlParser import stlParser
from stlVisitor import stlVisitor
from stl import STLAbstractSyntaxTreeExtractor
from matplotlib.path import Path
from matplotlib.patches import PathPatch


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

    # print(rho_formula)
    wstl_milp.model.setObjective(rho_formula, GRB.MAXIMIZE)
    wstl_milp.model.update()
    if type == 'long':
        wstl_milp.model.write('long_milp.lp')
    else:
        wstl_milp.model.write('short_milp.lp')

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


def simple_vis(t, stl, weights, w1, w2, w3, w4, y1, y2):
    print("t:", t)
    fig, ax = plt.subplots()
    plt.plot(t, stl, '-sr', label='STL')
    # for traj in range(len(wstl_list)):
    #     plt.plot(t, wstl_list[traj], '-s', label='x_wstl_{}'.format(weights_list[traj]))

    ax.plot(t, w1, '*-', label='x_wstl_{}'.format(weights_list[0]))
    ax.plot(t, w2, '^-', label='x_wstl_{}'.format(weights_list[1]))
    ax.plot(t, w3, '+-', label='x_wstl_{}'.format(weights_list[2]))
    ax.plot(t, w4, '--sb', label='x_wstl_{}'.format(weights_list[3]))


    # ax.plot(t, y1, '--g', label='A')
    # ax.plot(t, y2, '--c', label='B')
    lvertices1 = []
    lcodes1 = []
    lvertices2 = []
    lcodes2 = []
    lvertices3 = []
    lcodes3 = []
    lcodes1 += [Path.MOVETO] + [Path.LINETO] * 3 + [Path.CLOSEPOLY]
    lvertices1 += [(0, -3), (4, -3), (4, 12), (0, 12), (0, 0)]
    lcodes2 += [Path.MOVETO] + [Path.LINETO] * 3 + [Path.CLOSEPOLY]
    lvertices2 += [(5, -3), (10, -3), (10, 12), (5, 12), (0, 0)]
    lcodes3 += [Path.MOVETO] + [Path.LINETO] * 3 + [Path.CLOSEPOLY]
    lvertices3 += [(11, -3), (15, -3), (15, 12), (11, 12), (0, 0)]
    lpath1 = Path(lvertices1, lcodes1)
    lpath2 = Path(lvertices2, lcodes2)
    lpath3 = Path(lvertices3, lcodes3)

    lpathpatch1 = PathPatch(lpath1, facecolor='skyblue', edgecolor='k', alpha=0.2)
    lpathpatch2 = PathPatch(lpath2, facecolor='plum', edgecolor='k', alpha=0.2)
    lpathpatch3 = PathPatch(lpath3, facecolor='wheat', edgecolor='k', alpha=0.2)

    ax.add_patch(lpathpatch1)
    ax.add_patch(lpathpatch2)
    ax.add_patch(lpathpatch3)

    # plt.fill_between(x,12,-3,where=(x>5) & (x<=12),color='b')
    ax.legend()
    ax.grid()
    ax.grid(color='lightgrey')
    # ax.show()
    plt.show()


def get_weights(T, t):
    w = 1 - (t / T)
    return [w, 1 - w]


def reference_func(T, deg):
    t = np.arange(T)
    x = []
    ## crazy curve
    x[0:T] = [0.1 * np.tan(t[i]) + 0.01 * (t[i] / T) * (3 * np.sin(math.sqrt((t[i]) ** 1.5 / T))) + 3 * np.exp(
        -0.5 * t[i]) + 6 for i in range(T)]
    poly1 = np.poly1d(np.polyfit(t, x, deg))
    x = poly1(t)
    return t, x


if __name__ == '__main__':
    T = 5
    solw1 = []
    solw2 = []
    solw3 = []
    solw4 = []
    sol2 = []
    degree = 3
    # create DataFrame
    df = pd.DataFrame({'x_t': [1, 2, 3, 4, 5],
                       'y1': [3, 3, 9, 9, 8],
                       'y2': [12, 12, 10, 2, 2], })
    steps, x_ref = reference_func(T, degree)
    increments = np.arange(0, T)
    w_try1 = [.1, .2, .3, .4, .5]
    w_try2 = [.9, .9, .8, .1, .1]
    w_try3 = [.5, .5, .5, .5, .5]
    w_try4 = [.1, .1, .5, .9, .9]
    # for t in range(0, T):

        # if t <= 5:
    wstl_formula = " &&^weight3 (F[0,4]^weight1 (x>=4), F[0,4]^weight2 (x<=3))"
    stl_formula = "F[0,4]((x>=4) && (x<=3))"
    weights_list = [w_try1, w_try2, w_try3, w_try4]
    for num, item in enumerate(weights_list):
        # if df.y1[t] >= df.y2[t]:
        weights = {'weight1': lambda x: item[x],
                       'weight2': lambda x: 1-item[x],
                       'weight3': lambda x: 1}
        wstl_milp = wstl_solve(wstl_formula, weights, type='short')
        # x = [var.X for var in wstl_milp.variables['x'].values()]
        if num == 0:
            print("weight:", item)
            solw1 = wstl_milp
        elif num == 1:
            solw2= wstl_milp
        elif num == 2:
            solw3 = wstl_milp
        else:
            solw4 = wstl_milp

    # stl_formula = "G[0,5] ((x<= 12) && (x>=3)) && G[6,10] ((x<= 9) && (x>=2)) && G[11,14] ((x<= 12) && (x>=2))"
    stl_milp = stl_solve(stl_formula)

    # print("stl_traj:", stl_milp)

    # polyw1 = np.poly1d(np.polyfit(increments, solw1, degree))
    # wstl_x1 = polyw1(increments)
    #
    # polyw2 = np.poly1d(np.polyfit(increments, solw2, degree))
    # wstl_x2 = polyw2(increments)
    #
    # polyw3 = np.poly1d(np.polyfit(increments, solw3, degree))
    # wstl_x3 = polyw3(increments)
    #
    # polyw4 = np.poly1d(np.polyfit(increments, solw4, degree))
    # wstl_x4 = polyw4(increments)

    # wstl_list = [solw1, solw2, solw3, solw4]

    print("wtl:", solw1)

    # poly2 = np.poly1d(np.polyfit(increments, stl_milp, degree))
    # stl_x = poly2(increments)
    steps = np.arange(T)
    print(len(steps), len(solw1))
    simple_vis(steps, stl_milp, weights_list, solw1, solw2, solw3, solw4, df.y1, df.y2)

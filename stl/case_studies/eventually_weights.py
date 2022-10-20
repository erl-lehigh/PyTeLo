'''Interesting case : G, F'''

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


def simple_vis(t, x, weights, wstl_list, stl_x, y1, y2):
    print("t:", t)
    fig, ax = plt.subplots()
    plt.plot(t, x, '-ok', label='x_ref')
    for traj in range(len(wstl_list)):
        plt.plot(t, wstl_list[traj], '-s', label='x_wstl_{}'.format(weights_list[traj]))
    ax.plot(t, stl_x, '--*b', label='x_stl')
    ax.plot(t, y1, '--g', label='A')
    ax.plot(t, y2, '--c', label='B')
    lvertices1 = []
    lcodes1 = []
    lvertices2 = []
    lcodes2 = []
    lvertices3 = []
    lcodes3 = []
    lcodes1 += [Path.MOVETO] + [Path.LINETO] * 3 + [Path.CLOSEPOLY]
    lvertices1 += [(0, 3), (4, 3), (4, 12), (0, 12), (0, 0)]
    lcodes2 += [Path.MOVETO] + [Path.LINETO] * 3 + [Path.CLOSEPOLY]
    lvertices2 += [(5, 2), (10, 2), (10, 9), (5, 9), (0, 0)]
    lcodes3 += [Path.MOVETO] + [Path.LINETO] * 3 + [Path.CLOSEPOLY]
    lvertices3 += [(11, 2), (15, 2), (15, 12), (11, 12), (0, 0)]
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
    T = 15
    solw1 = []
    solw2 = []
    solw3 = []
    solw4 = []
    sol2 = []
    degree = 3
    # create DataFrame
    df = pd.DataFrame({'x_t': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                       'y1': [3,    3, 3, 3,  3,  3,   3, 2, 2, 2, 2, 2, 2,  5, 5],
                       'y2': [12, 12, 12, 12, 10, 10, 10, 9, 9, 9, 9, 8, 8, 12, 12], })
    steps, x_ref = reference_func(T, degree)
    increments = np.arange(0, T)
    # w_try1 = [.1, .2, .3, .4, .5, .1, .2, .3, .4, .5, .1, .2, .3, .4, .5,.1]
    w_try1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    w_try2 = [.9, .9, .8, .8, .8, .7, .1, .5, .9, .9, .1, .1, .5, .9, .9,.1]
    w_try3 = [.5, .5, .5, .5, .5, .9, .9, .5, .1, .1, .9, .9, .5, .1, .1,.1]
    w_try4 = [.9, .9, .5, .1, .1,.9, .9, .5, .1, .1,.9, .9, .5, .1, .1,.1]
    for t in range(0, T):

        # if t <= 5:
        #     wstl_formula = " F[0,4]^weight1 (&&^weight2 ((x<= 12), (x>=3)))"
        # elif (t > 5 & t <= 10):
        #     wstl_formula = " F[5,10]^weight1 (&&^weight2 ((x<= 9), (x>=2)))"
        # else:
        #     wstl_formula = " F[11,15]^weight1 (&&^weight2 ((x<= 12), (x>=2)))"

        # wstl_1 = " G[0,4]^weight1 (&&^weight2 ((x<= 12), (x>=3)))"
        #
        # wstl_2 =  " G[5,10]^weight1 (&&^weight2 ((x<= 9), (x>=2)))"
        #
        # wstl_3 =" G[11,15]^weight1 (&&^weight2 ((x<= 12), (x>=2)))"
        
        wstl_1 = " F[0,4]^weight1 (&&^weight2 ((x<= 12), (x>=3)))"

        wstl_2 =  " F[5,10]^weight1 (&&^weight2 ((x<= 9), (x>=2)))"

        wstl_3 =" F[11,15]^weight1 (&&^weight2 ((x<= 12), (x>=2)))"
        
        
        wstl_formula ='&&^weight3({},{},{})'.format(wstl_1, wstl_2, wstl_3)
        # if t <= 5:
        #     wstl_formula = "  (&&^weight2 ((x<= 12), (x>=3)))"
        # elif (t > 5 & t <= 10):
        #     wstl_formula = " (&&^weight2 ((x<= 9), (x>=2)))"
        # else:
        #     wstl_formula = " (&&^weight2 ((x<= 12), (x>=2)))"
        gamma = np.abs((x_ref[t] - df.y2[t]) / (df.y1[t] - df.y2[t]))
        # # gamma = (x_ref[t] - df.y2[t]) / (df.y1[t] - df.y2[t])
        # weights_list = [0.1, 0.3, 0.7, .9]
        weights_list = [w_try1, w_try2, w_try3, w_try4]
        for num, item in enumerate(weights_list):
            if df.y1[t] >= df.y2[t]:
                gamma = np.abs((x_ref[t] - df.y2[t]) / (df.y1[t] - df.y2[t]))

                weights = {'weight1': lambda x: item[x],
                           'weight2': lambda k: [(gamma), (1 - gamma)][k],
                           'weight3': lambda x: 1}
            else:
                gamma = np.abs((x_ref[t] - df.y1[t]) / (df.y2[t] - df.y1[t]))
                weights = {'weight1': lambda x: item[x],
                           'weight2': lambda k: [(gamma), (1 - gamma)][k],
                           'weight3': lambda x: 1}
            print("w:", gamma)

            #
            #     # Translate WSTL to MILP and retrieve integer variable for the formula
            #     # x1=wstl_solve(wstl_formula, weights, type='long')
            wstl_milp = wstl_solve(wstl_formula, weights, type='short')
            x = [var.X for var in wstl_milp.variables['x'].values()]
            print(x,'hola kamale', t)
            if num == 0:
                print("weight:", item)
                solw1.append(x[t])
            elif num == 1:
                solw2.append(x[t])
            elif num == 2:
                solw3.append(x[t])
            else:
                solw4.append(x[t])

        # for num, item in enumerate(weights_list):
        # if df.y1[t] >= df.y2[t]:
        #     gamma = np.abs((x_ref[t] - df.y2[t]) / (df.y1[t] - df.y2[t]))
        #
        #     weights = {'weight1': lambda x: 10,
        #                'weight2': lambda k: [(gamma), (1 - gamma)][k],
        #                'weight3': lambda x: 5}
        # else:
        #     gamma = np.abs((x_ref[t] - df.y1[t]) / (df.y2[t] - df.y1[t]))
        #     weights = {'weight1': lambda x: 10,
        #                'weight2': lambda k: [(1 - gamma), (gamma)][k],
        #                'weight3': lambda x: 5}
        # print("w:", gamma)

        #
        #     # Translate WSTL to MILP and retrieve integer variable for the formula
        #     # x1=wstl_solve(wstl_formula, weights, type='long')
        #     wstl_milp = wstl_solve(wstl_formula, weights, type='short')
        #     x = [var.X for var in wstl_milp.variables['x'].values()]
        #     solw1.append(x[0])

    stl_formula = "G[0,5] ((x<= 12) && (x>=3)) && G[6,10] ((x<= 9) && (x>=2)) && G[11,14] ((x<= 12) && (x>=2))"
    stl_milp = stl_solve(stl_formula)

    print("stl_traj:", stl_milp)

    # print("stl:", len(stl_milp))
    polyw1 = np.poly1d(np.polyfit(increments, solw1, degree))
    wstl_x1 = polyw1(increments)

    polyw2 = np.poly1d(np.polyfit(increments, solw2, degree))
    wstl_x2 = polyw2(increments)

    polyw3 = np.poly1d(np.polyfit(increments, solw3, degree))
    wstl_x3 = polyw3(increments)

    polyw4 = np.poly1d(np.polyfit(increments, solw4, degree))
    wstl_x4 = polyw4(increments)

    wstl_list = [wstl_x1, wstl_x2, wstl_x3, wstl_x4]
    # wstl_list = [wstl_x1]
    # wstl_list = [solw1, solw2, solw3, solw4]

    print("wtl:", wstl_list)

    poly2 = np.poly1d(np.polyfit(increments, stl_milp, degree))
    stl_x = poly2(increments)
    simple_vis(steps, x_ref, weights_list, wstl_list, stl_x, df.y1, df.y2)

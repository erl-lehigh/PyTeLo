#!/usr/bin/env python3

"""
 Copyright (C) 2015-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
 @author: Gustavo Cardona, Cristian-Ioan Vasile
"""
from pstl2milp import pstl2milp
from stl import STLAbstractSyntaxTreeExtractor
from stlVisitor import stlVisitor
from stlParser import stlParser
from stlLexer import stlLexer
from stl import Operation, RelOperation, STLFormula
import matplotlib.pyplot as plt
import gurobipy as grb
from gurobipy import GRB
from gurobipy import Model as GRBModel
from antlr4 import InputStream, CommonTokenStream

import sys
sys.path.append('..')


# from stl2milp import stl2milp


def pstl_mpc(x_init, y_init, x_init2, y_init2, x_init3, y_init3,
             x_init4, y_init4, x_init5, y_init5, x_init6, y_init6,
            current_step, period, ast, ranges):

    # Define the general range for x y z

    stl_milp = pstl2milp(ast, ranges=ranges, robust=True)
    stl_milp.M = 20
    
    # system variables and the time period
    # Define the matrixes that used for linear system
    A = [[1, 0], [0, 1]]
    B = [[1, 0], [0, 1]]

    x = dict()
    x2 = dict()
    y = dict()
    y2 = dict()
    x3 = dict()
    x4 = dict()
    y3 = dict()
    y4 = dict()
    x5 = dict()
    x6 = dict()
    y5 = dict()
    y6 = dict()

    u = dict()
    u2 = dict()
    v = dict()
    v2 = dict()
    u3 = dict()
    u4 = dict()
    v3 = dict()
    v4 = dict()
    u5 = dict()
    u6 = dict()
    v5 = dict()
    v6 = dict()

    if current_step < period - 1:
        backward_steps = current_step
    else:
        backward_steps = period - 1

    for k in range(period + backward_steps):
        name = "x_{}".format(k)
        x[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        name = "x2_{}".format(k)
        x2[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        name = "y_{}".format(k)
        y[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        name = "y2_{}".format(k)
        y2[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        name = "u_{}".format(k)
        u[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-1, ub=1, name=name)
        name = "v_{}".format(k)
        v[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-1, ub=1, name=name)
        name = "u2_{}".format(k)
        u2[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-1, ub=1, name=name)
        name = "v2_{}".format(k)
        v2[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-1, ub=1, name=name)
        name = "x3_{}".format(k)
        x3[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        name = "x4_{}".format(k)
        x4[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        name = "y3_{}".format(k)
        y3[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        name = "y4_{}".format(k)
        y4[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        name = "u3_{}".format(k)
        u3[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-1, ub=1, name=name)
        name = "v3_{}".format(k)
        v3[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-1, ub=1, name=name)
        name = "u4_{}".format(k)
        u4[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-1, ub=1, name=name)
        name = "v4_{}".format(k)
        v4[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-1, ub=1, name=name)
        name = "x5_{}".format(k)
        x5[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        name = "x6_{}".format(k)
        x6[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        name = "y5_{}".format(k)
        y5[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        name = "y6_{}".format(k)
        y6[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        name = "u5_{}".format(k)
        u5[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-1, ub=1, name=name)
        name = "v5_{}".format(k)
        v5[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-1, ub=1, name=name)
        name = "u6_{}".format(k)
        u6[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-1, ub=1, name=name)
        name = "v6_{}".format(k)
        v6[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-1, ub=1, name=name)

    # use system variables in STL spec encoding
    stl_milp.variables['x'] = x
    stl_milp.variables['y'] = y
    stl_milp.variables['u'] = u
    stl_milp.variables['v'] = v
    stl_milp.variables['x2'] = x2
    stl_milp.variables['y2'] = y2
    stl_milp.variables['u2'] = u2
    stl_milp.variables['v2'] = v2
    stl_milp.variables['x3'] = x3
    stl_milp.variables['y3'] = y3
    stl_milp.variables['u3'] = u3
    stl_milp.variables['v3'] = v3
    stl_milp.variables['x4'] = x4
    stl_milp.variables['y4'] = y4
    stl_milp.variables['u4'] = u4
    stl_milp.variables['v4'] = v4
    stl_milp.variables['x5'] = x5
    stl_milp.variables['y5'] = y5
    stl_milp.variables['u5'] = u5
    stl_milp.variables['v5'] = v5
    stl_milp.variables['x6'] = x6
    stl_milp.variables['y6'] = y6
    stl_milp.variables['u6'] = u6
    stl_milp.variables['v6'] = v6
    
    
    

    # define the inital states for each mpc step
    for i in range(backward_steps + 1):
        stl_milp.model.addConstr(x[i] == x_init[current_step - backward_steps + i])
        stl_milp.model.addConstr(y[i] == y_init[current_step - backward_steps + i])
        stl_milp.model.addConstr(x2[i] == x_init2[current_step - backward_steps + i])
        stl_milp.model.addConstr(y2[i] == y_init2[current_step - backward_steps + i])
        stl_milp.model.addConstr(x3[i] == x_init3[current_step - backward_steps + i])
        stl_milp.model.addConstr(y3[i] == y_init3[current_step - backward_steps + i])
        stl_milp.model.addConstr(x4[i] == x_init4[current_step - backward_steps + i])
        stl_milp.model.addConstr(y4[i] == y_init4[current_step - backward_steps + i])
        stl_milp.model.addConstr(x5[i] == x_init5[current_step - backward_steps + i])
        stl_milp.model.addConstr(y5[i] == y_init5[current_step - backward_steps + i])
        stl_milp.model.addConstr(x6[i] == x_init6[current_step - backward_steps + i])
        stl_milp.model.addConstr(y6[i] == y_init6[current_step - backward_steps + i])


    # system constraints
    for k in range(backward_steps, period + backward_steps - 1):
        stl_milp.model.addConstr(x[k+1] == A[0][0] * x[k] + A[0][1] * y[k] + B[0][0] * u[k] + B[0][1] * v[k])
        stl_milp.model.addConstr(y[k+1] == A[1][0] * x[k] + A[1][1] * y[k] + B[1][0] * u[k] + B[1][1] * v[k])
        stl_milp.model.addConstr(x2[k+1] == A[0][0] * x2[k] + A[0][1] * y2[k] + B[0][0] * u2[k] + B[0][1] * v2[k])
        stl_milp.model.addConstr(y2[k+1] == A[1][0] * x2[k] + A[1][1] * y2[k] + B[1][0] * u2[k] + B[1][1] * v2[k])
        stl_milp.model.addConstr(x3[k+1] == A[0][0] * x3[k] + A[0][1] * y3[k] + B[0][0] * u3[k] + B[0][1] * v3[k])
        stl_milp.model.addConstr(y3[k+1] == A[1][0] * x3[k] + A[1][1] * y3[k] + B[1][0] * u3[k] + B[1][1] * v3[k])
        stl_milp.model.addConstr(x4[k+1] == A[0][0] * x4[k] + A[0][1] * y4[k] + B[0][0] * u4[k] + B[0][1] * v4[k])
        stl_milp.model.addConstr(y4[k+1] == A[1][0] * x4[k] + A[1][1] * y4[k] + B[1][0] * u4[k] + B[1][1] * v4[k])
        stl_milp.model.addConstr(x5[k+1] == A[0][0] * x5[k] + A[0][1] * y5[k] + B[0][0] * u5[k] + B[0][1] * v5[k])
        stl_milp.model.addConstr(y5[k+1] == A[1][0] * x5[k] + A[1][1] * y5[k] + B[1][0] * u5[k] + B[1][1] * v5[k])
        stl_milp.model.addConstr(x6[k+1] == A[0][0] * x6[k] + A[0][1] * y6[k] + B[0][0] * u6[k] + B[0][1] * v6[k])
        stl_milp.model.addConstr(y6[k+1] == A[1][0] * x6[k] + A[1][1] * y6[k] + B[1][0] * u6[k] + B[1][1] * v6[k])

    # add the specification (STL) constraints
    z = stl_milp.translate()
    # stl_milp.method_1()
    stl_milp.method_2()
    # stl_milp.method_3(z)


    pstlrobust = stl_milp.pstl2lp(ast)
    x_rhovals = [rvar.x for rvar in pstlrobust.getVars()]
    print("HERE CHECk HERE:", len(x_rhovals))


    
    # print("HERE PRINTING:", str(pstlrobust))
    print('Objective')
    obj = stl_milp.model.getObjective()
    print(str(obj), obj.getValue(), "MILP")
    # obj = [stl_milp.model.getObjective(objectives) for objectives in range(3)]
    # print(str(obj), ':', [obj[i].getValue() for i in range(3)], "MILP")

    x_vals = [var.x for var in stl_milp.variables['x'].values()]
    y_vals = [var.x for var in stl_milp.variables['y'].values()]
    x_vals2 = [var.x for var in stl_milp.variables['x2'].values()]
    y_vals2 = [var.x for var in stl_milp.variables['y2'].values()]
    x_vals3 = [var.x for var in stl_milp.variables['x3'].values()]
    y_vals3 = [var.x for var in stl_milp.variables['y3'].values()]
    x_vals4 = [var.x for var in stl_milp.variables['x4'].values()]
    y_vals4 = [var.x for var in stl_milp.variables['y4'].values()]
    x_vals5 = [var.x for var in stl_milp.variables['x5'].values()]
    y_vals5 = [var.x for var in stl_milp.variables['y5'].values()]
    x_vals6 = [var.x for var in stl_milp.variables['x6'].values()]
    y_vals6 = [var.x for var in stl_milp.variables['y6'].values()]

    x_init[current_step + 1] = x_vals[backward_steps + 1]
    y_init[current_step + 1] = y_vals[backward_steps + 1]
    x_init2[current_step + 1] = x_vals2[backward_steps + 1]
    y_init2[current_step + 1] = y_vals2[backward_steps + 1]
    x_init3[current_step + 1] = x_vals3[backward_steps + 1]
    y_init3[current_step + 1] = y_vals3[backward_steps + 1]
    x_init4[current_step + 1] = x_vals4[backward_steps + 1]
    y_init4[current_step + 1] = y_vals4[backward_steps + 1]
    x_init5[current_step + 1] = x_vals5[backward_steps + 1]
    y_init5[current_step + 1] = y_vals5[backward_steps + 1]
    x_init6[current_step + 1] = x_vals6[backward_steps + 1]
    y_init6[current_step + 1] = y_vals6[backward_steps + 1]
    
    return x_vals, y_vals, x_vals2, y_vals2, x_vals3, y_vals3, x_vals4, y_vals4, x_vals5, y_vals5, x_vals6, y_vals6, x_rhovals


def main():

    # formula = '(G[2,4] (x <= 1)) && (G[8,10] (x >= 1)) && (G[14, 18] (x <= 2)) && (G[23, 28] (x >= 2)) '
    # formula = "G[2,8] (x>=3) && G[15,24] (x<=2)"
    # formula = "G[5,30] ((x>=2) && (y>=2))"
    # formula = "(G[10,20] (x>=2)) && (G[24,28](x<=-1)) && (G[5,8](x>=4))"
    # formula = "(G[10,25] (x>=3)) && (G[15,20](x<=-1))"
    # formula = "(G[10,15] (x>=4)) && (G[5,20](x<=2))"
    # formula = "(G[10,12](x>=1))"
    formula = "(G[10,24] (x>=3)) && (G[13,15](x<=2))"
    # formula = "(G[8,12] (x>=2.1)) && (G[8,12](x<=2))"
    ranges = {'x': [-4, 5], 'y': [-4, 5], 'x2': [-4, 5], 'y2': [-4, 5]}

    # Stl2milp Initialization
    lexer = stlLexer(InputStream(formula))
    tokens = CommonTokenStream(lexer)
    parser = stlParser(tokens)
    t = parser.stlProperty()
    print(t.toStringTree())
    ast = STLAbstractSyntaxTreeExtractor().visit(t)

    print(set(ast.variables()))
    print(set(ranges))
    print('AST:', str(ast))
    number_robots = len(ast.variables())
    print('number of robots:', number_robots)

    # Based on the formula, you need to define the period and the steps for it.
    # Normally, period should bigger than the formula range and steps should be bigger than period
    steps = 30
    period = 30
    x_init, y_init, x_init2, y_init2, x_init3, y_init3 = 1, 1, 1, 3, 1, 0
    x_init4, y_init4, x_init5, y_init5, x_init6, y_init6 = 2, 4, 1, 3, 1, 0

    x = [0 if i != 0 else x_init for i in range(steps + period)]
    y = [0 if i != 0 else y_init for i in range(steps + period)]
    x2 = [0 if i != 0 else x_init2 for i in range(steps + period)]
    y2 = [0 if i != 0 else y_init2 for i in range(steps + period)]
    x3 = [0 if i != 0 else x_init3 for i in range(steps + period)]
    y3 = [0 if i != 0 else y_init3 for i in range(steps + period)]
    x4 = [0 if i != 0 else x_init4 for i in range(steps + period)]
    y4 = [0 if i != 0 else y_init4 for i in range(steps + period)]
    x5 = [0 if i != 0 else x_init5 for i in range(steps + period)]
    y5 = [0 if i != 0 else y_init5 for i in range(steps + period)]
    x6 = [0 if i != 0 else x_init6 for i in range(steps + period)]
    y6 = [0 if i != 0 else y_init6 for i in range(steps + period)]

    t = [i for i in range(steps + period)]

    x_v = []
    y_v = []
    x_v2 = []
    y_v2 = []
    x_v3 = []
    y_v3 = []
    x_v4 = []
    y_v4 = []
    x_v5 = []
    y_v5 = []
    x_v6 = []
    y_v6 = []

    for i in range(0, steps):
        x_v, y_v, x_v2, y_v2, x_v3, y_v3, x_v4, y_v4, x_v5, y_v5, x_v6, y_v6, x_rho = pstl_mpc(
                                x, y, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, i, period, ast, ranges)

    # print(type(x_rho), len(x_rho), "rho: ", str(x_rho))
    fig, axs = plt.subplots(3)
    fig.suptitle('subplots')
    axs[0].plot(t[0:period], x_v[0:period])
    axs[0].grid()
    axs[0].set_title('x vs t')
    axs[1].plot(t[0:period], x_v[0:period])
    axs[1].grid()
    axs[1].set_title('x vs t')
    axs[2].plot(t[0:period], x_v[0:period])
    axs[2].grid()
    axs[2].set_title('x vs t')
    fig.tight_layout()
    plt.plot(t[10:26], x_rho)
    plt.show()
if __name__ == '__main__':
    main()

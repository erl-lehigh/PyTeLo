#!/usr/bin/env python3

"""
 Copyright (C) 2015-2020 Cristian Ioan Vasile <cvasile@lehigh.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
"""
from antlr4 import InputStream, CommonTokenStream

import sys
sys.path.append('../')

import gurobipy as grb

import matplotlib.pyplot as plt

from stl import Operation, RelOperation, STLFormula
from stlLexer import stlLexer
from stlParser import stlParser
from stlVisitor import stlVisitor

from stl import STLAbstractSyntaxTreeExtractor

from stl2milp import stl2milp

def stl_milp_solver(ast, x_init, y_init, z_init, current_step, period, M, B):
    # Define the general range for x y z 
    stl_milp = stl2milp(ast, ranges={'x': [-4, 5], 'y': [-4, 5], 'z': [-4, 5]}, robust=True)
    stl_milp.M = 20

    x = dict()
    y = dict()
    z = dict()
    u = dict()
    v = dict()
    w = dict()

    if current_step < period - 1: 
        backward_steps = current_step
    else:
        backward_steps = period - 1

    for k in range(period + backward_steps):
        name = "x_{}".format(k) 
        x[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        name = "y_{}".format(k)
        y[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        name = "z_{}".format(k) 
        z[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
        name = "u_{}".format(k)
        u[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-1, ub=1, name=name)
        name = "v_{}".format(k)
        v[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-1, ub=1, name=name)
        name = "w_{}".format(k)
        w[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-1, ub=1, name=name)

    # use system variables in STL spec encoding
    stl_milp.variables['x'] = x
    stl_milp.variables['y'] = y
    stl_milp.variables['z'] = z
    stl_milp.variables['u'] = u
    stl_milp.variables['v'] = v
    stl_milp.variables['w'] = w

    # define the inital states for each mpc step 
    for i in range(backward_steps + 1):
        stl_milp.model.addConstr(x[i] == x_init[current_step - backward_steps + i])
        stl_milp.model.addConstr(y[i] == y_init[current_step - backward_steps + i])
        stl_milp.model.addConstr(z[i] == z_init[current_step - backward_steps + i])

    # system constraints
    for k in range(backward_steps, period + backward_steps - 1):
        stl_milp.model.addConstr(x[k+1] == M[0][0] * x[k] + M[0][1] * y[k] + M[0][2] * z[k] + \
            B[0][0] * u[k] + B[0][1] * v[k] + B[0][2] * w[k])
        stl_milp.model.addConstr(y[k+1] == M[1][0] * x[k] + M[1][1] * y[k] + M[1][2] * z[k] + \
            B[1][0] * u[k] + B[1][1] * v[k] + B[1][2] * w[k])
        stl_milp.model.addConstr(z[k+1] == M[2][0] * x[k] + M[2][1] * y[k] + M[2][2] * z[k] + \
            B[2][0] * u[k] + B[2][1] * v[k] + B[2][2] * w[k])

    # add the specification (STL) constraints
    stl_milp.translate(satisfaction=True)

    # Solve the problem with gurobi 
    stl_milp.model.optimize()
    stl_milp.model.write('model_test.lp')


    x_vals = [var.x for var in stl_milp.variables['x'].values()]
    y_vals = [var.x for var in stl_milp.variables['y'].values()]
    z_vals = [var.x for var in stl_milp.variables['z'].values()]
    x_init[current_step + 1] = x_vals[backward_steps + 1]
    y_init[current_step + 1] = y_vals[backward_steps + 1] 
    z_init[current_step + 1] = z_vals[backward_steps + 1]

def main():
    # Define the formula that you want to apply 
    formula = "G[5,20] ((x>=2) && (y>=2) && (z<=1))"
    # Define the matrixes that used for linear system 
    M = [[1, 0, 0], [0, 1, 0],[0, 0, 1]] 
    B = [[1, 0, 0], [0, 1, 0],[0, 0, 1]] 

    # Stl2milp Initialization
    lexer = stlLexer(InputStream(formula))
    tokens = CommonTokenStream(lexer)
    parser = stlParser(tokens)
    t = parser.stlProperty()
    print(t.toStringTree())
    ast = STLAbstractSyntaxTreeExtractor().visit(t)

    print('AST:', str(ast))
    # Based on the formula, you need to define the period and the steps for it. 
    # Normally, period should bigger than the formula range and steps should be bigger than period 
    steps = 40
    period = 30 
    x_init, y_init, z_init = 0, 0, 0
    x = [0 if i != 0 else x_init for i in range(steps + period)]
    y = [0 if i != 0 else y_init for i in range(steps + period)]
    z = [0 if i != 0 else z_init for i in range(steps + period)]
    t = [i for i in range(steps + period)]

    for i in range(0, steps):
        stl_milp_solver(ast, x, y, z, i, period, M, B)

    fig, axs = plt.subplots(3)
    fig.suptitle('subplots')
    axs[0].plot(t[0:25], x[0:25])
    axs[0].set_title('x vs t')
    axs[1].plot(t[0:25], y[0:25])
    axs[1].set_title('y vs t')
    axs[2].plot(t[0:25], z[0:25])
    axs[2].set_title('z vs t')
    fig.tight_layout()
    plt.show()

if __name__ =='__main__':
    main()
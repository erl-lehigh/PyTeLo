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
from random import randint

import sys
sys.path.append('..')


# from stl2milp import stl2milp


def pstl_mpc(x_init, y_init, current_step, period, ast, ranges, num_rob):

    # Define the general range for x y z

    stl_milp = pstl2milp(ast, ranges=ranges, robust=True)
    stl_milp.M = 20
    
    # system variables and the time period
    # Define the matrixes that used for linear system
    A = [[1, 0], [0, 1]]
    B = [[1, 0], [0, 1]]

    x = []
    y = []
    u = []
    v = []
    for i in range(num_rob):

        x.append([])
        y.append([])
        u.append([])
        v.append([])

        x[i] = dict()
        y[i] = dict()
        u[i] = dict()
        v[i] = dict()


    if current_step < period - 1:
        backward_steps = current_step
    else:
        backward_steps = period - 1

    for j in range(num_rob):
        for k in range(period + backward_steps):
            name = "x{}_{}".format(j, k)
            x[j][k] = stl_milp.model.addVar(
                vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
            name = "y{}_{}".format(j, k)
            y[j][k] = stl_milp.model.addVar(
                vtype=grb.GRB.CONTINUOUS, lb=-4, ub=5, name=name)
            name = "u{}_{}".format(j, k)
            u[j][k] = stl_milp.model.addVar(
                vtype=grb.GRB.CONTINUOUS, lb=-3, ub=3, name=name)
            name = "v{}_{}".format(j, k)
            v[j][k] = stl_milp.model.addVar(
                vtype=grb.GRB.CONTINUOUS, lb=-3, ub=3, name=name)

    # use system variables in STL spec encoding
    for i in range(num_rob):
        stl_milp.variables['x{}'.format(i)] = x[i]
        stl_milp.variables['y{}'.format(i)] = y[i]
        stl_milp.variables['u{}'.format(i)] = u[i]
        stl_milp.variables['v{}'.format(i)] = v[i]

    # define the inital states for each mpc step
    for j in range (num_rob):
        for i in range(backward_steps + 1):
            stl_milp.model.addConstr(
                x[j][i] == x_init[j][current_step - backward_steps + i])
            stl_milp.model.addConstr(
                y[j][i] == y_init[j][current_step - backward_steps + i])


    # system constraints
    for j in range(num_rob):
            
        for k in range(backward_steps, period + backward_steps - 1):
            stl_milp.model.addConstr(
                x[j][k+1] == A[0][0] * x[j][k] + A[0][1] * y[j][k] + B[0][0] * u[j][k] + B[0][1] * v[j][k])
            stl_milp.model.addConstr(
                y[j][k+1] == A[1][0] * x[j][k] + A[1][1] * y[j][k] + B[1][0] * u[j][k] + B[1][1] * v[j][k])
           

    # add the specification (STL) constraints
    z = stl_milp.translate()

    # Solve the problem with gurobi
    stl_milp.model.setObjective(z, GRB.MAXIMIZE)
    stl_milp.model.update()
    stl_milp.model.optimize()
    stl_milp.model.write('model_test.lp')

    pstlrobust = [stl_milp.pstl2lp(ast, t) for t in range(1)]
    print('Objective')
    obj = stl_milp.model.getObjective()
    print(str(obj), ':', obj.getValue(), "MILP")
    x_vals = []
    y_vals = []
    for j in range(num_rob):
        x_vals.append([])
        y_vals.append([])
        x_vals[j] = [var.x for var in stl_milp.variables['x{}'.format(j)].values()]
        y_vals[j] = [var.x for var in stl_milp.variables['y{}'.format(j)].values()]
    
    for j in range(num_rob):
        x_init[j][current_step + 1] = x_vals[j][backward_steps + 1]
        y_init[j][current_step + 1] = y_vals[j][backward_steps + 1]


    return x_vals, y_vals

def main():

    # formula = 'G[2,4] (x <= 1) && G[0,10] (y >= 4) && G[10, 18] (x <= 2) || G[10, 18] (x >= 10) '
    # formula = "G[2,8] (x>=3) && G[2,10] (y>=2)| G[4, 8] (x>=1)"
    formula = "G[2,10] (x>=2) && G[2,10] (y>=2) && G[2, 6] (y2<=1) && G[2,10] (x2>=2)"
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
    steps = 30
    period = 30
    x_init = []
    y_init = []
    x = []
    y = []
    x_v = []
    y_v = []
    for i in range(number_robots):
        x_init.append(randint(-8, 8))
        y_init.append(randint(-8, 8))
        x.append([])
        y.append([])
   
 
    for j in range(number_robots):
        x[j].append([0 if i != 0 else x_init[0] for i in range(steps + period)])
        y[j].append([0 if i != 0 else y_init[0] for i in range(steps + period)])
        x_v.append([])
        y_v.append([])
    t = [i for i in range(steps + period)]

    for i in range(number_robots):
        for j in range(0, steps):
            x_v[i], y_v[i] = pstl_mpc(x, y, j, period, ast, ranges, number_robots)
    

    fig, axs = plt.subplots(3)
    fig.suptitle('subplots')
    axs[0].plot(x[0:period], y[0:period])
    axs[0].grid()
    axs[0].set_title('x vs t')
    axs[1].plot(x2[0:period], y2[0:period])
    axs[1].grid()
    axs[1].set_title('y vs t')
    axs[2].plot(t[0:period], x_v[0:period])
    axs[2].grid()
    axs[2].set_title('x2 vs t')
    fig.tight_layout()

    plt.show()
if __name__ == '__main__':
    main()
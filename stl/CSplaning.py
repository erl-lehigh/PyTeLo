

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
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import gurobipy as grb
from gurobipy import GRB
from gurobipy import Model as GRBModel
from antlr4 import InputStream, CommonTokenStream
from environment import environment
import sys
import numpy as np
import time
sys.path.append('..')

from stl2milp import stl2milp

def pstl_mpc(x_init, y_init, current_step, period, ast, ranges, method):
    # Define the general range for x y z
    stl_milp = pstl2milp(ast, ranges=ranges, robust=True)
    stl_milp.M = 20

    A = [[1, 0], [0, 1]]
    B = [[1, 0], [0, 1]]

    x = dict()
    y = dict()
    u = dict()
    v = dict()

    if current_step < period - 1:
        backward_steps = current_step
    else:
        backward_steps = period - 1

    saturation = 2.4 #2.4 , 2.3, 2

    for k in range(period + backward_steps):
        name = "x_{}".format(k)
        x[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-9.5, ub=9.5, name=name)
        name = "y_{}".format(k)
        y[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-9.5, ub=9.5, name=name)
        name = "u_{}".format(k)
        u[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-saturation, ub=saturation, name=name)
        name = "v_{}".format(k)
        v[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-saturation, ub=saturation, name=name)

    # use system variables in STL spec encoding
    stl_milp.variables['x'] = x
    stl_milp.variables['y'] = y
    stl_milp.variables['u'] = u
    stl_milp.variables['v'] = v

    # define the inital states for each mpc step
    for i in range(backward_steps + 1):
        stl_milp.model.addConstr(x[i] == x_init[current_step - backward_steps + i])
        stl_milp.model.addConstr(y[i] == y_init[current_step - backward_steps + i])
        
    # system constraints
    for k in range(backward_steps, period + backward_steps - 1):
        stl_milp.model.addConstr(x[k+1] == A[0][0] * x[k] + A[0][1] * y[k] + B[0][0] * u[k] + B[0][1] * v[k])
        stl_milp.model.addConstr(y[k+1] == A[1][0] * x[k] + A[1][1] * y[k] + B[1][0] * u[k] + B[1][1] * v[k])

    # add the specification (STL) constraints
    z = stl_milp.translate()
    # stl_milp.translate(satisfaction=True)
    # stl_milp.model.optimize()
    # stl_milp.model.write('model_test.lp')
    # method = method

    if method == 1:
        d = stl_milp.method_1()
        obj = [stl_milp.model.getObjective(objectives) for objectives in range(d+1)]
        print(str(obj), ':', [obj[i].getValue() for i in range(d+1)], "MILP")
    elif method == 2: 
        stl_milp.method_2()
        # print('Objective')
        obj = stl_milp.model.getObjective()
        # print(str(obj), obj.getValue(), "MILP")
    elif method == 3:
        stl_milp.method_3(z)
        # print('Objective')
        obj = stl_milp.model.getObjective()
        # print(str(obj), obj.getValue(), "MILP")

    pstlrobust = stl_milp.pstl2lp(ast)
    # x_rhovals = [rvar.x for rvar in pstlrobust.getVars()]
    # print("HERE CHECk HERE:", len(x_rhovals))
    
    # print("HERE PRINTING:", str(pstlrobust))

    x_vals = [var.x for var in stl_milp.variables['x'].values()]
    y_vals = [var.x for var in stl_milp.variables['y'].values()]
    

    x_init[current_step + 1] = x_vals[backward_steps + 1]
    y_init[current_step + 1] = y_vals[backward_steps + 1]

    return x_vals, y_vals
def main():

    # formula = '(G[2,4] (x <= 1)) && (G[8,10] (x >= 1)) && (G[14, 18] (x <= 2)) && (G[23, 28] (x >= 2)) '
    # formula = "G[2,8] (x>=3) && G[15,24] (x<=2)"
    # formula = "G[5,30] ((x>=2) && (y>=2))"
    # formula = "(G[10,20] (x>=2)) && (G[24,28](x<=-1)) && (G[5,8](x>=4))"
    # formula = "(G[10,25] (x>=3)) && (G[15,20](x<=-1))"
    # formula = "(G[10,15] (x>=4)) && (G[5,20](x<=2))"
    # formula = "(G[10,12](x>=1))"
    def zone(ap, T, l, u, a, b): # atomic proposition, Temporal operator, lower bound, upper bound, agent_x, agent_y
        if ap == "A":
            if T == "G":
                ret = " (G[{},{}](({}<=-6) && ({}<=-6))) ".format(l,u,a,b)
            elif T == "F":
                ret = " (F[{},{}](({}<=-6) && ({}<=-6))) ".format(l,u,a,b)
            else:
                raise NotImplementedError
        
        elif ap == "B":
            if T == "G":
                ret = " (G[{},{}](({}>=6) && ({}<=-6))) ".format(l,u,a,b)
            elif T == "F":
                ret = " (F[{},{}](({}>=6) && ({}<=-6))) ".format(l,u,a,b)
            else:
                raise NotImplementedError
        
        elif ap == "C":
            if T == "G":
                ret = " (G[{},{}](({}>=6) && ({}>=6))) ".format(l,u,a,b)
            elif T == "F":
                ret = " (F[{},{}](({}>=6) && ({}>=6))) ".format(l,u,a,b)
            else:
                raise NotImplementedError
       
        elif ap == "D":
            if T == "G": 
                ret = " (G[{},{}](({}<=-6) && ({}>=6))) ".format(l,u,a,b)
            elif T == "F":
                ret = " (G[{},{}](({}<=-6) && ({}>=6))) ".format(l,u,a,b)
            else:
                raise NotImplementedError
        
        elif ap == "O":
            if T == "G": 
                ret = " (G[{},{}]( ({}>= 3) || ({}<=-3) || ({}>=3) || ({}<=-3))) ".format(l,u,a,a,b,b)
            elif T == "F":
                ret = " (F[{},{}]( ({}>= 3) || ({}<=-3) || ({}>=3) || ({}<=-3))) ".format(l,u,a,a,b,b)
            else:
                raise NotImplementedError

        else:
            raise NotImplementedError
        return ret

    obstacle = "&&" + zone("O", "G", 0, 59, "x", "y")  
    # TODO: symmetric formula
    formula_ps = "(" + zone("A", "G", 0, 3, "x", "y") + "&&" + zone("B", "G", 10, 21, "x", "y") + "&&" + zone("D", "G", 10, 21, "x", "y") + ")"  #BLUE

    formula = "(" + zone("A", "G", 0, 3, "x", "y") + "&&" + zone("B", "F", 7, 14, "x", "y") + "&&" + zone("D", "G", 15, 20, "x", "y") + ")"  #RED

    # formula2 = "(" + zone("B", "G", 13, 14, "x2", "y2") + "&&" + zone("C", "G", 26, 28, "x2", "y2") + "&&" + zone("D", "G", 35, 40, "x2", "y2") + ")" + "&&" + "(" + zone("D", "G", 45, 50, "x", "y") + ")"  + "&&" + "(" + zone("C", "G", 15, 20, "x", "y") + ")"
    # formula3 = "(" + zone("D", "G", 10, 20, "x3", "y3") + "&&" + zone("A", "G", 30, 33, "x3", "y3") + "&&" + zone("D", "G", 45, 50, "x3", "y3") + ")" 
    # formula4 = "(" + zone("D", "G", 10, 20, "x4", "y4") + "&&" + zone("C", "G", 30, 33, "x4", "y4") + "&&" + zone("D", "G", 45, 50, "x4", "y4") + ")" 
    # formula5 = "(" + zone("B", "G", 10, 20, "x5", "y5") + "&&" + zone("A", "G", 30, 33, "x5", "y5") + "&&" + zone("D", "G", 45, 50, "x5", "y5") + ")" 
    # formula6 = "(" + zone("A", "G", 10, 20, "x6", "y6") + "&&" + zone("B", "G", 30, 33, "x6", "y6") + "&&" + zone("D", "G", 45, 50, "x6", "y6") + ")" 
    # formula = zone("B", "G", 18, 29, "x", "y") + "&&" + zone("D", "G", 18, 29, "x", "y") 
    formula += obstacle 
    formula_ps += obstacle
    # formula += formula2  #+ "&&" + formula3 + "&&" + formula4 + "&&" + formula5 + "&&" + formula6
    # formula = "(G[0,2] (x<=-6.5)) && (G[8,18](x>=6.5)) && (G[24,27](x<=-6.5))"
    # formula += " && (G[0,10] (y<=-6.5)) && (G[16,27](y>=6.5))"
    # formula = "(G[10,24] (x>=3)) && (G[13,15](x<=2))"
    # formula = "(G[8,12] (x>=2.1)) && (G[8,12](x<=2))"
    ranges = {'x': [-10, 10], 'y': [-10, 10]}

    # Stl2milp Initialization
    lexer = stlLexer(InputStream(formula))
    tokens = CommonTokenStream(lexer)
    parser = stlParser(tokens)
    t = parser.stlProperty()
    ast = STLAbstractSyntaxTreeExtractor().visit(t)

    lexer_ps = stlLexer(InputStream(formula_ps))
    tokens_ps = CommonTokenStream(lexer_ps)
    parser_ps = stlParser(tokens_ps)
    t_ps = parser_ps.stlProperty()
    ast_ps = STLAbstractSyntaxTreeExtractor().visit(t_ps)


    # Based on the formula, you need to define the period and the steps for it.
    # Normally, period should bigger than the formula range and steps should be bigger than period
    steps = 21
    period = 21
    x_init, y_init= -9, -8

    x = [0 if i != 0 else x_init for i in range(steps + period)]
    y = [0 if i != 0 else y_init for i in range(steps + period)]
    t = [i for i in range(steps + period)]

    x_v = []
    y_v = []
    x_ps = []
    y_ps = []
    x_v2 = []
    y_v2 = []
    x_ps2 = []
    y_ps2 = []
    x_v3 = []
    y_v3 = []
    x_ps3 = []
    y_ps3 = []
    for i in range(0, steps):
        x_v, y_v = pstl_mpc(x, y, i, period, ast, ranges, 1)


    for j in range(0, steps):
        x_ps, y_ps = pstl_mpc(x, y, j, period, ast_ps, ranges, 1)


    for i in range(0, steps):
        x_v2, y_v2 = pstl_mpc(x, y, i, period, ast, ranges, 2)

    for j in range(0, steps):
        x_ps2, y_ps2 = pstl_mpc(x, y, j, period, ast_ps, ranges, 2)

    for i in range(0, steps):
        x_v3, y_v3 = pstl_mpc(x, y, i, period, ast, ranges, 3)

    for j in range(0, steps):
        x_ps3, y_ps3 = pstl_mpc(x, y, j, period, ast_ps, ranges, 3)
    
    # print("Total time: ", total_time)
    # print(type(x_rho), len(x_rho), "rho: ", str(x_rho))
    # for i in range(60):
    #     val = np.sqrt(x_v[i]**2 +  y_v[i]**2)
    #     val2 = abs(x_v[i]) + abs(y_v[i])
    #     if val < 3:
    #         print("HERE: it was violated", i, val)
    #     elif val2 <3:
    #         print("HERE: it was violated2", i, val2)
    #     else:
    #         print("NEVER VIOLATED")

    fig, axs = plt.subplots(2)
    
    axs[0].plot(t[0:period], x_v[0:period], 'salmon', linestyle='dotted', linewidth=3, label="FS-HO", marker='s', markersize=13)
    axs[0].plot(t[0:period], x_ps[0:period], 'lightblue', linestyle='dotted', linewidth=3, label="PS-HO", marker='s', markersize=13)
    axs[0].plot(t[0:period], x_v2[0:period], 'salmon', linestyle='dashed', linewidth=3, label= 'FS-LDF', marker='s', markersize=13)
    axs[0].plot(t[0:period], x_ps2[0:period], 'lightblue', linestyle='dashed', linewidth=3, label="PS-LDF", marker='s', markersize=13)
    axs[0].plot(t[0:period], x_v3[0:period], 'r', linewidth=4, label= 'FS-WLN', marker='s', markersize=13)
    axs[0].plot(t[0:period], x_ps3[0:period], 'b', linewidth=4, label = "PS-WLN", marker='s', markersize=13)
    axs[0].grid()
    axs[0].set_xlabel('time', fontsize=25)
    axs[0].set_ylabel("x-position", fontsize=25)
    axs[0].set_ylim(-10, 10)
    axs[0].set_xlim(0, 20)
    axs[0].legend(fontsize = 'xx-large', loc= 'upper left')

    axs[1].plot(t[0:period], y_v[0:period], 'salmon', linestyle='dotted', linewidth=3, label="FS-HO", marker='s', markersize=13)
    axs[1].plot(t[0:period], y_ps[0:period], 'lightblue', linestyle='dotted', linewidth=3, label="PS-HO", marker='s', markersize=13)
    axs[1].plot(t[0:period], y_v2[0:period], 'salmon', linestyle='dashed', linewidth=3, label="FS-LDF", marker='s', markersize=13)
    axs[1].plot(t[0:period], y_ps2[0:period], 'lightblue', linestyle='dashed', linewidth=3, label="PS-LDF", marker='s', markersize=13)
    axs[1].plot(t[0:period], y_v3[0:period], 'r', linewidth=4, label="FS-WLN", marker='s', markersize=13)
    axs[1].plot(t[0:period], y_ps3[0:period], 'b', linewidth=4, label="PS-WLN", marker='s', markersize=13)
    axs[1].grid()
    axs[1].set_xlabel("time", fontsize=25)
    axs[1].set_ylabel("y-position", fontsize=25)
    axs[1].set_ylim(-10, 10)
    axs[1].set_xlim(0, 20)
    axs[1].legend(fontsize = 'xx-large', loc= 'upper left')
    fig.tight_layout()
    plt.show()
    environment(x_v[0:period], y_v[0:period], x_ps[0:period], y_ps[0:period],
                x_v2[0:period], y_v2[0:period], x_ps2[0:period], y_ps2[0:period],
                x_v3[0:period], y_v3[0:period], x_ps3[0:period], y_ps3[0:period])

if __name__ == '__main__':
    main()

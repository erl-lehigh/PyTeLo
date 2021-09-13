

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


# from stl2milp import stl2milp


def pstl_mpc(x_init, y_init, x_init2, y_init2, x_init3, y_init3,
             x_init4, y_init4, x_init5, y_init5, x_init6, y_init6,
            current_step, period, ast, ranges):
# def pstl_mpc(x_init, y_init, current_step, period, ast, ranges):
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

    saturation = 2 #2.4 , 2.3, 2

    for k in range(period + backward_steps):
        name = "x_{}".format(k)
        x[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-9.5, ub=9.5, name=name)
        name = "x2_{}".format(k)
        x2[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-9.5, ub=9.5, name=name)
        name = "y_{}".format(k)
        y[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-9.5, ub=9.5, name=name)
        name = "y2_{}".format(k)
        y2[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-9.5, ub=9.5, name=name)
        name = "u_{}".format(k)
        u[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-saturation, ub=saturation, name=name)
        name = "v_{}".format(k)
        v[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-saturation, ub=saturation, name=name)
        name = "u2_{}".format(k)
        u2[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-saturation, ub=saturation, name=name)
        name = "v2_{}".format(k)
        v2[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-saturation, ub=saturation, name=name)
        name = "x3_{}".format(k)
        x3[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-9.5, ub=9.5, name=name)
        name = "x4_{}".format(k)
        x4[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-9.5, ub=9.5, name=name)
        name = "y3_{}".format(k)
        y3[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-9.5, ub=9.5, name=name)
        name = "y4_{}".format(k)
        y4[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-9.5, ub=9.5, name=name)
        name = "u3_{}".format(k)
        u3[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-saturation, ub=saturation, name=name)
        name = "v3_{}".format(k)
        v3[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-saturation, ub=saturation, name=name)
        name = "u4_{}".format(k)
        u4[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-saturation, ub=saturation, name=name)
        name = "v4_{}".format(k)
        v4[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-saturation, ub=saturation, name=name)
        name = "x5_{}".format(k)
        x5[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-9.5, ub=9.5, name=name)
        name = "x6_{}".format(k)
        x6[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-9.5, ub=9.5, name=name)
        name = "y5_{}".format(k)
        y5[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-9.5, ub=9.5, name=name)
        name = "y6_{}".format(k)
        y6[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-9.5, ub=9.5, name=name)
        name = "u5_{}".format(k)
        u5[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-saturation, ub=saturation, name=name)
        name = "v5_{}".format(k)
        v5[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-saturation, ub=saturation, name=name)
        name = "u6_{}".format(k)
        u6[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-saturation, ub=saturation, name=name)
        name = "v6_{}".format(k)
        v6[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=-saturation, ub=saturation, name=name)

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
    method = 3

    if method == 1:
        d = stl_milp.method_1()
        obj = [stl_milp.model.getObjective(objectives) for objectives in range(d+1)]
        print(str(obj), ':', [obj[i].getValue() for i in range(d+1)], "MILP")
    elif method == 2: 
        stl_milp.method_2()
        print('Objective')
        obj = stl_milp.model.getObjective()
        print(str(obj), obj.getValue(), "MILP")
    elif method == 3:
        stl_milp.method_3(z)
        # print('Objective')
        # obj = stl_milp.model.getObjective()
        # print(str(obj), obj.getValue(), "MILP")

    # pstlrobust = stl_milp.pstl2lp(ast)
    # x_rhovals = [rvar.x for rvar in pstlrobust.getVars()]
    # print("HERE CHECk HERE:", len(x_rhovals))


    
    # print("HERE PRINTING:", str(pstlrobust))





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
    
    return x_vals, y_vals, x_vals2, y_vals2, x_vals3, y_vals3, x_vals4, y_vals4, x_vals5, y_vals5, x_vals6, y_vals6


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
    obstacle2 = "&&" + zone("O", "G", 0, 59, "x2", "y2")  
    obstacle3 = "&&" + zone("O", "G", 0, 59, "x3", "y3")  
    obstacle4 = "&&" + zone("O", "G", 0, 59, "x4", "y4")  
    obstacle5 = "&&" + zone("O", "G", 0, 59, "x5", "y5")  
    obstacle6 = "&&" + zone("O", "G", 0, 59, "x6", "y6") 
    obstacle += obstacle2 + obstacle3 + obstacle4 + obstacle5 +obstacle6
    # TODO: symmetric formula
    # formula = "(" + zone("C", "G", 25, 28, "x", "y") + "&&" + zone("B", "G", 10, 20, "x", "y") + "&&" + zone("D", "G", 10, 20, "x", "y") + ")"  

    # formula = "(" + zone("C", "G", 10, 20, "x", "y") + "&&" + zone("B", "G", 30, 33, "x", "y") + "&&" + zone("D", "G", 45, 50, "x", "y") + ")" + obstacle

    formula = "(" + zone("B", "G", 13, 14, "x2", "y2") + "&&" + zone("C", "G", 26, 28, "x2", "y2") + "&&" + zone("D", "G", 35, 40, "x2", "y2") + ")" + "&&" + "(" + zone("D", "G", 45, 50, "x", "y") + ")"  + "&&" + "(" + zone("C", "G", 15, 20, "x", "y") + ")" + obstacle
    # formula3 = "(" + zone("D", "G", 10, 20, "x3", "y3") + "&&" + zone("A", "F", 30, 33, "x3", "y3") + "&&" + zone("D", "G", 45, 50, "x3", "y3") + ")" + obstacle
    # formula4 = "(" + zone("D", "F", 10, 20, "x4", "y4") + "&&" + zone("C", "G", 30, 33, "x4", "y4") + "&&" + zone("D", "F", 45, 50, "x4", "y4") + ")" + obstacle
    # formula5 = "(" + zone("B", "G", 10, 20, "x5", "y5") + "&&" + zone("A", "G", 30, 33, "x5", "y5") + "&&" + zone("D", "F", 45, 50, "x5", "y5") + ")" + obstacle
    # formula6 = "(" + zone("A", "F", 10, 20, "x6", "y6") + "&&" + zone("B", "F", 30, 33, "x6", "y6") + "&&" + zone("D", "G", 45, 50, "x6", "y6") + ")" + obstacle 
    # formula = zone("B", "G", 18, 29, "x", "y") + "&&" + zone("D", "G", 18, 29, "x", "y") 
    # formula += "||" + formula3 + "||" + formula4 + "||" + formula5 +"||" + formula6 + "||" + formula2
    # formula += formula2  #+ "&&" + formula3 + "&&" + formula4 + "&&" + formula5 + "&&" + formula6
    # formula = "(G[0,2] (x<=-6.5)) && (G[8,18](x>=6.5)) && (G[24,27](x<=-6.5))"
    # formula += " && (G[0,10] (y<=-6.5)) && (G[16,27](y>=6.5))"
    # formula = "(G[10,24] (x>=3)) && (G[13,15](x<=2))"
    # formula = "(G[8,12] (x>=2.1)) && (G[8,12](x<=2))"
    ranges = {'x': [-10, 10], 'y': [-10, 10], 'x2': [-10, 10], 'y2': [-10, 10], 'x3': [-10, 10], 'y3': [-10, 10],
             'x4': [-10, 10], 'y4': [-10, 10], 'x5': [-10, 10], 'y5': [-10, 10], 'x6': [-10, 10], 'y6': [-10, 10]}

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
    steps = 60
    period = 60
    x_init, y_init, x_init2, y_init2, x_init3, y_init3 = -8, -8, 8, 8, 7, 6
    x_init4, y_init4, x_init5, y_init5, x_init6, y_init6 = -4, -4,-6, 5, 9, -6

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
    start = time.time()
    for i in range(0, steps):
        x_v, y_v, x_v2, y_v2, x_v3, y_v3, x_v4, y_v4, x_v5, y_v5, x_v6, y_v6 = pstl_mpc(
                                x, y, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, i, period, ast, ranges)
    end = time.time()
    total_time = end -start
    print("Total time: ", total_time)
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
    axs[0].plot(t[0:period/2], x_v[0:period/2],linewidth=2)
    lvertices3 = []
    lcodes3 = []
    lvertices4 = [] #method1
    lcodes4 = []    #method1
    lcodes4 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY] #method1
    lvertices4 += [(10, -9.5), (20, -9.5), (20, -5.5), (10, -5.5), (0, 0)] #method1
    lpath4 = Path(lvertices4, lcodes4) #method1
    lpathpatch4 = PathPatch(lpath4, facecolor='lightcyan', edgecolor='lightcyan') #method1
    axs[0].add_patch(lpathpatch4) #method1
    # lcodes3 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY] #method3
    # lvertices3 += [(10, 5.5), (20, 5.5), (20, 9.5), (10, 9.5), (0, 0)] #method3
    
    lcodes3 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    lvertices3 += [(25, 5.5), (28, 5.5), (28, 9.5), (25, 9.5), (0, 0)]    
    lpath3 = Path(lvertices3, lcodes3)
    lpathpatch3 = PathPatch(lpath3, facecolor='plum', edgecolor='plum', alpha=0.6)
    axs[0].add_patch(lpathpatch3)
    axs[0].grid()
    axs[0].set_xlabel('x-position', fontsize=25)
    axs[0].set_ylabel("time", fontsize=25)
    axs[0].axvspan(10, 10.2, facecolor='gray')
    axs[0].axvspan(20, 20.2, facecolor='gray')
    axs[0].axvspan(25, 25.2, facecolor='gray')
    axs[0].axvspan(28, 28.2, facecolor='gray')
    axs[0].set_ylim(-10, 10)
    axs[0].set_xlim(0, 30)
    axs[1].plot(t[0:period/2], y_v[0:period/2], linewidth=2.)
    lvertices4 = [] #method1
    lcodes4 = []    #method1
    lcodes4 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY] #method1
    lvertices4 += [(10, 5.5), (20, 5.5), (20, 9.5), (10, 9.5), (0, 0)]#method1
    lpath4 = Path(lvertices4, lcodes4) #method1
    lpathpatch4 = PathPatch(lpath4, facecolor='lightcyan', edgecolor='lightcyan') #method1
    axs[1].add_patch(lpathpatch4) #method1
    lvertices3 = []
    lcodes3 = []
    # lcodes3 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY] #method3
    # lvertices3 += [(10, 5.5), (20, 5.5), (20, 9.5), (10, 9.5), (0, 0)] #method3
    lcodes3 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    lvertices3 += [(25, 5.5), (28, 5.5), (28, 9.5), (25, 9.5), (0, 0)]    
    lpath3 = Path(lvertices3, lcodes3)
    lpathpatch3 = PathPatch(lpath3, facecolor='plum', edgecolor='plum', alpha=0.6)
    axs[1].add_patch(lpathpatch3)
    axs[1].axvspan(10, 10.2, facecolor='gray')
    axs[1].axvspan(20, 20.2, facecolor='gray')
    axs[1].axvspan(25, 25.2, facecolor='gray')
    axs[1].axvspan(28, 28.2, facecolor='gray')
    axs[1].grid()
    axs[1].set_xlabel("y-position", fontsize=25)
    axs[1].set_ylabel("time", fontsize=25)
    axs[1].set_ylim(-10, 10)
    axs[1].set_xlim(0, 30)
    fig.tight_layout()
    # plt.plot(t[10:26], x_rho)
    plt.show()

    environment(x_v[0:period], y_v[0:period], x_v2[0:period], y_v2[0:period], 
                x_v3[0:period], y_v3[0:period], x_v4[0:period], y_v4[0:period]
                , x_v5[0:period], y_v5[0:period], x_v6[0:period], y_v6[0:period])
    # environment(x_v[0:period/2], y_v[0:period/2])
if __name__ == '__main__':
    main()

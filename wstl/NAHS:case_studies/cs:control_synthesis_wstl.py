from antlr4 import InputStream, CommonTokenStream
import time
import numpy as np
import matplotlib.pyplot as plt
import gurobipy as grb
import sys
sys.path.append('../')

from stl import Operation, RelOperation, STLFormula
from wstlLexer import wstlLexer
from wstlParser import wstlParser
from wstlVisitor import wstlVisitor

from wstl import WSTLAbstractSyntaxTreeExtractor
# from stl import STLAbstractSyntaxTreeExtractor
from wstl2milp import wstl2milp
# from stl2milp import stl2milp
# from dstl2milp import dstl2milp
from gurobipy import *
# from stlLexer import stlLexer
# from stlParser import stlParser
# from stlVisitor import stlVisitor
# from stl import STLAbstractSyntaxTreeExtractor
# from environment import environment, stl_zone, wstl_zone

def wstl_synthesis_control(formula, A, B, vars_ub, vars_lb, control_ub, 
                          control_lb, weights, alpha=0.1, beta=0.1):
    
    lexer = wstlLexer(InputStream(formula))
    tokens = CommonTokenStream(lexer)
    parser = wstlParser(tokens)    
    t = parser.wstlProperty()
    ast = WSTLAbstractSyntaxTreeExtractor(weights).visit(t)
  
    wstl_milp = wstl2milp(ast)
   
    time_bound = int(ast.bound()) + 1
    x = dict()
    y = dict()
    u = dict()
    v = dict()
    x_aux = dict()
    y_aux =dict()
    u_aux = dict()
    v_aux =dict() 
    #creating the Gurobi Variables 
    for k in range(time_bound):
        name = "x_{}".format(k) 
        x[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                     ub=vars_ub, name=name)                             
        name = "y_{}".format(k)
        y[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                     ub=vars_ub, name=name)
        name = "u_{}".format(k)
        u[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=control_lb, 
                                     ub=control_ub, name=name)
        name = "v_{}".format(k)
        v[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=control_lb, 
                                     ub=control_ub, name=name)
        name = "x_aux_{}".format(k) 
        x_aux[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=0, 
                                     ub=vars_ub, name=name)
        name = "y_aux_{}".format(k)                                      
        y_aux[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=0, 
                                     ub=vars_ub, name=name)
        name = "u_aux_{}".format(k) 
        u_aux[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=0, 
                                     ub=vars_ub, name=name)
        name = "v_aux_{}".format(k)                                      
        v_aux[k] = wstl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=0, 
                                     ub=vars_ub, name=name)

    # use system variables in STL spec encoding
    wstl_milp.variables['x'] = x
    wstl_milp.variables['y'] = y
    wstl_milp.variables['u'] = u
    wstl_milp.variables['v'] = v

    # system constraints x[k+1] = A X[k]+ B U[k]
    for k in range(time_bound-1):
        wstl_milp.model.addConstr(x[k+1] == A[0][0] * x[k] + A[0][1] * y[k] +
                                           B[0][0] * u[k])

        wstl_milp.model.addConstr(y[k+1] == A[1][0] * x[k] + A[1][1] * y[k] +
                                           B[0][1] * v[k])
    
    #initial conditions
    wstl_milp.model.addConstr(x[0] == 0)
    wstl_milp.model.addConstr(y[0] == 0)
    wstl_milp.model.addConstr(u[0] == 0)
    wstl_milp.model.addConstr(v[0] == 0)

    # add the specification (STL) constraints
    _, rho_formula = wstl_milp.translate()
    wstl_milp.model.update()
    wstl_milp.model.setObjective(rho_formula, GRB.MAXIMIZE)
    wstl_milp.model.update()
    
    # add objective function
    wstl_milp.model.addConstrs(x_aux[k] == grb.abs_(x[k]) for k in range(time_bound))
    wstl_milp.model.addConstrs(y_aux[k] == grb.abs_(y[k]) for k in range(time_bound))
    state_cost = sum(x_aux[k] + y_aux[k] for k in range(time_bound))

    wstl_milp.model.addConstrs(u_aux[k] == grb.abs_(u[k]) for k in range(time_bound))
    wstl_milp.model.addConstrs(v_aux[k] == grb.abs_(v[k]) for k in range(time_bound))
    control_cost = sum(u_aux[k] + v_aux[k] for k in range(time_bound))

    wstl_milp.model.setObjectiveN(-state_cost, 2, weight=alpha, name='state_cost')
    wstl_milp.model.setObjectiveN(-control_cost, 3, weight=beta, name='control_cost')
    # Solve the problem with gurobi 
    wstl_milp.model.optimize()
    return wstl_milp

def visualize(stl_milp, stl_milp2):
    t = stl_milp.variables['x'].keys()
    t2 = stl_milp2.variables['x'].keys()

    stl_x = [var.x for var in stl_milp.variables['x'].values()]
    stl_y = [var.x for var in stl_milp.variables['y'].values()]
    stl_u = [var.x for var in stl_milp.variables['u'].values()]
    stl_v = [var.x for var in stl_milp.variables['v'].values()]
    stl_x2 = [var.x for var in stl_milp2.variables['x'].values()]
    stl_y2 = [var.x for var in stl_milp2.variables['y'].values()]
    stl_u2 = [var.x for var in stl_milp2.variables['u'].values()]
    stl_v2 = [var.x for var in stl_milp2.variables['v'].values()]
    
    fig, axs = plt.subplots(2, 2)
    # fig.suptitle('STL-Control Synthesis')

    axs[0][0].plot(t, stl_x, '-r', label=r'$\lambda=1, \alpha=0, \beta=0$', 
                   linewidth=3, marker='s', markersize=13)
    axs[0][0].plot(t, stl_x2, '-b', label=r'$\lambda=1, \alpha=0.1, \beta=0.1$',
                   linewidth=3, marker='s', markersize=13)                
    # axs[0][0].set_title('x vs t')
    axs[0][0].grid()
    axs[0][0].legend(prop={'size': 18})
    axs[0][0].xaxis.set_tick_params(labelsize=7)
    axs[0][0].tick_params(labelsize=18)

    axs[1][0].plot(t, stl_y, '-r', label=r'$\lambda=1, \alpha=0, \beta=0$', 
                   linewidth=3, marker='s', markersize=13)
    axs[1][0].plot(t, stl_y2, '-b', label=r'$\lambda=1, \alpha=0.1, \beta=0.1$',
                   linewidth=3, marker='s', markersize=13)
    # axs[1][0].set_title('y vs t')
    axs[1][0].grid()
    axs[1][0].legend(prop={'size': 18})
    axs[1][0].tick_params(labelsize=18)

    axs[0][1].plot(t, stl_u, '-r', label=r'$\lambda=1, \alpha=0, \beta=0$', 
                   linewidth=3, marker='s', markersize=13)
    axs[0][1].plot(t, stl_u2, '-b', label=r'$\lambda=1, \alpha=0.1, \beta=0.1$',
                   linewidth=3, marker='s', markersize=13)
    # axs[0][1].set_title('u vs t')
    axs[0][1].grid()
    axs[0][1].legend(prop={'size': 18})
    axs[0][1].tick_params(labelsize=18)


    axs[1][1].plot(t, stl_v, '-r', label=r'$\lambda=1, \alpha=0, \beta=0$', 
                   linewidth=3, marker='s', markersize=13)
    axs[1][1].plot(t, stl_v2, '-b', label=r'$\lambda=1, \alpha=0.1, \beta=0.1$',
                   linewidth=3, marker='s', markersize=13)
    # axs[1][1].set_title('v vs t')
    axs[1][1].grid()
    axs[1][1].legend(prop={'size': 18})
    axs[1][1].tick_params(labelsize=18)
    fig.tight_layout()
    plt.show()
    


if __name__ == '__main__':
    #Formulas
    # formula = '(G[3,5] (x >= 3)) && (G[9,10] (y >= 2) || G[9,10] (y <= -4))'
    wstl_formula = " &&^weight1 (G[3,5]^weight1  (x>=3), ||^weight2 \
                    (G[9,10]^weight1  (y>=2), G[9,10]^weight1  (y<=-4)))"    
    weights = {'weight1': lambda x: 1, 'weight2': lambda k: [0.1, 4][k], 'weight3': lambda x: 5}
    # Define the matrixes that used for linear system 
    A = [[1, 1], [0, 1]] 
    B = [[1,  1]] 
    vars_ub = 9
    vars_lb = -9
    control_ub = 5
    control_lb = -5

    # Translate WSTL to MILP and retrieve integer variable for the formula
    wstl_start = time.time()
    wstl_milp = wstl_synthesis_control(wstl_formula, A, B, vars_ub, vars_lb, control_ub,
                                    control_lb, weights, alpha=0, beta=0)
    wstl_milp2 = wstl_synthesis_control(wstl_formula, A, B, vars_ub, vars_lb, control_ub,
                                    control_lb, weights, alpha=0.1, beta=0.1)
    # wdstl_milp = wstl_synthesis_control(wstl_formula, A, B, vars_ub, vars_lb, control_ub,
    #                                 control_lb, weights, alpha=0, beta=0)
    # wdstl_milp2 = wstl_synthesis_control(wstl_formula, A, B, vars_ub, vars_lb, control_ub,
                                    # control_lb, weights, alpha=0.1, beta=0.1)                                
    wstl_end = time.time()
    wstl_time = wstl_end - wstl_start

    # print(formula, 'Time needed:', stl_time)
    
    visualize(wstl_milp, wstl_milp2)
 
    
    


import time
import matplotlib.pyplot as plt
import gurobipy as grb
import sys
sys.path.append('../')

from stl import to_ast as stl2ast
from stl2milp import stl2milp

def stl_synthesis_control(formula, A, B, vars_ub, vars_lb, control_ub, 
                          control_lb, alpha=0.1, beta=0.1):

    ast = stl2ast(formula)
    stl_milp = stl2milp(ast, robust=True)
    
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
        x[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                     ub=vars_ub, name=name)                             
        name = "y_{}".format(k)
        y[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=vars_lb, 
                                     ub=vars_ub, name=name)
        name = "u_{}".format(k)
        u[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=control_lb, 
                                     ub=control_ub, name=name)
        name = "v_{}".format(k)
        v[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=control_lb, 
                                     ub=control_ub, name=name)
        name = "x_aux_{}".format(k) 
        x_aux[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=0, 
                                     ub=vars_ub, name=name)
        name = "y_aux_{}".format(k)                                      
        y_aux[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=0, 
                                     ub=vars_ub, name=name)
        name = "u_aux_{}".format(k) 
        u_aux[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=0, 
                                     ub=vars_ub, name=name)
        name = "v_aux_{}".format(k)                                      
        v_aux[k] = stl_milp.model.addVar(vtype=grb.GRB.CONTINUOUS, lb=0, 
                                     ub=vars_ub, name=name)

    # use system variables in STL spec encoding
    stl_milp.variables['x'] = x
    stl_milp.variables['y'] = y
    stl_milp.variables['u'] = u
    stl_milp.variables['v'] = v

    # system constraints x[k+1] = A X[k]+ B U[k]
    for k in range(time_bound-1):
        stl_milp.model.addConstr(x[k+1] == A[0][0] * x[k] + A[0][1] * y[k] +
                                           B[0][0] * u[k])

        stl_milp.model.addConstr(y[k+1] == A[1][0] * x[k] + A[1][1] * y[k] +
                                           B[0][1] * v[k])
    
    #initial conditions
    stl_milp.model.addConstr(x[0] == 0)
    stl_milp.model.addConstr(y[0] == 0)
    stl_milp.model.addConstr(u[0] == 0)
    stl_milp.model.addConstr(v[0] == 0)

    # add the specification (STL) constraints
    stl_milp.translate(satisfaction=True)

    
    # add objective function
    stl_milp.model.addConstrs(x_aux[k] == grb.abs_(x[k]) for k in range(time_bound))
    stl_milp.model.addConstrs(y_aux[k] == grb.abs_(y[k]) for k in range(time_bound))
    state_cost = sum(x_aux[k] + y_aux[k] for k in range(time_bound))

    stl_milp.model.addConstrs(u_aux[k] == grb.abs_(u[k]) for k in range(time_bound))
    stl_milp.model.addConstrs(v_aux[k] == grb.abs_(v[k]) for k in range(time_bound))
    control_cost = sum(u_aux[k] + v_aux[k] for k in range(time_bound))

    stl_milp.model.setObjectiveN(state_cost, 2, weight=alpha, name='state_cost')
    stl_milp.model.setObjectiveN(control_cost, 3, weight=beta, name='control_cost')
    # Solve the problem with gurobi 
    stl_milp.model.optimize()
    return stl_milp


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
    formula = '(G[3,5] (x >= 3)) && (G[9,10] (y >= 2))'    
    # wstl_formula = "&&^weight2 ( G[5,10]^weight0  (x>=3),G[5,10]^weight3 \
    #                 (y<=-2), G[5,10]^weight3 (z>=1) )"
    # obstacle = "&&" + stl_zone("O", "G", 0, 30, "x", "y")
    # formula = '(' + stl_zone("C", "G", 10, 15, "x", "y") + ' && '+\
    #               stl_zone("D", "G", 25, 30, "x", "y") + ' && '+ \
    #                 stl_zone("A", "G", 0, 1, "x", "y") + obstacle + ')'

    # Define the matrixes that used for linear system 
    A = [[1, 1], [0, 1]] 
    B = [[1,  1]] 
    vars_ub = 9
    vars_lb = -9
    control_ub = 5
    control_lb = -5

    # Translate WSTL to MILP and retrieve integer variable for the formula
    stl_start = time.time()
    stl_milp = stl_synthesis_control(formula, A, B, vars_ub, vars_lb, control_ub,
                                    control_lb, alpha=0, beta=0)
    stl_milp2 = stl_synthesis_control(formula, A, B, vars_ub, vars_lb, control_ub,
                                    control_lb, alpha=0.1, beta=0.1)                                
    stl_end = time.time()
    stl_time = stl_end - stl_start

    print(formula, 'Time needed:', stl_time)
    
    visualize(stl_milp, stl_milp2)
 
    
    


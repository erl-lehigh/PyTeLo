"""
 Explainable Robotics Lab, Lehigh University
 See license.txt file for license information.
 @author: Gustavo Cardona, Cristian-Ioan Vasile, Crockett Lee Hensley
"""
import sys
sys.path.append('..')

from mstl2milp import mstl2milp
from stl import to_ast
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import time

AC="(x<=5 || x>=15 || y<=5 || y>=20)"
BC="(x<=20 || x>=30 || y<=6 || y>=15)"
C="(x>=0 && x<=10 && y>=24 && y<=30)"
D="(x>=15 && x<=20 && y>=25 && y<=35)"
E="(x>=25 && x<=35 && y>=26 && y<=31)"
F="(x>=16 && x<=21 && y>=0 && y<=5)"
formula = f'G[0,80]{AC} && G[0, 80]{BC} && ((F[0, 75]{C}) || (F[0, 75]{E}) || (F[0, 75]{D})) && G[75, 80]{F}]'

def addDynamics(model):
    for var in model.getVars():
        var_name = var.VarName
        print(var_name)
        if var_name.startswith('x_') or var_name.startswith('y_'):
            t = int(var_name.split('_')[1])
            if t > 0:
                model.addConstr(var - model.getVarByName(var_name.replace(f"_{t}_", f"_{t-1}_")) <= 1)
                model.addConstr(var - model.getVarByName(var_name.replace(f"_{t}_", f"_{t-1}_")) >= -1)
def maximal_stl_test(complete=False, balanced=True):
    ast = to_ast(formula)
    stl_milp = mstl2milp(ast, ranges={'x': [-10, 45], 'y': [-10, 45]}, robust=True)
    z = stl_milp.translate()
    stl_milp.model.addConstr(stl_milp.model.getVarByName('x_0_') == 0)
    stl_milp.model.addConstr(stl_milp.model.getVarByName('y_0_') == 0)
    addDynamics(stl_milp.model)
    if complete:
        d = stl_milp.hierarchical(balance=balanced, completeSolve=True)
        mstlrobust = stl_milp.model
        
    else:
        d = stl_milp.hierarchical(balance=balanced, completeSolve=False)
        mstlrobust = stl_milp.mstl2lp()
        mstlrobust.addConstr(mstlrobust.getVarByName('x_0_lp') == 0)
        mstlrobust.addConstr(mstlrobust.getVarByName('y_0_lp') == 0)
        addDynamics(mstlrobust)
        stl_milp.outerOptim(mstlrobust, balance=balanced)
    x_vals = []
    y_vals = []
    for var in mstlrobust.getVars():
        name = var.VarName
        if 'x_' in name:
            x_vals.append((int(name.split('_')[1]), var.X))
        elif 'y_' in name:
            y_vals.append((int(name.split('_')[1]), var.X))
    return ([v for t, v in x_vals], [v for t, v in y_vals])

    

if __name__ == '__main__':
     print("=" * 50)
     print("Running maximal_stl_test() function calls...")
     print("=" * 50)
     
     start = time.time()
     x1, y1 = maximal_stl_test(False, False)
     elapsed1 = (time.time() - start) * 1000
     
     start = time.time()
     x2, y2 = maximal_stl_test(False, True)
     elapsed2 = (time.time() - start) * 1000
     
     start = time.time()
     x3, y3 = maximal_stl_test(True, False)
     elapsed3 = (time.time() - start) * 1000
     
     start = time.time()
     x4, y4 = maximal_stl_test(True, True)
     elapsed4 = (time.time() - start) * 1000
     print(f"maximal_stl_test(incomplete, unbalanced): {elapsed1:.2f} ms\n")
     print(f"maximal_stl_test(incomplete, balanced): {elapsed2:.2f} ms\n")
     print(f"maximal_stl_test(complete, unbalanced): {elapsed3:.2f} ms\n")
     print(f"maximal_stl_test(complete, balanced): {elapsed4:.2f} ms\n")
     
     print("=" * 50)
     
     # Define colors and line styles that work in both color and B&W
     colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # blue, orange, green, red
     linestyles = ['-', '--', '-.', ':']  # solid, dashed, dash-dot, dotted
     labels = ['Unbalanced (incomplete)', 'Balanced (incomplete)', 
               'Unbalanced (complete)', 'Balanced (complete)']
     
     # Plot 1: XY Plane - All trajectories
     fig1, ax1 = plt.subplots(figsize=(12, 10))
     
     # Define regions with De Morgan's law applied to AC and BC complements
     # AC = (x<=5 || x>=15 || y<=5 || y>=20) is complement, so A = (x>5 && x<15 && y>5 && y<20)
     # BC = (x<=20 || x>=30 || y<=6 || y>=15) is complement, so B = (x>20 && x<30 && y>6 && y<15)
     regions = {
         'A': {'x_min': 5, 'x_max': 15, 'y_min': 5, 'y_max': 20, 'color': '#FFD700', 'alpha': 0.3},
         'B': {'x_min': 20, 'x_max': 30, 'y_min': 6, 'y_max': 15, 'color': '#87CEEB', 'alpha': 0.3},
         'C': {'x_min': 0, 'x_max': 10, 'y_min': 24, 'y_max': 30, 'color': '#FFB6C1', 'alpha': 0.3},
         'D': {'x_min': 15, 'x_max': 20, 'y_min': 25, 'y_max': 35, 'color': '#90EE90', 'alpha': 0.3},
         'E': {'x_min': 25, 'x_max': 35, 'y_min': 26, 'y_max': 31, 'color': '#DDA0DD', 'alpha': 0.3},
         'F': {'x_min': 16, 'x_max': 21, 'y_min': 0, 'y_max': 5, 'color': '#F0E68C', 'alpha': 0.3},
     }
     
     # Draw regions
     for region_name, region_props in regions.items():
         width = region_props['x_max'] - region_props['x_min']
         height = region_props['y_max'] - region_props['y_min']
         rect = Rectangle((region_props['x_min'], region_props['y_min']), 
                          width, height, 
                          linewidth=2, edgecolor='black', 
                          facecolor=region_props['color'], 
                          alpha=region_props['alpha'])
         ax1.add_patch(rect)
         # Add label in center of region
         label_x = region_props['x_min'] + width / 2
         label_y = region_props['y_min'] + height / 2
         ax1.text(label_x, label_y, region_name, fontsize=14, fontweight='bold',
                  ha='center', va='center', bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
     
     ax1.plot(x1, y1, color=colors[0], linestyle=linestyles[0], linewidth=2, 
              label=labels[0], marker='o', markersize=4)
     ax1.plot(x2, y2, color=colors[1], linestyle=linestyles[1], linewidth=2, 
              label=labels[1], marker='s', markersize=4)
     ax1.plot(x3, y3, color=colors[2], linestyle=linestyles[2], linewidth=2, 
              label=labels[2], marker='^', markersize=4)
     ax1.plot(x4, y4, color=colors[3], linestyle=linestyles[3], linewidth=2, 
              label=labels[3], marker='d', markersize=4)
     ax1.set_xlabel('X Position', fontsize=12)
     ax1.set_ylabel('Y Position', fontsize=12)
     ax1.set_title('Trajectories in XY Plane with Regions', fontsize=14, fontweight='bold')
     ax1.legend(loc='best', fontsize=10)
     ax1.grid(True, alpha=0.3)
     ax1.set_xlim(-10, 45)
     ax1.set_ylim(-10, 45)
     
     # Plot 2: X values over time
     fig2, ax2 = plt.subplots(figsize=(10, 6))
     time1 = list(range(len(x1)))
     time2 = list(range(len(x2)))
     time3 = list(range(len(x3)))
     time4 = list(range(len(x4)))
     ax2.plot(time1, x1, color=colors[0], linestyle=linestyles[0], linewidth=2, 
              label=labels[0], marker='o', markersize=4)
     ax2.plot(time2, x2, color=colors[1], linestyle=linestyles[1], linewidth=2, 
              label=labels[1], marker='s', markersize=4)
     ax2.plot(time3, x3, color=colors[2], linestyle=linestyles[2], linewidth=2, 
              label=labels[2], marker='^', markersize=4)
     ax2.plot(time4, x4, color=colors[3], linestyle=linestyles[3], linewidth=2, 
              label=labels[3], marker='d', markersize=4)
     ax2.set_xlabel('Time Step', fontsize=12)
     ax2.set_ylabel('X Position', fontsize=12)
     ax2.set_title('X Position over Time', fontsize=14, fontweight='bold')
     ax2.legend(loc='best', fontsize=10)
     ax2.grid(True, alpha=0.3)
     
     # Plot 3: Y values over time
     fig3, ax3 = plt.subplots(figsize=(10, 6))
     ax3.plot(time1, y1, color=colors[0], linestyle=linestyles[0], linewidth=2, 
              label=labels[0], marker='o', markersize=4)
     ax3.plot(time2, y2, color=colors[1], linestyle=linestyles[1], linewidth=2, 
              label=labels[1], marker='s', markersize=4)
     ax3.plot(time3, y3, color=colors[2], linestyle=linestyles[2], linewidth=2, 
              label=labels[2], marker='^', markersize=4)
     ax3.plot(time4, y4, color=colors[3], linestyle=linestyles[3], linewidth=2, 
              label=labels[3], marker='d', markersize=4)
     ax3.set_xlabel('Time Step', fontsize=12)
     ax3.set_ylabel('Y Position', fontsize=12)
     ax3.set_title('Y Position over Time', fontsize=14, fontweight='bold')
     ax3.legend(loc='best', fontsize=10)
     ax3.grid(True, alpha=0.3)
     
     plt.tight_layout()
     plt.show()
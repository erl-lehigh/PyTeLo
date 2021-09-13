from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt
import numpy as np
import time

def environment(x, y, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
# def environment(x, y):
    # Desired locations 
    lvertices1 = []
    lcodes1 = []
    lvertices2 = []
    lcodes2 = []
    lvertices3 = []
    lcodes3 = []
    lvertices4 = []
    lcodes4 = []
    
    # lcodes += [Path.MOVETO] + [Path.LINETO]*2 + [Path.CLOSEPOLY]
    # lvertices += [(4, 4), (5, 5), (5, 4), (0, 0)]
    # lvertices += [(1, 1), (1, 4), (4, 4), (4, 1), (0, 0)]
    lcodes1 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    lvertices1 += [(5.5, -9.5), (9.5, -9.5), (9.5, -5.5), (5.5, -5.5), (0, 0)]

    lcodes2 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    lvertices2 += [(-9.5, -9.5), (-5.5, -9.5), (-5.5, -5.5), (-9.5, -5.5), (0, 0)]

    lcodes3 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    lvertices3 += [(5.5, 5.5), (9.5, 5.5), (9.5, 9.5), (5.5, 9.5), (0, 0)]

    lcodes4 += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    lvertices4 += [(-9.5, 5.5), (-5.5, 5.5), (-5.5, 9.5), (-9.5, 9.5), (0, 0)]



    lpath1 = Path(lvertices1, lcodes1)
    lpath2 = Path(lvertices2, lcodes2)
    lpath3 = Path(lvertices3, lcodes3)
    lpath4 = Path(lvertices4, lcodes4)

    lpathpatch1 = PathPatch(lpath1, facecolor='skyblue', edgecolor='k')
    lpathpatch2 = PathPatch(lpath2, facecolor='wheat', edgecolor='k')
    lpathpatch3 = PathPatch(lpath3, facecolor='plum', edgecolor='k')
    lpathpatch4 = PathPatch(lpath4, facecolor='lightcyan', edgecolor='k')



    #obstacles
    overtices = []
    ocodes = []
    ocodes += [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    overtices += [(-2.2, -2.2), (2.2, -2.2), (2.2, 2.2), (-2.2, 2.2), (0, 0)]
    opath = Path(overtices, ocodes)
    opathpatch = PathPatch(opath, facecolor='gray', edgecolor='k', linewidth='3')

    # Envieronment border
    vertices = []
    codes = []

    codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    vertices = [(-10, -10), (10, -10), (10, 10), (-10, 10), (0, 0)]

    path = Path(vertices, codes)

    pathpatch = PathPatch(path, facecolor='NONE', edgecolor='k', linewidth='8')

    fig, ax = plt.subplots()
    ax.text(-9, -9, 'A', fontsize=90)
    ax.text(6, 6, 'C', fontsize=90)
    ax.text(-9, 6, 'D', fontsize=90)
    ax.text(6, -9, 'B', fontsize=90)
    ax.text(-2, -0.5, 'OBS', fontsize=50)
    ax.add_patch(lpathpatch1)
    ax.add_patch(lpathpatch2)
    ax.add_patch(lpathpatch3)
    ax.add_patch(lpathpatch4)
    ax.add_patch(pathpatch)
    ax.add_patch(opathpatch)
    # ax.set(xlim=(-15, 15), ylim=(-15, 15))
    # ax.grid()
    ax.axis('equal')
    ax.plot(x, y, linewidth=2.5)
    ax.plot(x2, y2, linewidth=2.5)
    ax.plot(x3, y3, linewidth=2.5)
    ax.plot(x4, y4, linewidth=2.5)
    ax.plot(x5, y5, linewidth=2.5)
    ax.plot(x6, y6, linewidth=2.5)
    plt.show()

if __name__ == '__main__':
    x = 0
    y = 0
    

    start = time.time()
    print("hello")
    environment(x, y)
    end = time.time()
    print(end - start)
   


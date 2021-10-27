from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt
import numpy as np
import time

def environment6(x, y, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12):
# def environment(x, y, x2, y2):
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
    ax.text(-1.3, -1.3, 'E', fontsize=90)
    ax.add_patch(lpathpatch1)
    ax.add_patch(lpathpatch2)
    ax.add_patch(lpathpatch3)
    ax.add_patch(lpathpatch4)
    ax.add_patch(pathpatch)
    ax.add_patch(opathpatch)
    # ax.set(xlim=(-15, 15), ylim=(-15, 15))
    # ax.grid()
    ax.plot(x[0], y[0],'g', marker='*', markersize=28)
    ax.plot(x[29], y[29],'g', marker='s', markersize=20)
    ax.plot(x2[0], y2[0],'b', marker='*', markersize=28)
    ax.plot(x2[29], y2[29], 'b',marker='s', markersize=20)
    ax.plot(x3[0], y3[0],'r', marker='*', markersize=28)
    ax.plot(x3[29], y3[29],'r', marker='s', markersize=20)
    ax.plot(x4[0], y4[0],'m', marker='*', markersize=28)
    ax.plot(x4[29], y4[29],'m', marker='s', markersize=20)
    ax.plot(x5[0], y5[0],'y', marker='*', markersize=28)
    ax.plot(x5[29], y5[29],'y', marker='s', markersize=20)
    ax.plot(x6[0], y6[0],'c', marker='*', markersize=28)
    ax.plot(x6[29], y6[29],'c', marker='s', markersize=20)
    ax.plot(x7[0], y7[0], 'pink',marker='*', markersize=28)
    ax.plot(x7[29], y7[29],'pink', marker='s', markersize=20)
    ax.plot(x8[0], y8[0], 'salmon',marker='*', markersize=28)
    ax.plot(x8[29], y8[29], 'salmon',marker='s', markersize=20)
    ax.plot(x9[0], y9[0],'lime', marker='*', markersize=28)
    ax.plot(x9[29], y9[29], 'lime',marker='s', markersize=20)
    ax.plot(x10[0], y10[0], 'orange',marker='*', markersize=28)
    ax.plot(x10[29], y10[29],'orange', marker='s', markersize=20)
    ax.plot(x11[0], y11[0], 'brown',marker='*', markersize=28)
    ax.plot(x11[29], y11[29],'brown', marker='s', markersize=20)
    ax.plot(x12[0], y12[0],'maroon', marker='*', markersize=28)
    ax.plot(x12[29], y12[29], 'maroon',marker='s', markersize=20)
    ax.axis('equal')
    ax.plot(x, y,'g', linestyle='dashed', linewidth=5.5, label = "FS-Robot1" , alpha=0.5)
    ax.plot(x2, y2,'b', linestyle='dashed', linewidth=5.5, label = "FS-Robot2", alpha=0.5)
    ax.plot(x3, y3, 'r',linestyle='dashed', linewidth=5.5, label = "FS-Robot3", alpha=0.5)
    ax.plot(x4, y4,'m', linestyle='dashed', linewidth=5.5, label = "FS-Robot4", alpha=0.5)
    ax.plot(x5, y5, 'y', linestyle='dashed', linewidth=5, label = "FS-Robot5", alpha=0.5)
    ax.plot(x6, y6,'c',  linestyle='dashed', linewidth=5, label = "FS-Robot6", alpha=0.5)

    ax.plot(x7, y7,'pink', linewidth=5.5, label = "PS-Robot1" )
    ax.plot(x8, y8,'salmon', linewidth=5.5, label = "PS-Robot2", alpha=0.8)
    ax.plot(x9, y9,'lime',  linewidth=5.5, label = "PS-Robot3", alpha=0.8)
    ax.plot(x10, y10, 'orange',linewidth=5.5, label = "PS-Robot4", alpha=0.8)
    ax.plot(x11, y11,'brown', linewidth=5, label = "PS-Robot5", alpha=0.8)
    ax.plot(x12, y12,'maroon', linewidth=5, label = "PS-Robot6", alpha=0.8)
    ax.legend(fontsize = 'xx-large')
    plt.show()

if __name__ == '__main__':
    x = 0
    y = 0
    d=0
    a=0

    start = time.time()
    print("hello")
    environment6(x, y, d, a, x, y, d, a, x, y, d, a, x, y, d, a, x, y, d, a ,x, y, d, a)
    end = time.time()
    print(end - start)
   


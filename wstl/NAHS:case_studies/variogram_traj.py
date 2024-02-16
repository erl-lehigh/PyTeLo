import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint
import warnings
warnings.filterwarnings("ignore")
import skgstat as skg
import plotly
from plotly.subplots import make_subplots



plt.rcParams['lines.linewidth'] = 3
plt.rcParams['lines.markersize'] = 15
plt.rcParams['lines.marker'] = '*'
font = {'family' : 'normal',

        'size'   : 18}

plt.rc('font', **font)
# src = skg.data.meuse()
# print(src.get('origin'))
#
# coords, vals = src.get('sample')
# # make a nice table
# pd.DataFrame({'x': coords[:, 0], 'y': coords[:, 1], 'lead': vals.flatten()}).head()
#
# fig, ax = plt.subplots(1, 1, figsize=(9, 9))
# art = ax.scatter(coords[:, 0], coords[:, 1], s=50, c=vals.flatten(), cmap='plasma')
# plt.colorbar(art)
#
#
# V = skg.Variogram(coords, vals.flatten(), maxlag='median', n_lags=15, normalize=False)
# fig = V.plot()
# plt.show()
#
#
# print('Sample variance: %.2f   Variogram sill: %.2f' % (vals.flatten().var(), V.describe()['sill']))
#
# pprint(V.describe())
# print(V)




data = pd.read_csv('traj.csv')
mean_traj = data.mean(axis=0)
print(len(mean_traj))
weights = np.arange(0, len(mean_traj))
print(len(weights))
fig, ax = plt.subplots(1, 1, figsize=(9, 9))

# for i in range(len(data)):
#     ax.scatter(weights, data.loc[i], '-s', label='x_wstl_{}'.format(i))

Corrdinates = ax.scatter(weights, mean_traj, s=50,  cmap='plasma')
plt.colorbar(Corrdinates)
plt.show()
#
V = skg.Variogram(mean_traj, weights, maxlag='median',  normalize=True)
fig1 = V.plot(hist=False, show=False, grid=False)
plt.show()



obj = [0.75, 0.7500000001750001, 0.75, 0.7500000001750002, 0.7500000001750001, 0.7500014998280093, 0.75, 0.7500004998266776, 0.5999999999999999, 0.29999999999999993]

obj = np.round(obj, 3)
weights = np.linspace(0, 1, len(obj))

W = skg.Variogram(obj, weights,    normalize=False)
# fig = W.plot(hist=False, show=False)
# plt.show()

fig = make_subplots(rows=1, cols=1)
fig.update_layout(
    width=800,
    height=200,
    template='seaborn',
    showlegend=False,
    margin=dict(l=0, r=0, b=0, t=0)
 )

W.plot( hist=False, show=False, grid=False)
fig
plt.show()



# weights = np.arange(0, 1, 0.1)
# t = np.arange(0, len(mean_traj))
# weights = np.arange(0, len(mean_traj))
#
# fig1 = plt.figure().add_subplot(projection='3d')
# data=  data.T
# for i in range(len(data)):
#     fig1.scatter3D(weights, t, data.loc[i])
#     plt.draw()
#     plt.show()
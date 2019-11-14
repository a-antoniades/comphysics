import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# this script solves laplace's equation (Δ^2V)=0, using numerical methods,
# and plots results


# create empty array

dfx = np.zeros(shape=(101, 1))
dfy = np.zeros(shape=(1,101))
df2 = np.array([2])

for i in range(0, 100):
    dfx[i] = i
    dfy[:, i] = i

# make array into v = sin^2(arctan(y/x))
# note, to make matters simpler I changed the -1 - 1 box to a 0-100 box.

dfarctan = np.arctan2(dfy, dfx)
dfsin = np.sin(dfarctan)
dfsinsqrd = np.power(dfsin, 2)  # array with 100 x 100 elements
dfsinsqrd[2:99, 2:99] = 0

dflaplace = np.copy(dfsinsqrd)
dflaplacey = np.copy(dflaplace)


# at 200 tries the values seemed to converge pretty well, better technique might be
# to set threshold for variance between adjacent values

for k in range(400):
    for j in range(2, 100):
        for i in range(2, 100):
            dflaplacey[i,j] = 1/4*(dflaplacey[i-1, i] + dflaplacey[i+1, i]
                                   + dflaplacey[i, i-1] + dflaplacey[i, i+1])


# plot the pringle

dflaplacex= pd.DataFrame(dflaplacey[1:98, 1:98])

x = np.arange(len(dflaplacex.columns))
X,Y = np.meshgrid(x, x)
Z = dflaplacex
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init(elev=35, azim=30)
ax = Axes3D.plot_surface(ax, X, Y, Z, cmap='hot')
plt.savefig('3d-pringle.png')




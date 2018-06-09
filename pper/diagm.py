from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

import csv

fig = plt.figure()

alpha = []
beta = []
ah = []
al = []

with open("c:\\users\\hypnoes\\downloads\\cedf.csv\\cedf.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        alpha.append(row[0])
        beta.append(row[1])
        ah.append(row[2])
        al.append(row[3])

ah = np.array(list(map(np.float, ah)))
al = np.array(list(map(np.float, al)))

#ah = ah.reshape(11, 11)
#al = al.reshape(11, 11)

X = np.arange(0.0, 1.1, 0.1)
Y = np.arange(0.0, 1.1, 0.1)
X, Y = np.meshgrid(X, Y)

aX = np.triu(X).flatten()
X = np.array([0.0] + aX[aX.nonzero()].tolist())

aY = np.tril(Y).flatten()
Y = np.array([0.0] + aY[aY.nonzero()].tolist())

ax = fig.add_subplot(1, 2, 1, projection='3d')
#surf1 = ax.plot_surface(X, Y, al, label="al", linewidth=0, antialiased=True)
surf3 = ax.plot_trisurf(X, Y, ah, alpha=0.9, label="ah", linewidth=0, antialiased=True)

ax.set_zlim(0.5, 1.0)
ax.zaxis.set_major_locator(LinearLocator(20))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

ax.set_xlabel("alpha")
ax.set_ylabel("beta")
ax.set_zlabel("accuracy %")

ax = fig.add_subplot(1, 2, 2, projection='3d')
#surf2 = ax.plot_surface(X, Y, ah, label="ah", linewidth=0, antialiased=True)
surf4 = ax.plot_trisurf(X, Y, al, alpha=0.9, label="al", linewidth=0, antialiased=True)

ax.set_zlim(0.5, 1.0)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

ax.set_xlabel("alpha")
ax.set_ylabel("beta")
ax.set_zlabel("accuracy %")

plt.show()

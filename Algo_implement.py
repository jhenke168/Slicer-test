#goal: read files and display
#need to install plotly==4.11.0
import plotly.graph_objects as go
import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt

mc_file = open('mc115L.iv', 'r')
mc_mesh = mc_file.read().splitlines()

mc_coord_file = open('SCS_mc1.dat', 'r')
mc_coord = mc_coord_file.read().splitlines()

mc_coord_array = []
for i in range(len(mc_coord)):
    row = mc_coord[i].split()
    for j in range(len(row)):
        row[j] = float(row[j])
    mc_coord_array.append(row)

mc_mesh_coords = []
for i in range(18589,55744): 
    row = mc_mesh[i].split()
    for j in range(len(row)):
        row[j] = row[j].strip(',')
        row[j] = float(row[j])
    mc_mesh_coords.append(row)

mc_mesh_points = []
for i in range(6,18585): 
    row = mc_mesh[i].split(',')
    row = row[0].split()
    for j in range(len(row)):
        row[j] = float(row[j])
    mc_mesh_points.append(row)

mc_mesh_points = np.array(mc_mesh_points)
x = mc_mesh_points[:,0]
#x_t = np.transpose[x]
y = mc_mesh_points[:,1]
#y_t = np.transpose[y]
z = mc_mesh_points[:,2]
mc_mesh_coords = np.array(mc_mesh_coords)
i = mc_mesh_coords[:,0]
i_t = np.transpose(i)
j = mc_mesh_coords[:,1]
j_t = np.transpose(j)
k = mc_mesh_coords[:,2]
k_t = np.transpose(k)
#i'm pretty sure the coordinate index corresponds with i,j,k in plotly but there are obviously issues

#fig = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z, color='lightpink', opacity=0.50,  i=i_t, j=j_t, k=k_t)]) #, i=i, j=j, k=k
#fig.show()

triangles = mc_mesh_coords[:, 0:3]
print(triangles)
matplotlib.tri.Triangulation(x, y, triangles=triangles, mask=None)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_trisurf(triangulation, x, y, z, linewidth=0.2, antialiased=True)
plt.show()
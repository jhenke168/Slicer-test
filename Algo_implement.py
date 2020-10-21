#goal: read files and display
#need to install plotly==4.11.0
import plotly.graph_objects as go
import numpy as np

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
    mc_mesh_array.append(row)

mc_mesh_array = []
for i in range(6,18585): 
    row = mc_mesh[i].split(',')
    row = row[0].split()
    for j in range(len(row)):
        row[j] = float(row[j])
    mc_mesh_coords.append(row)

mc_mesh_array = np.array(mc_mesh_array)
x = mc_mesh_array[:,0]
y = mc_mesh_array[:,1]
z = mc_mesh_array[:,2]

fig = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z, color='lightpink', opacity=0.50)])
fig.show()
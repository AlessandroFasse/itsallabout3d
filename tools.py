import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def print_2d_mesh(vertices, faces): # prints the x and y coordintes of the mesh including the edges    
    for i in range(np.shape(faces)[0]):
        for j in range(3):
            x = np.array([[vertices[faces[i,j], 0]],
                          [vertices[faces[i,(j+1)%3], 0]]])
            y = np.array([[vertices[faces[i,j], 1]],
                          [vertices[faces[i,(j+1)%3], 1]]])
            plt.plot(x, y, c='#FF8B00', zorder=0)
    plt.scatter(vertices[:, 0], vertices[:, 1], c='k', zorder=1, s=80)
    plt.show()

def print_3d_mesh(vertices, faces): # prints the mesh in 3d
    fig = plt.figure()
    ax = Axes3D(fig)
    for i in range(np.shape(faces)[0]):
        for j in range(3):
            x = np.array([[vertices[faces[i,j], 0]],
                          [vertices[faces[i,(j+1)%3], 0]]])
            y = np.array([[vertices[faces[i,j], 1]],
                          [vertices[faces[i,(j+1)%3], 1]]])
            z = np.array([[vertices[faces[i,j], 2]],
                          [vertices[faces[i,(j+1)%3], 2]]])
            ax.plot(x, y, c='#FF8B00', zorder=0)
    ax.scatter(vertices[:,0], vertices[:,1], vertices[:, 2], c='k', s=80)
    plt.show()
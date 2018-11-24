import numpy
from tools import *


'''
Exercise 1

Write a down the vertices and faces of a cube as given in the picture
'''



vertices = np.array([[0,0,0],
            [1,0,0],
            [0,1,0],
            [1,1,0]])

faces = np.array([[0,1,3],
         [3,2,0]])

print_3d_mesh(vertices, faces)

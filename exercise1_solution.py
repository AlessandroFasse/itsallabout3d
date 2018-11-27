import numpy
from tools import *

## Exercise 1 - It's all about 3D Workshop

vertices = np.array([[0,0,0],
                     [1,0,0],
                     [1,1,0],
                     [0,1,0],
                     [0,0,1],
                     [1,0,1],
                     [1,1,1],
                     [0,1,1]], dtype=np.float16)

faces = np.array([[0,2,1], # bottom
                  [0,3,2],
                  [4,0,5], # back
                  [5,0,1],
                  [6,5,1], # right side
                  [6,1,2], 
                  [7,6,2], # front 
                  [7,2,3],
                  [4,7,3], # left side
                  [4,3,0], 
                  [4,5,7], # top
                  [7,5,6]], dtype=np.uint8)

# Check your result with a 3d print of the vertices and edges
print_3d_mesh(vertices, faces)

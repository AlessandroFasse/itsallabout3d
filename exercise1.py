import numpy
from tools import *

## Exercise 1 - It's all about 3D Workshop

vertices = np.array([[0,0,0], [1,0,0]], dtype=np.float16)
faces = np.array([[0,1,1]], dtype=np.uint8)

# Check your result with a 3d print of the vertices and edges
print_3d_mesh(vertices, faces)

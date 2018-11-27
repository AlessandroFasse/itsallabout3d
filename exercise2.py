import numpy
from tools import *

# a)
vertices = np.array([[]], dtype=np.float16)

faces = np.array([[]], dtype=np.uint8)

print_3d_mesh(vertices, faces)

# b) 

# c)
def compute_face_normals(vertices, faces):
    face_normals = np.zeros(np.shape(faces))
    for i in range(np.shape(faces)[0]):
        # insert your solution here
    return face_normals

print(compute_face_normals(vertices, faces)) # print the result

# d)
def compute_face_areas(vertices, faces):
    face_areas = np.zeros(np.shape(faces)[0])
    for i in range(np.shape(faces)[0]):
        # insert your solution here
    return face_areas

print(compute_face_areas(vertices, faces)) # print the result

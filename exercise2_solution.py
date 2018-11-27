import numpy
from tools import *

# a)
vertices = np.array([[0,0,0],
                     [1,0,0],
                     [0,1,0],
                     [0,0,1]], dtype=np.float16)

faces = np.array([[0,1,2],
                  [3,0,1],
                  [3,2,0],
                  [3,2,1]], dtype=np.uint8)

print_3d_mesh(vertices, faces)

# b) Yes

# c)
def compute_face_normals(vertices, faces):
    face_normals = np.zeros(np.shape(faces))
    for i in range(np.shape(faces)[0]):
        face_normals[i] = np.cross(vertices[faces[i,1]]-vertices[faces[i,0]], vertices[faces[i,2]]-vertices[faces[i,0]]) # compute the normal vector via the cross product
        face_normals[i] /= np.linalg.norm(face_normals[i]) # normalize the computed vectors
    return face_normals

print(compute_face_normals(vertices, faces)) # print the result

# d)
def compute_face_areas(vertices, faces):
    face_areas = np.zeros(np.shape(faces)[0])
    for i in range(np.shape(faces)[0]):
        face_areas[i] = np.linalg.norm(np.cross(vertices[faces[i,1]]-vertices[faces[i,0]], vertices[faces[i,2]]-vertices[faces[i,0]]))/2 # compute the area as the half of the norm of the cross product
    return face_areas

print(compute_face_areas(vertices, faces)) # print the result

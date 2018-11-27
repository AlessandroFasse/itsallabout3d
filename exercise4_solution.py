import numpy as np

# c)
def compute_boundary(faces):
    boundary_vertices = []
    nr_faces = np.shape(faces)[0]
    for i in range(nr_faces-1):
        for j in range(nr_faces):
            test = 1 
import numpy as np
from exercise3_solution import compute_edges

# the cube of exercise 1 without the top, so the solution is [4,5,6,7]
faces1 = np.array([[0,2,1], # bottom
                   [0,3,2],
                   [4,0,5], # back
                   [5,0,1],
                   [6,5,1], # right side
                   [6,1,2], 
                   [7,6,2], # front 
                   [7,2,3],
                   [4,7,3], # left side
                   [4,3,0]], dtype=np.uint8)

# c)
def compute_boundary(faces):
    boundary_edges = []
    non_unique_edges = []
    edges = compute_edges(faces)
    for i in range(np.shape(edges)[0]):
        if(i not in non_unique_edges):
            is_unique = True # assume that the vertex is unique
            for j in range(i+1, np.shape(edges)[0]):
                if(edges[j,0] == edges[i,1] and edges[j,1] == edges[i,0]):
                    non_unique_edges.append(j)
                    is_unique = False
                    break
            if(is_unique == True):
                boundary_edges.append(i)
    return np.unique(edges[np.array(boundary_edges)].flatten())

print(compute_boundary(faces1))
            
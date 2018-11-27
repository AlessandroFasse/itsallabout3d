import numpy as np

# the faces of the other exercises for testing
faces1 = np.array([[0,2,1], # bottom
                  [0,3,2],
                  [4,0,5], # back
                  [5,0,1],
                  [6,5,1], # right side
                  [6,1,2], 
                  [7,6,2], # front 
                  [7,2,3],
                  [4,7,3], # left side
                  [7,3,0], 
                  [4,5,6], # top
                  [6,7,4]], dtype=np.uint8)

faces2 = np.array([[0,1,2],
                   [3,0,1],
                   [3,2,0],
                   [3,2,1]], dtype=np.uint8)

# c)
def compute_edges(faces):
    edges = np.zeros((3*np.shape(faces)[0], 2), dtype=np.uint8)
    for i in range(np.shape(faces)[0]):
        edges[3*i] = [faces[i,0], faces[i,1]]
        edges[3*i+1] = [faces[i,1], faces[i,2]]
        edges[3*i+2] = [faces[i,2], faces[i,0]]
    return edges

print(compute_edges(faces1))
print(compute_edges(faces2))

# c)
def compute_neighbors(faces):
    neighbors = [[] for i in range(np.max(faces)+1)]
    for i in range(np.shape(faces)[0]):
        for j in range(3): # for every vertex add the other ones of the face
            neighbors[faces[i,j]].append(faces[i,(j+1)%3])
            neighbors[faces[i,j]].append(faces[i,(j+2)%3])
    for i in range(len(neighbors)): # make the lists unique
        neighbors[i] = list(set(neighbors[i]))
    return neighbors

print(compute_neighbors(faces1))
print(compute_neighbors(faces2))
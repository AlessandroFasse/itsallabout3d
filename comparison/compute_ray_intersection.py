import numpy as np
import trimesh
import time 

mesh = trimesh.load("test.ply")

print("Number of faces = "+str(np.shape(mesh.faces)[0]))

origin = np.mean(mesh.vertices, axis=0)

mesh = trimesh.Trimesh(vertices=mesh.vertices - origin, faces=mesh.faces)

vector = np.array([1,0,0])
point = np.array([0,0,0])
distance = 10e100 

start = time.time()

for i in range(np.shape(mesh.faces)[0]):
    a = point - mesh.vertices[mesh.faces[i,0]]
    e1 = mesh.vertices[mesh.faces[i,1]] - mesh.vertices[mesh.faces[i,0]]
    e2 = mesh.vertices[mesh.faces[i,2]] - mesh.vertices[mesh.faces[i,0]]
    det = np.dot(np.cross(e1, e2), -1*vector)
    if(abs(det) >= 0.001):
        lambda0 = np.dot(np.cross(a, e2), -1*vector) / det
        if(lambda0 >= 0 and lambda0 <=1):
            lambda1 = np.dot(np.cross(e1, a), -1*vector) / det
            if(lambda1 >= 0 and lambda1 <= 1 and lambda0 + lambda1 <= 1):
                d = np.dot(np.cross(e1, e2), a) / det
                if(abs(d) < distance):
                    distance = abs(d)
                    result = point + d * vector

print("Finished in "+str(np.round(time.time() - start, 2))+" seconds")
print(result)
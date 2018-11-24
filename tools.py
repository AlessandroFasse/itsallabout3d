import numpy
import matplotlib.pyplot as plt

def print_2d_mesh(vertices, faces):
    plt.scatter(vertices[:, 0], vertices[:, 1])
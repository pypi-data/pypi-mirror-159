import numpy as np
import matplotlib.pyplot as plt
from plot_network import build_pos, plot_network

# Interaction matrix
A = np.array([[ 1, 1, 1],
              [-1,-1,-1],
              [ 1,-1, 1]])

# Node positions and names
pos = build_pos(A)
names = [f'G{i+1}' for i in range(A[0].size)]

# Figure
fig = plt.figure(figsize=(5,5))
ax = fig.gca()

# Draw the network
plot_network(A, pos, axes=ax, names=names, scale=2)

# Export the figure
fig.savefig('network.pdf', bbox_inches='tight')

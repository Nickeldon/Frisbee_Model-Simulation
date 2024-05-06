#Additional 3-D graph

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import math
from main import GetFrisbeeTraj

# Constants
x_0 = 0
y_0 = 1.0
v_0 = 12.0
g = 9.81
rho = 1.23
r = 0.135
A = math.pi * r**2
m = 0.175
DT = 0.01   # Time step
T_MAX = 5 # Max time of the simulation
STEPS = int(T_MAX/DT) # Number of steps in the simulation

# Function to compute the frisbee trajectory and return the range
def GetFrisbeeRange(theta, beta):
    # Assume the trajectory function has been correctly defined here.
    x, y = GetFrisbeeTraj(x_0, y_0, v_0, theta, beta, m, A, rho, STEPS)
    return x[-1]

# Grid of theta and beta values
theta_values = np.linspace(0, 90, 50)  # More points for smoother surface
beta_values = np.linspace(0, 10, 50)
theta, beta = np.meshgrid(theta_values, beta_values)

# Calculate range for each combination of theta and beta
Range = np.array([GetFrisbeeRange(t, b) for t, b in zip(np.ravel(theta), np.ravel(beta))])
Range = Range.reshape(theta.shape)

# Plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Surface plot
surf = ax.plot_surface(theta, beta, Range, cmap=cm.viridis, linewidth=0, antialiased=False, alpha=0.6)

# Highlight the maximum range
optimized_theta = 16.20
optimized_beta = 8.56
max_range = 20.51
ax.scatter([optimized_theta], [optimized_beta], [max_range], color='r', s=50, label=f"Optimized: Theta={optimized_theta}°, Beta={optimized_beta}°, Range={max_range:.2f}m")

# Labels and title
ax.set_xlabel('Theta (degrees)')
ax.set_ylabel('Beta (degrees)')
ax.set_zlabel('Range (meters)')
ax.set_title('3D Surface Plot of Frisbee Range vs. Theta and Beta')
ax.legend()

# Color bar
cbar = fig.colorbar(surf, shrink=0.5, aspect=5)
cbar.set_label('Range (meters)')

plt.show()
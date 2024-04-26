import math
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

# Constants
CD = 0.5
p = 1.225
A = 0.010
m = 0.40
g = 9.81  # Acceleration due to gravity in m/s^2
DT = 0.03   # Time step
T_MAX = 5.0 # Max time of the simulation
STEPS = int(T_MAX/DT) # Number of steps in the simulation

# Function calculating the trajectory of a launched projectile



# Initial Conditions
x_0 = 0 # Initial position in x in meters
y_0 = 10 # Initial position in y in meters
v_0 = 20 # Initial speed in m/s

# Create a set of launching angles to try out.
theta_0 = range(20,60,5) # Launch angle in degrees

def drag(CD, p, A, v_x, v_y):
  v = ((v_x**2) + (v_y**2))**(0.5)
  return ((0.5) * (CD * p * A * v * v_y)), ((0.5) * (CD * p * A * v * v_x))

def a_nodrag_y(CD, p, A, v_x, v_y, m):
  return (-drag(CD, p, A, v_x, v_y)[0] / m)

class motionEquations:
    def __init__(self, CD, p, A, m, g):
        self.CD = CD
        self.p = p
        self.A = A
        self.m = m
        self.g = g
    
    def drag(self, v_x, v_y):
        v = ((v_x**2) + (v_y**2))**(0.5)
        return ((0.5) * (self.CD * self.p * self.A * v * v_y)), ((0.5) * (self.CD * self.p * self.A * v * v_x))

    def a_nodrag_y(self, v_x, v_y):
        return (-self.drag(v_x, v_y)[0] / self.m)
    
    def newton_2nd_law(self, v_x, v_y):
        return self.drag(v_x, v_y)[1] / self.m

"""
# VX AND AX NEVER CHANGE
def a_nodrag_x(CD, p, A, v_x, v_y, m):
  return (-drag(CD, p, A, v_x, v_y)[1] / m)"""

def GetFrisbeeTraj(x_0,y_0,v_0, theta_0):

  x = [x_0]
  y = [y_0]

  vx = v_0 * math.cos(math.radians(theta_0))
  vy = v_0 * math.sin(math.radians(theta_0))

  for i in range(STEPS):
    ay = a_nodrag_y(CD, p, A, vx, vy, m)
    
    vy += DT* ay

    #Calculating position in x
    x.append(x[i] + DT* vx)

    #Calculating position in y
    y.append(y[i] + DT* vy)

    if y[i] <= 0:
      break
  return x, y

# For loop on the launching angle

prevHigh = [0, 0]


rho = 1.23            # air density in kg/m^3
r = 0.135             # radius in m
m = 0.175             # mass in kg
x_0 = 0               # initial horizontal position in m
y_0 = 1.0             # initial vertical position in m
g = 9.81              # acceleration due to gravity in m/s^2
v_0 = 12.0            # initial speed in m/s




for angle in theta_0:
  # Calculate the trajectory for each launching angle and add to plot
  x,y = GetFrisbeeTraj(x_0,y_0,v_0,angle)
  if(x[len(x) - 1] > prevHigh[1]):
    prevHigh[0] = angle
    prevHigh[1] = x[len(x) - 1]
  plt.plot(x,y,label = f"{angle}\N{DEGREE SIGN} - Range={x[-1]:.1f}m")
plt.legend()
plt.title("Effect of (theta0, B) on trajectory of a Frisbee for an initial speed of 12 m/s")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.show()
print(f'The highest range in the x axis is equal to {prevHigh[1]:.1f}m with an angle of {prevHigh[0]}°')

import math
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

def getCD(theta):
  return 0.085 + 3.30 * (theta - (-0.052))**2

def getCL(theta):
  return 0.13 + (3.09 * theta)

class AerodynamicForces:
    def __init__(self, v_x, v_y, theta):
        self.theta = theta
        self.CD = getCD(self.theta)
        self.CL = getCL(self.theta)
        self.v_x = v_x
        self.v_y = v_y
        self.v = math.sqrt(self.v_x**2 + self.v_y**2)
    
    def lift(self):
      print(self.CL, self.CD)
      return {
          'y': 0.5 * self.CL * rho * A * math.cos(math.radians(self.theta)) * (self.v**2),
          'x': 0.5 * self.CL * rho * A * math.sin(math.radians(self.theta)) * (self.v**2)}

    def drag(self):
      print(self.CL, self.CD)
      return {
          'y': 0.5 * self.CD * rho * A * math.sin(math.radians(self.theta)) * (self.v**2),
          'x': 0.5 * self.CD * rho * A * math.cos(math.radians(self.theta)) * (self.v**2)}

# Constants
g = 9.81  # Acceleration due to gravity in m/s^2
DT = 0.03   # Time step
T_MAX = 1.0 # Max time of the simulation
STEPS = int(T_MAX/DT) # Number of steps in the simulation
rho = 1.23            # air density in kg/m^3
r = 0.135
A = math.pi * r**2# radius in m
m = 0.175             # mass in kg
x_0 = 0               # initial horizontal position in m
y_0 = 1.0             # initial vertical position in m
v_0 = 12.0            # initial speed in m/s


# Create a set of launching angles to try out.
theta_0 = range(0,20,5) # Launch angle in degrees

def getAcc(v_x, v_y, m, theta):
  AEFORCES = AerodynamicForces(v_x, v_y, theta)
  Ay = (1 / m) * (-m*g + AEFORCES.lift()['y'] - AEFORCES.drag()['y'])
  Ax = (1 / m) * (AEFORCES.lift()['x'] - AEFORCES.drag()['x'])
  return [Ax,  Ay]


def GetFrisbeeTraj(x_0,y_0,v_0, theta_0):

  x = [x_0]
  y = [y_0]

  vx = [v_0 * math.cos(math.radians(theta_0))]
  vy = [v_0 * math.sin(math.radians(theta_0))]

  for i in range(STEPS):
    #print(vx[i], vy[i])
    Accelerations = getAcc(vx[i], vy[i], m, theta_0)
    
    ay = Accelerations[1]
    ax = Accelerations[0]
    
    vy.append(vy[i] + DT * ay)
    vx.append(vx[i] + DT * ax)
    
    
    #Calculating position in x
    x.append(x[i] + DT* vx[i])

    #Calculating position in y
    y.append(y[i] + DT* vy[i])

    
    if y[i] <= 0:
      print("Hit the ground")
      break
  return x, y

# For loop on the launching angle

prevHigh = [0, 0]


print(theta_0)
# Calculate the trajectory for each launching angle and add to plot
for angle in theta_0:
  x,y = GetFrisbeeTraj(x_0,y_0,v_0,angle)
  if(x[len(x) - 1] > prevHigh[1]):
    prevHigh[0] = angle
    prevHigh[1] = x[len(x) - 1]
  plt.plot(x,y,label = f"{10}\N{DEGREE SIGN} - Range={x[-1]:.1f}m")
plt.legend()
plt.title("Effect of (theta0, B) on trajectory of a Frisbee for an initial speed of 12 m/s")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.show()
print(f'The highest range in the x axis is equal to {prevHigh[1]:.1f}m with an angle of {prevHigh[0]}°')

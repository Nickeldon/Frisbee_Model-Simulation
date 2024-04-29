import math
import matplotlib.pyplot as plt


def getCD(alpha):
  return 0.085 + 3.30 * (math.radians(alpha) - (-0.052))**2

def getCL(alpha):
  return 0.13 + (3.09 * math.radians(alpha))

class AerodynamicForces:
	def __init__(self, v_x, v_y, theta, beta):
		self.theta = theta
		self.beta = beta
		self.alpha = self.beta - self.theta*(180/math.pi)
		self.CD = getCD(self.alpha)
		self.CL = getCL(self.alpha)
		self.v_x = v_x
		self.v_y = v_y
		self.v = math.sqrt(self.v_x**2 + self.v_y**2)
		
	def lift(self, v_x, v_y):
		self.v_x = v_x
		self.v_y = v_y
		return {
		'y': 0.5 * self.CL * rho * A * (self.v)**2,
		'x': 0.5 * self.CL * rho * A * (self.v)**2}

	def drag(self, v_x, v_y):
		self.v_x = v_x
		self.v_y = v_y
		return {
		'y': 0.5 * self.CD * rho * A * (self.v)**2,
		'x': 0.5 * self.CD * rho * A * (self.v)**2}

# Constants
g = 9.81  # Acceleration due to gravity in m/s^2
DT = 0.01   # Time step
T_MAX = 5.0 # Max time of the simulation
STEPS = int(T_MAX/DT) # Number of steps in the simulation
rho = 1.23            # air density in kg/m^3
r = 0.135
A = math.pi * r**2
m = 0.175             # mass in kg
x_0 = 0               # initial horizontal position in m
y_0 = 1.0             # initial vertical position in m
v_0 = 12.0            # initial speed in m/s


# Create a set of launching angles to try out.
theta_0 = range(0, 20, 5) # Launch angle in degrees

def getAcc(v_x, v_y, m, beta):
	theta = math.atan(v_y/v_x)
	#print(theta*180/math.pi)
	AEFORCES = AerodynamicForces(v_x, v_y, theta, beta)
	Ay = (1 / m) * (-m*g + AEFORCES.lift(v_x, v_y)['y']*math.cos(theta) - AEFORCES.drag(v_x, v_y)['y']*math.sin(theta))
	Ax = (1 / m) * (-AEFORCES.lift(v_x, v_y)['x']*math.sin(theta) - AEFORCES.drag(v_x, v_y)['x']*math.cos(theta))
	return [Ax,  Ay]


def GetFrisbeeTraj(x_0,y_0,v_0, theta_0, beta):
    vx_0 = v_0 * math.cos(math.radians(theta_0))
    vy_0 = v_0 * math.sin(math.radians(theta_0))

    x = [x_0]
    y = [y_0]
    vx = [vx_0]
    vy = [vy_0]
    
    acceleration = getAcc(vx[0], vy[0], m, beta)
    
    ax = [acceleration[0]]
    ay = [acceleration[1]]

    for i in range(0, STEPS):
        x.append(x[i] + vx[i] * DT)
        y.append(y[i] + vy[i] * DT)

        vx.append(vx[i] + ax[i]*DT)
        vy.append(vy[i] + ay[i]*DT)
        
        ax.append(getAcc(vx[-1], vy[-1], m, beta)[0])
        ay.append(getAcc(vx[-1], vy[-1], m, beta)[1])

        if y[-1] <= 0:
            break

    return x, y

# For loop on the launching angle

prevHigh = [0, 0]

# Calculate the trajectory for each launching angle and add to plot
plt.rcParams['figure.figsize'] = (10, 4)

for angle in theta_0:
  x,y = GetFrisbeeTraj(x_0,y_0,v_0,angle, 10)
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

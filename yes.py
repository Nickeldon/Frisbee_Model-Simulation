from main import Frisbee
import math

g = 9.81  # Acceleration due to gravity in m/s^2
DT = 0.01   # Time step
T_MAX = 5 # Max time of the simulation
STEPS = int(T_MAX/DT) # Number of steps in the simulation
rho = 1.23            # air density in kg/m^3
r = 0.135
A = math.pi * r**2
m = 0.175          # mass in kg
x_0 = 0               # initial horizontal position in m
y_0 = 1.0             # initial vertical position in m
v_0 = 12.0            # initial speed in m/s

#Frisbee.get_trajectory([10, 20, 30, 40, 50], [0, 0, 0, 0, 0], 12, 1.0, 0, 0.175, 0.135, 1.23, 500, True, [], [], [], True)

Frisbee.optimize()
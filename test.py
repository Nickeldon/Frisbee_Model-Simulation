from main import *

def run_test():
    # Constants
    g = 9.8  # Acceleration due to gravity in m/s^2
    DT = 0.01   # Time step
    T_MAX = 12.3 # Max time of the simulation
    STEPS = int(T_MAX/DT) # Number of steps in the simulation
    rho = 1.2041            # air density in kg/m^3
    r = 0.27305/2
    A = math.pi * r**2
    m = 0.2455          # mass in kg
    x_0 = 0               # initial horizontal position in m
    y_0 = 1.0             # initial vertical position in m
    v_0 = 22.0            # initial speed in m/s
    
    theta_0 = [2]
    beta_0 = [11]
    # For loop on the launching angle

    prevHigh = [0, 0]

    # Calculate the trajectory for each launching angle and add to plot
    plt.rcParams['figure.figsize'] = (1	, 4)
    plt.figure(figsize=(13, 4))
    plt.yticks(np.arange(0, 4, 1))
    plt.xticks(np.arange(-1, 22, 2.5))
    plt.xlim(-1, 22)
    plt.ylim(0, 4)

    for index, angle in enumerate(theta_0):
        x,y = GetFrisbeeTraj(x_0,y_0,v_0,angle, beta_0[index], m, A, rho, STEPS)
    if(x[len(x) - 1] > prevHigh[1]):
        prevHigh[0] = angle
        prevHigh[1] = x[len(x) - 1]
    plt.plot(x,y,label = f"({angle}\N{DEGREE SIGN}, {beta_0[index]}\N{DEGREE SIGN})  - Range={x[-1]:.1f}m")
    plt.legend()
    plt.title("Effect of (\u03B8\u2080, \u03B2) on trajectory of a Frisbee for an initial speed of 12 m/s")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.show()
    print(f'The highest range in the x axis is equal to {prevHigh[1]:.1f}m with an angle of {prevHigh[0]}°')

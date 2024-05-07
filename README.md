# Frisbee_Model-Simulation

## Contributors
- [Nickeldon](https://github.com/Nickeldon)
- [tigersh4rk](https://github.com/tigersh4rk)

## Description
This repository contains a Frisbee trajectory simulator created using Jupyter Notebook and Python. The simulator follows physical principles to model the trajectory of a Frisbee under various conditions.

## How to Run
1. Ensure you have Python 3 or higher installed on your system.
2. Clone this repository to your local machine.
```
git clone https://github.com/Nickeldon/Frisbee_Model-Simulation.git
```
4. Navigate to the directory where you cloned the repository.
```
cd Frisbee_Model-Simulation
```
5. Installed the required libraries
```
pip install matplotlib
pip install numpy
```
- [If possible]
```
pip install scipy
```
6. To visualize an example, run the `test.py` script using the following command:
    ```
    python test.py
    ```

## Example
### Based on the experimentation processed in [this article by Erynn J. Schroeder](https://digitalcommons.csbsju.edu/cgi/viewcontent.cgi?article=1067&context=honors_theses)
```python
# test.py

from main import *

def run_test():
    # Constants
    g = 9.8  # Acceleration due to gravity in m/s^2
    DT = 0.01             # Time step
    T_MAX = 12.3          # Max time of the simulation
    STEPS = int(T_MAX/DT) # Number of steps in the simulation
    rho = 1.2041          # air density in kg/m^3
    r = 0.27305/2         # Radius of cross section of frisbee
    A = math.pi * r**2    # Cross section area of Frisbee
    m = 0.2455            # mass in kg
    x_0 = 0               # initial horizontal position in m
    y_0 = 1.0             # initial vertical position in m
    v_0 = 22.0            # initial speed in m/s
    
    theta_0 = [2]         # Initial throwing angle
    beta_0 = [11]         # Initial angle of attack
    # For loop on the launching angle

    prevHigh = [0, 0]     # History array to find maximum range of the frisbee

    # Calculate the trajectory for each launching angle and add to plot
    plt.rcParams['figure.figsize'] = (1	, 4)
    plt.figure(figsize=(13, 4))
    plt.yticks(np.arange(0, 6, 1))
    plt.xticks(np.arange(-1, 533, 2.5))
    plt.xlim(-1, 53)
    plt.ylim(0, 6)

    for index, angle in enumerate(theta_0):
        x,y = GetFrisbeeTraj(x_0,y_0,v_0,angle, beta_0[index], m, A, rho, STEPS)
    if(x[len(x) - 1] > prevHigh[1]):
        prevHigh[0] = angle
        prevHigh[1] = x[len(x) - 1]
    plt.plot(x,y,label = f"({angle}°, {beta_0[index]}°)  - Range={x[-1]:.1f}m")
    plt.legend()
    plt.title("Effect of (θ₀, β) on trajectory of a Frisbee for an initial speed of 12 m/s")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.show()
    print(f'The highest range in the x axis is equal to {prevHigh[1]:.1f}m with an angle of {prevHigh[0]}°')

run_test()

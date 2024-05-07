from trajectory_compiler import GetFrisbeeTraj

#optimization code

import matplotlib.pyplot as plt
import math

class optimize:
    def __init__(self) -> None:
        pass
        
    """g = 9.81  # Acceleration due to gravity in m/s^2
    DT = 0.01   # Time step
    T_MAX = 5 # Max time of the simulation
    STEPS = int(T_MAX/DT) # Number of steps in the simulation
    rho = 1.23            # air density in kg/m^3
    r = 0.135
    A = math.pi * r**2
    m = 0.175          # mass in kg"""

    # Define a function to perform the golden section search, a method for finding the minimum or maximum of a function
    def golden_section_search(f, a, b, tol=1e-5):
        # Define the golden ratio
        phi = (1 + math.sqrt(5)) / 2
        # Calculate c and d based on the golden ratio
        c = b - (b - a) / phi
        d = a + (b - a) / phi
        # Continue adjusting a and b until the desired precision is achieved
        while abs(c - d) > tol:
            # Compare function values at c and d and adjust the search interval
            if f(c) < f(d):
                b = d
            else:
                a = c
            c = b - (b - a) / phi
            d = a + (b - a) / phi
        # Return the midpoint of the final interval as the best estimate of the extremum
        result = (b + a) / 2
        return result

    # Function to perform a two-dimensional golden section search
    def two_dim_gss(self, x_0, y_0, v_0, m, A, rho, STEPS, theta_range, beta_range, tol=1e-5):
        # Define the objective function which returns the negative of the last x position of the frisbee trajectory
        def objective(theta, beta):
            x, y = GetFrisbeeTraj(x_0, y_0, v_0, theta, beta, m, A, rho, STEPS)
            return -x[-1]

        # Initialize the best estimates for theta and beta
        best_theta, best_beta = (theta_range[0] + theta_range[1]) / 2, (beta_range[0] + beta_range[1]) / 2
        for _ in range(100):  # Perform a maximum of 100 iterations
            # Optimize theta by fixing beta
            new_theta = self.golden_section_search(lambda theta: objective(theta, best_beta), theta_range[0], theta_range[1], tol)
            print(f"The result of the one-dimensional golden section search for theta is: Theta = {new_theta:.2f}")

            # Optimize beta by fixing theta
            new_beta = self.golden_section_search(lambda beta: objective(new_theta, beta), beta_range[0], beta_range[1], tol)
            print(f"The result of the one-dimensional golden section search for beta is: Beta = {new_beta:.2f}")

            # Break if the changes are below the tolerance
            if abs(new_theta - best_theta) < tol and abs(new_beta - best_beta) < tol:
                break
            best_theta, best_beta = new_theta, new_beta

        return best_theta, best_beta

    """# Constants for the simulation
    x_0 = 0  # Initial horizontal position
    y_0 = 1.0  # Initial vertical position
    v_0 = 12.0  # Initial velocity
    theta_range = (0, 90)  # Range of theta values to explore
    beta_range = (0, 90)  # Range of beta values to explore"""

    def show_optimized_trajectory(self, x_0, y_0, v_0, m, A, rho, STEPS, theta_range, beta_range):
        # Perform the optimization to find the optimal theta and beta (2D)
        optimized_theta, optimized_beta = self.two_dim_gss(theta_range, beta_range)
        # Compute the frisbee trajectory using the optimized theta and beta
        x, y = GetFrisbeeTraj(x_0, y_0, v_0, optimized_theta, optimized_beta,m, A, rho, STEPS)

        # Plot the optimized trajectory
        plt.figure(figsize=(10, 5))
        plt.plot(x, y, label=f"Optimal launch: Theta={optimized_theta:.2f}°, Beta={optimized_beta:.2f}°")
        plt.title("Optimized Frisbee Trajectory")
        plt.xlabel("Distance (m)")
        plt.ylabel("Height (m)")
        plt.legend()
        plt.grid(True)
        plt.show()

        # Print the final result of the two-dimensional search
        print(f"The result of the two-dimensional golden section search is: Theta = {optimized_theta:.2f}°, Beta = {optimized_beta:.2f}°")
        print(f"The maximum range with optimized angles is {x[-1]:.2f}m.")
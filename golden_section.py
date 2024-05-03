import numpy as np
import math
import matplotlib.pyplot as plt
import time

# use R as the distance between the Sun and the Earth in meters
G = 6.67e-11
MS = 2e30
ME = 6e24
R = 1.5e11

# Initial brackets: It's between these two points
r1 = 5e8
r2 = 5e9


# define your effective potential function
def VL1(r):
    return -(G * MS * (R - r) ** 2) / (2 * R ** 3) - (G * MS) / (abs(R - r)) - (G * ME) / (abs(r))


def golden_section(f, x1, x2, **kwargs):
    start_time = time.time()

    # Setting the max number of steps and the accuracy
    NSTEPS = kwargs.get("NSTEPS", 1000)
    ACCURACY = kwargs.get("ACCURACY", 1e-2)

    # Defining the constants for the ratios with gr1 < gr2
    gr2 = 2 / (1 + math.sqrt(5))
    gr1 = 1.0 - gr2

    x3 = x1 + (x2 - x1) * gr1
    x4 = x1 + (x2 - x1) * gr2
    f3 = f(x3)
    f4 = f(x4)

    # TASK B.1: Modify your trisection search code to do a Golden Section search instead.

    for i in range(NSTEPS):

        if (x2 - x1) / ((x1 + x2) / 2) < ACCURACY:
            break

        if f(x3) > f(x4):
            x2 = x4
            x4 = x3
            f4 = f3
            x3 = x1 + (x2 - x1) * gr1
            f3 = f(x3)
        else:
            x1 = x3
            x3 = x4
            f3 = f4
            x4 = x1 + (x2 - x1) * gr2
            f4 = f(x4)

    print(f"Found the maximum at {(x1 + x2) / 2} in {(time.time() - start_time):.14f} seconds after {i} steps")
    return (x1 + x2) / 2, f((x1 + x2) / 2)


# Using Golden Section Search
# Using the negative of the effective potential to search for a minimum
# Positive r gives Lagrange point L1, often used for solar telescopes
# Use an accuracy of 1e-8
r_max_L1, V_max_L1 = golden_section(VL1, r1, r2, ACCURACY=1e-8)
print(f"Lagrange point L1 is located at {r_max_L1:.8g} m with {V_max_L1} N")

# Note: you can also use a negative r to give the Lagrange point L2 (James Webb Space Telescope)
r_max_L2, V_max_L2 = golden_section(VL1, -r1, -r2, ACCURACY=1e-8)
print(f"Lagrange point L2 is located at {r_max_L2:.8g} m")

"""
# Plot it
r_array = np.linspace(-r2, r2, 300)
f_array = [VL1(x) for x in r_array]
plt.plot(r_array, f_array)
plt.xlabel("r")
plt.ylabel("Veff(r)")
plt.plot(r_max_L1, V_max_L1, marker = "*")
plt.text(r_max_L1, V_max_L1, "L1")
plt.plot(r_max_L2, V_max_L2, marker = "*")
plt.text(r_max_L1, V_max_L1, f"L1, {r_max_L1:.3g} m")
plt.text(r_max_L2, V_max_L2, f"L2, {r_max_L2:.4g} m")
plt.annotate("The L2 is situated 1.51e+9 m from Earth\naway from the sun",(-5e+09, -1.355e+09), color = "black", size = "12")
# plt.ylim(-1.34e9,-1.33e9)
plt.show()"""
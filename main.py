from _3D_visulizer import _3d_plotter
import numpy as np
from optimizer import optimize
from trajectory_compiler import GetFrisbeeTraj

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("The matplotlib module is not installed. \nPlease install it using 'pip install matplotlib'!")
class Frisbee:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def optimize(theta_range, beta_range, g, DT, T_MAX, STEPS, rho, r, A, m, x_0, y_0, v_0):
        return optimize(g, DT, T_MAX, STEPS, rho, r, A, m, x_0, y_0, v_0, theta_range, beta_range)
    
    @staticmethod
    def plot_3d(x_0, y_0, v_0, g, rho, r, A, m, DT, T_MAX, STEPS):
        return _3d_plotter(x_0, y_0, v_0, g, rho, r, A, m, DT, T_MAX, STEPS)        

    @staticmethod
    def get_trajectory(theta_0, beta_0, v_0, y_0, x_0, m, A, rho, STEPS, print_results = True, graphDim = [], max_coord = [], min_coord = [], show_graph = True):
        if isinstance(theta_0, list) and isinstance(beta_0, list):
            if len(theta_0) != len(beta_0):
                raise ValueError("The number of elements in theta_0 and beta_0 must be equal.")
        else:
            raise ValueError("theta_0 and beta_0 must be lists.")
        
        prevHigh = [0, 0, 0]
        prevMin = [0, 0, 0]
        trajectory_data = []

        for index, angle in enumerate(theta_0):
            x, y = GetFrisbeeTraj(x_0, y_0, v_0, angle, beta_0[index], m, A, rho, STEPS)
            trajectory_data.append((x, y))
            if abs(x[-1]) > prevHigh[1]:
                prevHigh[0] = angle
                prevHigh[1] = abs(x[-1])
            if abs(y[-1]) > prevHigh[2]:
                prevHigh[2] = abs(y[-1])
        
            if abs(x[-1]) < prevMin[1]:
                prevMin[0] = angle
                prevMin[1] = abs(x[-1])
            if abs(y[-1]) < prevMin[2]:
                prevMin[2] = abs(y[-1])

        if print_results:
            print('-----------------------------------------------------------------------------------------------------------------')
            print(f'\nThe Frisbee was launched at an initial speed of {v_0}m/s from a height of {y_0}m at a distance of {x_0}m from the origin.')
            print(f'The mass of the Frisbee is {m}kg with a cross-sectional area of {A}m² and a density of {rho}kg/m³.')
            print(f'The highest range in the x axis is equal to {prevHigh[1]:.1f}m with an angle of {prevHigh[0]}°')
            print(f'The highest height in the y axis is equal to {prevHigh[2]:.1f}m with an angle of {prevHigh[0]}°\n')
            print('---------------------------------------------------------------------------------------------------------------------')

        if show_graph:
            coord_size_x = [0, 0]
            coord_size_y = [0, 0]
            size_x = 0
            size_y = 0
            if len(max_coord) == 0 or len(min_coord) == 0:
                print("No max coordinate values provided. Using auto dimensions.")
                coord_size_x[1] = prevHigh[1] + 5
                coord_size_x[0] = prevMin[1] - 5
                coord_size_y[1] = prevHigh[2] + 2
                coord_size_y[0] = prevMin[2]
            elif len(min_coord) > 1 and len(max_coord) > 1:
                coord_size_x[1] = max_coord[0]
                coord_size_x[0] = min_coord[0]
                coord_size_y[1] = max_coord[1]
                coord_size_y[0] = min_coord[1]
            else:
                raise ValueError("Both max and min coordinates must be provided.")
            
            if(len(graphDim) == 0):
                print("No graph dimensions provided. Using auto dimensions.")
                if prevHigh[1] < 1:
                    size_x = prevHigh[1] * (1 / prevHigh[1]) * 5
                else:
                    size_x = prevHigh[1] * 0.7

                if prevHigh[2] < 1:
                    size_y = prevHigh[2] * (1 / prevHigh[2]) * 5
                else:
                    size_y = prevHigh[2]
            else:
                size_x = graphDim[0]
                size_y = graphDim[1]
            
            plt.rcParams['figure.figsize'] = (size_x, size_y)
            plt.figure(figsize=(size_x, size_y))
            plt.yticks(np.arange(coord_size_y[0], coord_size_y[1], 1))
            plt.xticks(np.arange(coord_size_x[0], coord_size_x[1], 2.5))
            plt.xlim(coord_size_x[0], coord_size_x[1])
            plt.ylim(coord_size_y[0], coord_size_y[1])

            for index, (x, y) in enumerate(trajectory_data):
                plt.plot(x, y, label=f"({theta_0[index]}\N{DEGREE SIGN}, {beta_0[index]}\N{DEGREE SIGN})  - Range={x[-1]:.1f}m")

            plt.legend()
            plt.title("Effect of (\u03B8\u2080, \u03B2) on trajectory of a Frisbee for an initial speed of 12 m/s")
            plt.xlabel("Distance (m)")
            plt.ylabel("Height (m)")
            plt.show()        
            
        return trajectory_data
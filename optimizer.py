from "./golden_section.py" import golden_section

max_beta, min_beta = [0, 90]

max_theta, min_theta = [0, 90]

theta_increm, beta_incream = [5, 2.5]

def Optimizer(angles, increms, mass):
    theta = angles[0]
    beta = angles[1]

    theta_inc = increms[0]
    beta_inc = increms[1]
    print("This seems to work")
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

# Define the transfer function of your system (ball on a beam)
def system(t, y, Kp, Ki, Kd):
    A = 1.0  # Your constant A
    dydt = [y[1], A - Kd * y[1] - Kp * y[0] - Ki * np.trapz(y)]
    return dydt

# Define the desired response (change this as needed)
def desired_response(t):
    return np.sin(t)

# Define the error function to minimize
def error(params):
    Kp, Ki, Kd = params
    sol = solve_ivp(lambda t, y: system(t, y, Kp, Ki, Kd), [0, 10], [0, 0], t_eval=np.linspace(0, 10, 100))
    actual_response = sol.y[0]
    return np.mean((desired_response(sol.t) - actual_response) ** 2)

# Initial guess for PID parameters
initial_params = [1.0, 0.1, 0.01]

# Minimize the error to find the best PID parameters
result = minimize(error, initial_params, method='Nelder-Mead')

# Extract the best PID parameters
best_params = result.x

# Print the best PID parameters
print(f"Best Kp: {best_params[0]}")
print(f"Best Ki: {best_params[1]}")
print(f"Best Kd: {best_params[2]}")

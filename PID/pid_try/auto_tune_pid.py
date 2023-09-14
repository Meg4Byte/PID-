import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
from scipy.signal import lti

# Define the plant transfer function G(s) = A/s^2
A = 0.2
numerator = [A]
denominator = [1, 0, 0]
plant = ctrl.TransferFunction(numerator, denominator)

# Time vector
time = np.linspace(0, 70, 1000)

"""
        lets see 
        Kp = 0.6, Ki = 0.027069704489059328, Kd = 3.32475
        Kp_nos = 0.2, Ki_nos = 0.009023234829686443, Kd_nos = 2.92578

"""


# Create an initial PID controller with default parameters
Kp_init = 0.2
Ki_init = 0
Kd_init = 10
pid_tf = ctrl.TransferFunction([Kd_init, Kp_init, Ki_init], [1, 0])

# Create a closed-loop system by connecting the PID controller to the plant
closed_loop = ctrl.feedback(pid_tf * plant, 1)

# Simulate the response to a step input
time, response = ctrl.step_response(closed_loop, time)

# Plot the response
plt.plot(time, response)
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('PID Step Response')
plt.grid()
plt.show()

import control as ctrl
import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, FloatSlider

# Initialize PID parameters
Kp = 1.0
Ki = 0.2
Kd = 0.1

# Create a PID transfer function
numerator = [Kd, Kp, Ki]
denominator = [1, 0]
pid_tf = ctrl.TransferFunction(numerator, denominator)

# Initialize time vector and response
time = np.arange(0, 100, 0.001)
response = np.zeros_like(time)

# Define the PID control function
def pid_control(Kp, Ki, Kd):
    # Update the PID transfer function with new parameters
    numerator = [Kd, Kp, Ki]
    pid_tf.num, pid_tf.den = numerator, [1, 0]
    
    # Simulate the PID response to a step input
    time, response = ctrl.step_response(pid_tf, time)
    
    # Plot the response
    plt.figure(figsize=(10, 6))
    plt.plot(time, response)
    plt.xlabel('Time (s)')
    plt.ylabel('Response')
    plt.title('PID Step Response')
    plt.grid()
    plt.show()

# Create interactive sliders for PID parameters
Kp_slider = FloatSlider(value=Kp, min=0.1, max=2.0, step=0.1, description='Kp')
Ki_slider = FloatSlider(value=Ki, min=0.1, max=2.0, step=0.1, description='Ki')
Kd_slider = FloatSlider(value=Kd, min=0.1, max=2.0, step=0.1, description='Kd')

# Create an interactive widget
interact(pid_control, Kp=Kp_slider, Ki=Ki_slider, Kd=Kd_slider)

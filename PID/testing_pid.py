import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
from scipy.signal import lti
import ipywidgets as widgets
from ipywidgets import interact

# Create an initial PID controller with default parameters


Kp_default = 10.0
Ki_default = 0.20
Kd_default = 10.0


pid = ctrl.TransferFunction([Kd_default, Kp_default, Ki_default], [1, 0])
system = ctrl.TransferFunction([1], [1, 1, 1])

# Create a time vector
time = np.linspace(0, 10, 1000)

def update_pid(Kp, Ki, Kd):
    global pid
    pid = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])
    t, y = ctrl.step_response(pid * system, time)
    plt.figure(figsize=(10, 5))
    plt.plot(t, y)
    plt.xlabel('Time')
    plt.ylabel('Response')
    plt.title('PID Step Response')
    plt.grid(True)
    plt.show()


Kp_slider = widgets.FloatSlider(value=Kp_default, min=0.1, max=2.0, step=0.1, description='Kp:')
Ki_slider = widgets.FloatSlider(value=Ki_default, min=0.1, max=2.0, step=0.1, description='Ki:')
Kd_slider = widgets.FloatSlider(value=Kd_default, min=0.1, max=2.0, step=0.1, description='Kd:')

interact(update_pid, Kp=Kp_slider, Ki=Ki_slider, Kd=Kd_slider)

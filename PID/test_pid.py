import control as ctrl
import matplotlib.pyplot as plt
import numpy as np


# Define the Transfer Function for Your New System
new_numerator = [1]  # Modify with your own coefficients
new_denominator = [1, 2]  # Modify with your own coefficients
new_tf = ctrl.TransferFunction(new_numerator, new_denominator)

# PID parameters (you can adjust these as needed)
Kp = 100.0
Ki = 10.2
Kd = 20.1

# Create a PID transfer function
numerator = [Kd, Kp, Ki]
denominator = [1, 0]
pid_tf = ctrl.TransferFunction(numerator, denominator)

# Time vector
#time = ctrl.timebase(0, 10, 0.01)  # Start, end, step
time = np.arange(0, 50, 0.001)
# Simulate the PID response to a step input for the new system
time, response = ctrl.step_response(pid_tf * new_tf, time)

time , old_tf = ctrl.step_response(new_tf, time)


# Create a subplot grid
plt.figure(figsize=(10, 6))

# First subplot (PID response)
plt.subplot(2, 1, 1)  # 2 rows, 1 column, first subplot
plt.plot(time, response)
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('PID Step Response')
plt.grid()

# Second subplot (Other data)
plt.subplot(2, 1, 2)  # 2 rows, 1 column, second subplot
plt.plot(time, old_tf)
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Transfer Function')
plt.grid()

# Adjust layout for better spacing
plt.tight_layout()

# Adjust spacing between subplots
plt.subplots_adjust(hspace=0.6)

plt.show()

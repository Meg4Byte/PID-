import control
import numpy as np

# Step 1: Define the Plant Transfer Function
num = [1]  # numerator coefficients
den = [1, 2, 1]  # denominator coefficients
plant_tf = control.TransferFunction(num, den)

# Step 2: Find Critical Period and Amplitude
def measure_oscillations(kp, ki, kd):
    controller_tf = control.TransferFunction([kd, kp, ki], [1, 0])
    sys_cl = control.feedback(controller_tf * plant_tf)

    t = np.linspace(0, 50, 1000)
    _, y = control.step_response(sys_cl, T=t)

    peaks, _ = control.find_peaks(y)
    period = np.mean(np.diff(peaks))

    return period, np.max(y)

kp = 0.1
ki = 0.01
kd = 0.05

period, amplitude = measure_oscillations(kp, ki, kd)
Tc = period
Ac = amplitude

# Step 3: Calculate PID Gains using Ziegler-Nichols Method
Kp = 0.6 * Ac / Tc
Ki = 1.2 * Ac / (Tc**2)
Kd = 0.075 * Ac * Tc

# Step 4: Create PID Controller
controller_tf = control.TransferFunction([Kd, Kp, Ki], [1, 0])

# Step 5: Combine Plant and Controller
sys_cl = control.feedback(controller_tf * plant_tf)

# Step 6: Simulate Step Response
t = np.linspace(0, 10, 100)
t, y = control.step_response(sys_cl, T=t)

# Plotting the Step Response
import matplotlib.pyplot as plt

plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response with Ziegler-Nichols Tuning')
plt.grid(True)
plt.show()

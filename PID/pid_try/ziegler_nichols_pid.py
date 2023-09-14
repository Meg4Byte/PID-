import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the plant transfer function G(s) = A/s^2

A = 0.2
numerator = [A]
denominator = [1, 0, 0]
plant = ctrl.TransferFunction(numerator, denominator)

time = np.linspace(0, 20, 1000)
u = np.ones(len(time))



_, open_loop_response = ctrl.step_response(plant, time)

# Plot the open-loop response to determine the ultimate gain (Ku)

plt.plot(time, open_loop_response)
plt.xlabel('Time (s)')
plt.ylabel('Open-Loop Response')
plt.title('Open-Loop Step Response')
plt.grid()
plt.show()

        # Identify the time period (Pu) and amplitude of oscillation (Au)
        # from the plot of open-loop response

Pu = 66  
Au = 2  
n = 2           # Number of oscillations (needs to be tuned)


# Calculate the ultimate gain (Ku) using Pu and Au
Ku = 4 / (n * Au)


            #Ideal PID parameters
            
Kp = 0.6 * Ku
Ki = 1.2 * Ku / Pu
Kd = 0.075 * Ku * Pu


#no overshoot paramerters
Kp_nos =  0.2 * Ku
Ki_nos =  0.4 * Ku / Pu
Kd_nos =  0.066 * Ku * Pu

# Create a PID controller with the calculated parameters
pid_tf = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])
pid_no_os = ctrl.TransferFunction([Kd_nos, Kp_nos, Ki_nos], [1, 0])


closed_loop = ctrl.feedback(pid_tf * plant, 1)
closer_loop_no_os = ctrl.feedback(pid_no_os * plant, 1)

# Simulate the response to a step input
time, response = ctrl.step_response(closed_loop, time)
time, response_no_os = ctrl.step_response(closer_loop_no_os, time)

# Plot 

plt.subplot(1,1,1)
plt.plot(time, response)
plt.xlabel('Time (s)')
plt.ylabel('Closed-Loop Response')
plt.title('Closed-Loop Step Response with Ziegler-Nichols Parameters')
plt.grid()
plt.show()

plt.subplot(1,1,1)
plt.plot(time, response_no_os)
plt.xlabel('Time (s)')
plt.ylabel('Closed-Loop Response')
plt.title('Closed-Loop Step Response no overshoot')
plt.grid()
plt.show()

# Print the calculated PID parameters
print(f'Kp = {Kp}, Ki = {Ki}, Kd = {Kd}')
print(f'Kp_nos = {Kp_nos}, Ki_nos = {Ki_nos}, Kd_nos = {Kd_nos}')

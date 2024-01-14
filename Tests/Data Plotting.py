import krpc

conn = krpc.connect(name='Hello World')

vessel = conn.space_center.active_vessel
refframe = vessel.orbit.body.reference_frame

import time
import matplotlib.pyplot as plt


y = []
t = []
timestamps = []

# PID constants
Kp = 0.02
Ki = 0.001
Kd = 0.1

# Desired height
desired_height = 100

loop_time = 0.5

# Initialize PID variables
previous_error = 0
integral = 0


while True:
    # Calculate error
    error = desired_height - vessel.flight().surface_altitude

    # Update integral term
    integral += error

    # Calculate PID output
    output = Kp * error + Ki * integral + Kd * (error - previous_error)

    # Update previous error
    previous_error = error

    # Append data for plotting
    y.append(vessel.flight().surface_altitude)
    t.append(vessel.control.throttle)
    timestamps.append(time.time())
    if len(y) > 30*1/loop_time:
        y.pop(0)
        t.pop(0)
        timestamps.pop(0)
        

    # Plot altitude
    plt.subplot(2, 1, 1)
    plt.plot(timestamps, y)
    plt.xlabel('Time')
    plt.ylabel('Altitude')
    plt.title('Altitude')

    # Plot throttle
    plt.subplot(2, 1, 2)
    plt.plot(timestamps, t)
    plt.xlabel('Time')
    plt.ylabel('Throttle')
    plt.title('Throttle')

    plt.pause(loop_time)
    plt.clf()

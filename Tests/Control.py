import krpc
import time
import matplotlib.pyplot as plt

class PIDController:
    def __init__(self, Kp, Ki, Kd, integral_limit=None):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.previous_error = 0
        self.integral = 0
        self.integral_limit = integral_limit

    def calculate_output(self, error):
        self.integral += error
        if self.integral_limit is not None:
            self.integral = max(min(self.integral, self.integral_limit), -self.integral_limit)
        output = self.Kp * error + self.Ki * self.integral + self.Kd * (error - self.previous_error)
        self.previous_error = error
        return output

conn = krpc.connect(name='Hello World')
vessel = conn.space_center.active_vessel
refframe = vessel.orbit.body.reference_frame

vertical_controller = PIDController(0.02, 0.0001, 1, integral_limit=1)

desired_height = 1000

loop_time = 0.05

vessel.control.sas = True

for i in range(2, -1, -1):
    print(f'Countdown: {i}')
    time.sleep(1)
    if i==2:
        print('Ignition!')
        vessel.control.activate_next_stage()
        vessel.control.throttle = 1.0
print('Lift off!')
vessel.control.activate_next_stage()

while True:
    vessel.control.throttle = vertical_controller.calculate_output(desired_height - vessel.flight().surface_altitude)
    time.sleep(loop_time)

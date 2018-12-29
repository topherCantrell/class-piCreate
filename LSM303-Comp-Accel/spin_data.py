import time

import IRobotCreate.roomba
import Adafruit_LSM303

# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()

# Create the Roomba instance.
roomba = IRobotCreate.roomba.Roomba()

roomba.set_drive_spin_cw(50)

for _ in range(20*4): # Twenty seconds
    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    print('{0}, {1}'.format(mag_x, mag_y))
    time.sleep(.25)

roomba.set_drive_stop()
roomba.close()
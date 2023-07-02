from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor, Remote
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Button, Port, Direction
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch

# __________________________________________________________________________________________________
# Initialize
# __________________________________________________________________________________________________

# Robot Constants
W_DIAMETER = 61.6  # mm
W_DISTANCE = 91  # mm
W_CIRC = W_DIAMETER * 3.1415926535  # mm
WHEELS_WALL_RATIO = 4  # TODO
WALL_MOTOR_RATIO = 35 / 6  # TODO


CHANNEL = 1

# Hardware Definition
hub = PrimeHub(observe_channels=[CHANNEL]) # make sure the channle matches with the broadcast channle. if more than one controller is broadcasting, change to different channles.
leftW = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
rightW = Motor(Port.B)
wall = Motor(Port.E, gears=[24, 140])
frontCS = ColorSensor(Port.D)
backCS = ColorSensor(Port.A)
wheels = DriveBase(leftW, rightW, wheel_diameter=W_DIAMETER, axle_track=W_DISTANCE)


# __________________________________________________________________________________________________
# Functions
# __________________________________________________________________________________________________


def move(stop, base_speed, turn_rate, lock_wall, wall_speed):
    """ 
    base_speed: int (turn/s)
    turn_rate: int (deg/s)
    """
    if stop:
        wheels.stop()

    else:
        wheels.drive(base_speed, turn_rate)
        if lock_wall:
            wall.run(-turn_rate)
        else:
            wall.run(wall_speed)
        

# __________________________________________________________________________________________________
# Main Loop
# __________________________________________________________________________________________________

hub.light.on(Color.GREEN)
while True:
    stop, turn_rate, base_speed, lock_wall, wall_speed = hub.ble.observe(CHANNEL)
    move(stop, turn_rate, base_speed, lock_wall)

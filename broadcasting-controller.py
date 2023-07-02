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
hub = PrimeHub(broadcast_channel=CHANNEL) # make sure the channle matches with the observing channle. if more than one controller is broadcasting, change to different channles.
speed_controll = ForceSensor(Port.A) 
wall_controll = ForceSensor(Port.B) 


# __________________________________________________________________________________________________
# Functions
# __________________________________________________________________________________________________

def read_contoller():
    """
    force1 - drive
    center + force - reverse drive
    only center - stop
    sides - turn
    force2 + sides - wall
    bluetooth - lock wall
    """

    # driving straight
    drive_direction = -1 if Button.CENTER in Buttons.pressed() else 1 # drive direction
    stop = True if Button.CENTER in Buttons.pressed() else False # stop?
    base_speed = speed_controll.force() * 50 * drive_direction # drive speed 

    # wall / wheels turn direction
    if Button.RIGHT in Buttons.pressed():
        turn_direction = 1
    elif Button.RIGHT in Buttons.pressed():
        turn_direction = -1
    else: 
        turn_direction = 0

    if wall_controll.pressed(): # wall start
        wall_speed  += 10 * turn_direction
        turn_rate = 0
    else: # turn
        turn_rate += turn_direction
        wall_speed = 0

    lock_wall = True in Button.BLUETHOOTH in Buttons.pressed() else False # lock wall

    return stop, turn_rate, base_speed, lock_wall, wall_speed
        

# __________________________________________________________________________________________________
# Main Loop
# __________________________________________________________________________________________________


hub.light.on(Color.MAGENTA)
system.set_stop_button((Button.BLUETHOOTH, Button.CENTER))
turn_rate = 0
wall_speed = 0

while True:
    hub.ble.broadcast(read_contoller())
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor, Remote
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Button, Port, Direction
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch


# __________________________________________________________________________________________________
# Initialize
# __________________________________________________________________________________________________

CHANNEL = 1

# Hardware Definition
hub = PrimeHub(broadcast_channel=CHANNEL) # make sure the channle matches with the observing channle. if more than one controller is broadcasting, change to different channles.
forward = ForceSensor(Port.A) 
backward = ForceSensor(Port.B) 


# __________________________________________________________________________________________________
# Functions
# __________________________________________________________________________________________________

def read_contoller():

    # driving straight: force sensors (back and forth, speed depends on pressure)
    base_speed = forward.force() * 50 if forward.pressed(force=1) else backward.force() * 50

    # turning: side buttons (press longer to increases turn rate, press both buttons to reset)
    global turn_rate
    if Button.RIGHT, Button.LEFT in Buttons.pressed():
        turn_rate = 0
    elif Button.RIGHT in Buttons.pressed():
        turn_rate += 1
    elif Button.LEFT in Buttons.pressed():
        turn_rate -= 1

    # controll wall: bluethooth / center buttons (bluethooth - turn clockwise, center - counter-clockwise, both - lock wall to abs angle)
    if Button.BLUETHOOTH, Button.CENTER in Buttons.pressed():
        lock_wall = True
        wall_direction = 0
    elif Button.BLUETHOOTH in Buttons.pressed():
        lock_wall = False
        wall_direction = 1
    elif Button.CENTER in Buttons.pressed():
        lock_wall = False
        wall_direction = -1


    return turn_rate, base_speed, lock_wall, wall_direction
        

# __________________________________________________________________________________________________
# Main Loop
# __________________________________________________________________________________________________


hub.light.on(Color.MAGENTA)
hub.system.set_stop_button((Button.BLUETHOOTH, Button.CENTER, Button.RIGHT, Button.LEFT))
turn_rate = 0

while True:
    hub.ble.broadcast(read_contoller())
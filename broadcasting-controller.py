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
force_sensor = ForceSensor(Port.A) 


# __________________________________________________________________________________________________
# Functions
# __________________________________________________________________________________________________

def read_contoller():
    # Stop the robot completely by pressing the center button
    stop = Button.CENTER.is_pressed()

    # controll the chassis' movement by tilting the controller:  base_speed => pitch, turn_rate => roll
    base_speed, turn_rate = hub.imu.tilt()
    base_speed *= 7
    turn_rate *= 2

    # controll the wall using the sode buttons. both buttons => stop
    global wall_speed
    if Button.LEFT.is_pressed() and Button.RIGHT.is_pressed(): 
        wall_speed = 0
    elif Button.RIGHT.is_pressed():
        wall_speed += WALL_CHNG
    elif Button.LEFT.is_pressed():
        wall_speed += WALL_CHNG

    # lock the wall to an abs degree by pressing the force sensor
    lock_wall = force_sensor.pressed()
    if lock_wall: wall_speed = 0
    
    return stop, turn_rate, base_speed, lock_wall, wall_speed

        

# __________________________________________________________________________________________________
# Main Loop
# __________________________________________________________________________________________________


hub.light.on(Color.MAGENTA)
system.set_stop_button(Button.BLUETHOOTH)
wall_speed = 0

while True:
    hub.ble.broadcast(read_contoller())
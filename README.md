# bluetooth-arm-yay

# bluetooth controlled robotic arm

this project is a RPI based robotic arm that i built and mounted onto a movable car. the goal was to wirelessly control both the movement of the car and the different joints of the robotic arm through bluetooth.

the RPI receives commands from a connected device over bluetooth and uses those commands to control the movement of the system.

## how it works

the raspberry pi runs a bluetooth rfcomm server and waits for a device to connect. once a connection is established, the program continuously receives numerical commands from the connected device.

each number corresponds to a specific movement.

commands 1-4 control the movement of the car:

- 1 - move forward
- 2 - move backward
- 3 - turn right
- 4 - turn left

commands 5-12 control the robotic arm:

- 5 / 6 - rotate the base clockwise or counterclockwise
- 7 / 8 - move the shoulder up or down
- 9 / 10 - move the elbow up or down
- 11 / 12 - close or open the gripper

the arm uses servoblaster to control the servo positions. each command changes the position of a joint in small increments instead of immediately moving it to a completely different position.

limits are included for each joint so that the position values stay within the intended movement range.

## bluetooth communication

the raspberry pi acts as the bluetooth server using rfcomm.

when the program starts, it waits in listening mode until another bluetooth device connects. after accepting the connection, it receives a command and converts the received value into an integer.

the command is then used to determine which movement should be performed.

if the bluetooth connection is disconnected, the program exits the current connection and waits for another device to connect.



## robotic arm control
the arm has four main controlled sections:

- base
- shoulder
- elbow
- gripper

servo positions are controlled using servoblaster commands from the python program.


## files

`bluearm.py` contains the integrated control program for the system
the files in `tests/` contain smaller programs that were used while testing the bluetooth connection and servo control before integrating the complete system

## hardware

- raspberry pi
- robotic arm
- servo motors
- movable car/base
- bluetooth-enabled control device
- external servo power/control hardware


## notes

this is an older raspberry pi project, so the code uses python 2 syntax and servoblaster, which was used to generate the servo control signals on the original system.

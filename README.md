# bluetooth-arm-yay

# bluetooth controlled robotic arm

this project is a RPI based robotic arm that i built and mounted onto a movable car. the goal was to wirelessly control both the movement of the car and the different joints of the robotic arm through bluetooth.

the RPI receives commands from a connected device over bluetooth and uses those commands to control the movement of the system.





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

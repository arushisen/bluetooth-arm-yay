from bluetooth import *
import RPi.GPIO as GPIO
import bluetooth
import os
import sys
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(35, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

GPIO.output(35, 0)
GPIO.output(36, 0)
GPIO.output(37, 0)
GPIO.output(38, 0)

base = 80
shoulder = 60
elbow = 65
gripper = 60

while True:
    servo_sock = BluetoothSocket(RFCOMM)
    servo_sock.bind(("", PORT_ANY))
    servo_sock.listen(1)

    print "Listening"

    try:
        client_sock, address = servo_sock.accept()
        print "Accepted Connection From", address

        while True:
            try:
                data = client_sock.recv(1024)
                print "Received %s" % data

                x = int(data)

                if x == 1:
                    print "Go Forward"

                    GPIO.output(35, 0)
                    GPIO.output(36, 1)
                    GPIO.output(37, 0)
                    GPIO.output(38, 1)

                    time.sleep(0.5)

                elif x == 2:
                    print "Go Backward"

                    GPIO.output(35, 1)
                    GPIO.output(36, 0)
                    GPIO.output(37, 1)
                    GPIO.output(38, 0)

                    time.sleep(0.5)

                elif x == 3:
                    print "Go Right"

                    GPIO.output(35, 0)
                    GPIO.output(36, 1)
                    GPIO.output(37, 1)
                    GPIO.output(38, 0)

                    time.sleep(0.5)

                elif x == 4:
                    print "Go Left"

                    GPIO.output(35, 1)
                    GPIO.output(36, 0)
                    GPIO.output(37, 0)
                    GPIO.output(38, 1)

                    time.sleep(0.5)

                elif x == 5:  # Base clockwise
                    if base <= 60:
                        base = 60
                    elif base >= 240:
                        base = 240

                    print "Base Clockwise %s" % base

                    cmd = "echo 3=%s >/dev/servoblaster" % base
                    os.system(cmd)

                    base = base + 10

                    time.sleep(0.2)

                elif x == 6:  # Base anticlockwise
                    if base <= 60:
                        base = 60
                    elif base >= 240:
                        base = 240

                    print "Base Anticlockwise %s" % base

                    cmd = "echo 3=%s >/dev/servoblaster" % base
                    os.system(cmd)

                    base = base - 10

                    time.sleep(0.2)

                elif x == 7:  # Shoulder up
                    if shoulder <= 190:
                        shoulder = 190
                    elif shoulder >= 230:
                        shoulder = 230

                    print "Shoulder Up %s" % shoulder

                    cmd = "echo 4=%s >/dev/servoblaster" % shoulder
                    os.system(cmd)

                    time.sleep(0.2)

                    os.system(cmd)

                    cmd = "echo 7=%s >/dev/servoblaster" % shoulder
                    os.system(cmd)

                    time.sleep(0.2)

                    os.system(cmd)

                    shoulder = shoulder + 10

                elif x == 8:  # Shoulder down
                    if shoulder <= 190:
                        shoulder = 190
                    elif shoulder >= 230:
                        shoulder = 230

                    print "Shoulder Moving Down %s" % shoulder

                    cmd = "echo 7=%s >/dev/servoblaster" % shoulder
                    os.system(cmd)

                    time.sleep(0.5)

                    cmd = "echo 4=%s >/dev/servoblaster" % shoulder
                    os.system(cmd)

                    time.sleep(0.2)

                    os.system(cmd)

                    shoulder = shoulder - 10

                elif x == 9:  # Elbow up
                    if elbow <= 120:
                        elbow = 120
                    elif elbow >= 160:
                        elbow = 160

                    print "Elbow Moving Up %s" % elbow

                    cmd = "echo 5=%s >/dev/servoblaster" % elbow
                    os.system(cmd)

                    elbow = elbow + 10

                    time.sleep(0.5)

                elif x == 10:  # Elbow down
                    if elbow <= 140:
                        elbow = 140
                    elif elbow >= 160:
                        elbow = 160

                    print "Elbow Moving Down %s" % elbow

                    cmd = "echo 5=%s >/dev/servoblaster" % elbow
                    os.system(cmd)

                    elbow = elbow - 10

                    time.sleep(0.5)

                elif x == 11:  # Close gripper
                    if gripper <= 60:
                        gripper = 60
                    elif gripper >= 120:
                        gripper = 120

                    print "Gripper Close %s" % gripper

                    cmd = "echo 6=%s >/dev/servoblaster" % gripper
                    os.system(cmd)

                    gripper = gripper + 10

                    time.sleep(0.5)

                elif x == 12:  # Open gripper
                    if gripper <= 60:
                        gripper = 60
                    elif gripper >= 120:
                        gripper = 120

                    print "Gripper Open %s" % gripper

                    cmd = "echo 6=%s >/dev/servoblaster" % gripper
                    os.system(cmd)

                    gripper = gripper - 10

                    time.sleep(0.5)

                else:
                    print "Stop"

            except IOError:
                print "Connection Disconnected"
                break

            except KeyboardInterrupt:
                client_sock.close()
                sys.exit()

    except KeyboardInterrupt:
        servo_sock.close()
        sys.exit()

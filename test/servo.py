# tests bluetooth-based control of a single servo before integrating multiple arm joints
# receives commands over rfcomm and adjusts the servo position in small increments

from bluetooth import*
import RPi.GPIO as GPIO
import os
import time
angle = 60
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,0)

while True:
  servo_sock = BluetoothSocket(RFCOMM) 
  servo_sock.bind(("", PORT_ANY))
  servo_sock.listen(1)
  print "Listening"
  client_sock, address = servo_sock.accept()
  print "Accepted Connection From", address
  while True:
    data = client_sock.recv(1024)
    print "Received %s Data" % data
    x = int(data) 
    
    if x == 1:
      print "Increase Angle"
      if angle <= 60:
        angle = 60
      if angle >= 240:
        angle = 240  
      print " angle is %s",angle
      cmd = "echo 0=%s > dev/servoblaster" %angle
      os.system(cmd)
      angle = angle + 10
      time.sleep(0.5)
   
    elif x == 2:
      print "Decrease Angle"
      if angle <= 60:
        angle = 60
      if angle >= 240:
        angle = 240  
      print " angle is %s",angle
      cmd = "echo 0 = %s >/dev/servoblaster" %angle
      os.system(cmd)
      angle = angle - 10
      time.sleep(1)
GPIO.cleanup()

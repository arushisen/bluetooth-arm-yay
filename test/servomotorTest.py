# basic servoblaster test used to verify that a servo could move between predefined positions.
# cycles through several position values with a short delay between each movement.

import RPi.GPIO as GPIO
import os
import time

cmd=  "echo 0=60 >/dev/servoblaster" 
cmd1= "echo 0=100 >/dev/servoblaster" 
cmd2= "echo 0=200 >/dev/servoblaster" 
cmd3= "echo 0=240 >/dev/servoblaster" 

while True:
  print "Rotating 60 degrees"
  os.system(cmd)
  time.sleep(1)
  
  print " Rotating 100 degrees"
  os.system(cmd1)
  time.sleep(1)
    
  print " Rotating 120 degrees"
  os.system(cmd2)
  time.sleep(1)
  
  print " Rotating 200 degrees"
  os.system(cmd3)
  time.sleep(1)

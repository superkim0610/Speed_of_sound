import serial
import datetime


def write_result(str: str):
    with open('result.txt', 'a') as f:
        f.write(str+'\n')


py_serial = serial.Serial(
    port='COM3',
    baudrate=9600,
)


write_result(">> logging starts at "+str(datetime.datetime.now()))
while True:
    if py_serial.readable():
        response = py_serial.readline()[:-1].decode()
        print(response)
        write_result(response)
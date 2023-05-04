import serial,time
import numpy as np

ser = serial.Serial("/dev/serial0", 115200,timeout=0) # mini UART serial device

def read_data():
    while True:
        counter = ser.in_waiting
        if counter > 8:
            bytes_serial = ser.read(9)
            ser.reset_input_buffer()

            if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59:
                distance = bytes_serial[2] + bytes_serial[3]*256
                return distance/100.0

if ser.isOpen() == False:
    ser.open()

distance = read_data()
print(distance)
ser.close()
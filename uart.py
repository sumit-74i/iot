import serial
import time

uart = serial.Serial(
    '/dev/serial0',
    9600,
    timeout=1
)

message = input("Enter message: ")

uart.write(message.encode())

print("Message sent:", message)

uart.close()

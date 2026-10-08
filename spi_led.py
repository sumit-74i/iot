import spidev
import time

spi = spidev.SpiDev()

spi.open(0, 0)
spi.max_speed_hz = 100000
spi.mode = 0

while True:

    command = input("Enter 1 to ON, 0 to OFF, q to quit: ")

    if command == 'q':
        break

    if command == '1' or command == '0':
        spi.xfer2([ord(command)])
        print("Command sent:", command)
    else:
        print("Please enter only 1, 0 or q")

spi.close()
import spidev

spi = spidev.SpiDev()

spi.open(0, 0)
spi.max_speed_hz = 100000
spi.mode = 0

while True:

    command = input("Enter 1 to ON, 0 to OFF, q to quit: ")

    if command == 'q':
        break

    if command == '1' or command == '0':
        spi.xfer2([ord(command)])
        print("Command sent:", command)
    else:
        print("Enter only 1, 0 or q")


spi.close()

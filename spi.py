import spidev
import time

spi = spidev.SpiDev()

spi.open(0, 0)
spi.max_speed_hz = 100000
spi.mode = 0

message = input("Enter message: ")

for c in message:
    spi.xfer2([ord(c)])
    time.sleep(0.01)

print("Message sent:", message)

spi.close()


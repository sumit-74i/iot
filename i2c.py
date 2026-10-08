
from smbus import SMBus

addr = 0x08

bus = SMBus(1)

message = "Hello World"

data = [ord(c) for c in message]

bus.write_i2c_block_data(addr, 0, data)

print("Message sent:", message)

bus.close()

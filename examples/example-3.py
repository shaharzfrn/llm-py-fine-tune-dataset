

'''
This code import the device class from the framework and create new device.
After that it init the device channels to their index
'''

# import the device class
from framework import Device

# create first device with 4 channels
device = Device(4)

# init channel 0 to 0
device[0] = 0

# init channel 1 to 1
device[1] = 1

# init channel 2 to 2
device[2] = 2

# init channel 3 to 3
device[3] = 3
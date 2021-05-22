import time
from ppadb.client import Client

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()
device = devices[0]

device.shell('input keyevent 26')
device.shell('input touchscreen swipe  540 1700 540 540 ')

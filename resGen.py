from ppadb.client import Client

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()
device = devices[0]

count =0

image = device.screencap()

with open('refff/processingState.png', 'wb') as f:
        f.write(image)
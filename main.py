from imgcrp import cmode
from imgcrp import buttonstat
from imgcrp import prnttym
from ppadb.client import Client
import os
import time
import datetime;

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

MAX = 4
count =0
status = "initialsed"

open("Log/timestamps.txt", "w").close()
while count <MAX or status != "\n------Task Finished-------":
    image = device.screencap()

    with open('refff/crntState.png', 'wb') as f:
        f.write(image)
    if cmode("refff/trgrState.png")!=cmode("refff/crntState.png"):
        device.shell('input touchscreen swipe  100 2130 900 2130 ')
    else:
        if buttonstat("refff/trgrState.png")==buttonstat("refff/crntState.png"):
            
            if count >= MAX :
                status = "\n------Task Finished-------"
            else:
                if count == 0:
                    startProgrm = time.time()
                count=count+1
                status="\n------Taking photo "+ str(count)+ "------"
                startCrntPhoto = time.time()
                device.shell('input touchscreen swipe  540 540 540 540 ')
                time.sleep(2)
                device.shell('input touchscreen swipe  540 1900 540 1900 ')
        else :
            if buttonstat("refff/crossState.png")==buttonstat("refff/crntState.png"):
                status="cross State"
            else :
                if buttonstat("refff/progrssState.png")==buttonstat("refff/crntState.png"):
                    status="progrss State"
                else:
                    if buttonstat("refff/ScreenOffState.png")==buttonstat("refff/crntState.png"):
                        status="Screenoff State"
                        count = MAX
    with open('Log/timestamps.txt', 'a') as f:
        f.write( str(datetime.datetime.now()) + " "+status +"\n")
        f.close
    try:
        os.system('cls')
        print( "Time elpsd for photo " +str(count)+" is "+ str(prnttym(time.time()-startCrntPhoto)) + "\n")
        print("Remaining Photos = "+str(MAX-count))
        print( "Time per photo is "+ str(prnttym(int((time.time()-startProgrm)/count)))+ "s" )
        print( "Total Time Estimate photo is "+ str(prnttym(int((time.time()-startProgrm)/count)*MAX))+ "s" )
        print( "Remaining Time Needed is "+ str(prnttym(int((time.time()-startProgrm)/count)*(MAX-count)))+ "s" )
    except:
        print("An exception occurred")
    device.shell('input touchscreen swipe  100 2133 100 2133 ')


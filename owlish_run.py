import threading
from threading import Thread
from bluepy.btle import Scanner, DefaultDelegate
import time
from send_twilio import send_twilio
from upload_cloudinary import upload_cloudinary
import picamera
from detect_picamera import main, q
activate_status = False

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
        elif isNewData:
            print ("Received new data from", dev.addr)
            
def rsl10_activate():
    while True:
        scanner = Scanner().withDelegate(ScanDelegate())
        devices = scanner.scan(3.0) #scan for 3 seconds and repeat
        for dev in devices:
            #print ("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
            if dev.addr == "60:c0:bf:28:65:c0":
               print("RSL-10 device found")
               global activate_status
               activate_status = not activate_status
               time.sleep(60)
               
def start_picamera():
    while True:
        main(activate_status)
        
def cloudinary_twilio_send():
    while True:
         classes_id = q.get()
         if(0.0 in classes_id): #check if object is person [person class id is 0.0 according to labels]
            url = upload_cloudinary('intruder') #upload to cloud
            print(url)
            send_twilio(url)
            #print("detected")
scan_bluetooth = Thread(target=rsl10_activate)
inference = Thread(target=start_picamera)
send_message = Thread(target=cloudinary_twilio_send)

if __name__ == '__main__':
    scan_bluetooth.start()
    inference.start()
    send_message.start()
    
 

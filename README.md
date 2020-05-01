## Owlish

### Demo
* Click the image below to view the demo on Youtube
[![Watch the video](https://scontent.fbki2-1.fna.fbcdn.net/v/t1.15752-9/95568337_1142028552813612_8274245158485098496_n.jpg?_nc_cat=109&_nc_sid=b96e70&_nc_ohc=_br9W-wYAlMAX-HR1KW&_nc_ht=scontent.fbki2-1.fna&oh=55880f16e666bf15c0f3e4933aae0f54&oe=5ED0FAE0)](https://youtu.be/idDMZyX_ofI)

<br />

### Quick Start without BLE from RSL-10 Sense Kit
* Install all dependencies with `pip3`in dependencies.txt in your PI.
* Replace credentials for Cloudinary and Twilio Whatsapp API (in upload_cloudinary.py & send_twilio.py) with your own.
* Clone and install the Tensorflow lite object detection model example by following the README.md in their official [repository](https://github.com/tensorflow/examples/blob/master/lite/examples/object_detection/raspberry_pi/README.md)
* Once cloned and installed,`cd` to examples/lite/examples/object_detection/raspberry_pi/ and insert the following files from this repository (send_twilio.py, upload_cloudinary.py & detect_picamera.py). 
* In owlish_run.py replace activate_status variable to `True` to run without activation from the BLE device and comment out `scan_bluetooth.start()` in the main.  
* Run the application with `python3 detect_picamera.py` 
<br />

### Quick Start using BLE from RSL-10 Sense Kit
* The only difference is to use `sudo pip3` for installing every dependency (including the tensorflow lite) as we'll need to expose modules to the root user. This is because running the `detect_picamera.py` requires root permissions for using the Bluetooth Peripheral on the PI.
* Follow the rest of the steps in `Quick Start without BLE from RSL-10 Sense Kit` without modifying owlish_run.py.
* Run the application with `sudo python3 detect_picamera.py` 

<br />

### Screenshot
* Once you have the application up and running, you should receive something similar!
 
 ![screenshot](images/detected_intruder.png?raw=true "Title")

### Built using
#### Hardware components
* [Raspberry Pi 3B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/)
* [A Pi Camera Module V2](https://www.raspberrypi.org/products/camera-module-v2/)
* [RSL10-SENSE-GEVK dev kit](https://www.onsemi.com/support/evaluation-board/rsl10-sense-gevk) 

#### Software components
* [Twilio WhatsApp](https://www.twilio.com/docs/whatsapp/tutorial/send-and-receive-media-messages-whatsapp-python) 
* [TensorFlow lite](https://github.com/tensorflow/examples/blob/master/lite/examples/object_detection/raspberry_pi/README.md) 
* [Bluepy](https://ianharvey.github.io/bluepy-doc/)
* [Cloudinary](https://cloudinary.com/) 

### Misc
If you'd like to learn more, I did a technical write up over at [dev.to](https://dev.to/mcoscon/placeholder-title-1a0f-temp-slug-5865389?preview=2d4da0309e604de71fe680c5632802c9dd1915a9a0d907b95dbf93e29b671441fb431eb3d35d5e5b466b6275f68274bb01cedaa2480e27e5562bd9ad)

### Future Improvements & Todo's
* Using a personal smartphone to activate the system when you're away instead of using the RSL10-SENSE-GEVK dev. This would be a better option but requires an additional WiFi adapter dongle.
* Using Twilio Autopilot for handoff to relevant authorities.
* Boost inference performance with Coral USB accelerator 
* Dockerize the application

### License
This project is licensed under [MIT](https://opensource.org/licenses/MIT).

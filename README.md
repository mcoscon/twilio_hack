<h1 align="center" style="border-bottom: none !important; margin-bottom: 5px !important;"><a href="https://designrevision.com/downloads/shards-dashboard-lite-react/">Intruder Twilert</a></h1>
<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" />
  </a>
</p>

<p align="center">
Owlish - a camera based application that has its eyes set on efficient monitoring, detection and alerting of anyone that's not supposed to be in your dorm while you're away.
</p>

<p align="center">
  <a href="https://idp-app-70f95.firebaseapp.com">
    <img height="55px" src="assets/btn-live-preview.png" />
  </a>
</p>


<br />

### Quick Start without BLE from RSL-10 Sense Kit
* Install all dependencies with `pip3`in dependencies.txt in your PI.
* Replace credentials for Cloudinary and Twilio Whatsapp API (in upload_cloudinary.py & send_twilio.py) with your own.
* Clone and install the Tensorflow lite object detection model example by following the README.md in their official [repository](https://github.com/tensorflow/examples/blob/master/lite/examples/object_detection/raspberry_pi/README.md)
* Once cloned and installed,`cd` to examples/lite/examples/object_detection/raspberry_pi/ and insert the following files from this repository (send_twilio.py, upload_cloudinary.py & detect_picamera.py). 
* In owlish_run.py replace activate_status variable to `True` to disable activation from the BLE device.
* Run the application with `python3 detect_picamera.py` 
<br />

### Quick Start using BLE from RSL-10 Sense Kit
* The only difference is to use `sudo pip3` for installing every dependency (including the tensorflow lite) as we'll need to expose modules to the root user. This is because running the `detect_picamera.py` requires root permissions for using the Bluetooth Peripheral on the PI.
* Follow the rest of the steps in `Quick Start without BLE from RSL-10 Sense Kit` without modifying the activate_status.
* Run the application with `sudo python3 detect_picamera.py` 

<br />

### Screenshot
Once you have the application up and running, you should receive something similar!
<br />
![screenshot](images/detected_intruder.png?raw=true "Title")

### Built using
- [Reactjs](https://reactjs.org/)
- [Material UI](https://material-ui.com/)
- [Firebase](https://firebase.google.com/)
- [Raspberry PI 3B+](https://www.raspberrypi.org/)
- [Intel Neural Compute Stick](https://software.intel.com/en-us/articles/intel-movidius-neural-compute-stick)
- [Nodejs](https://nodejs.org/en/)
- [Pyrebase](https://github.com/thisbejim/Pyrebase)

<br />

### Languages
- Python
- Javascript

<br />

### To-dos
- Twilio SMS integration

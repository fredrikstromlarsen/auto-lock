""" Autolock
A program that automatically locks your screen when nobody is in front of it.

    Get program exec arguments (lockscreen command)
    Start infinite loop:
        Sleep 5s

        Capture image from camera
        Do black magic to determine if person is visible or not

        If person is not visible:
            Send command: custom lockscreen command


Requires:
- A camera that captures enough light.
- A screen lock (command) that autolock can run when triggered. 
"""

from cv2 import VideoCapture, imshow, imwrite, waitKey, destroyWindow
from time import sleep
  
cam_port = 0

while True:
    sleep(2)
    cam = VideoCapture(cam_port)
    result, image = cam.read()
    
    if result:
        imwrite("img.png", image)
        # imshow("img", image)
        # waitKey(2000)
        # destroyWindow("img")
    
    else:
        print("No image detected. Please! try again")
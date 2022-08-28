""" Autolock
A program that automatically locks your screen when nobody is in front of it.

    Get program exec arguments (lockscreen command)
    Start infinite loop:
        Sleep 3s

        Capture image from camera
        Do black magic to determine if person is visible or not

        If person is not visible:
            Send command: custom lockscreen command


Requires:
- A camera that captures enough light.
- A screen lock (command) that autolock can run when triggered. 
"""

# Get exec args
from sys import argv
# Camera stuff
from cv2 import VideoCapture, imshow, imwrite, waitKey, destroyWindow
# Delay between image captures
from time import sleep
# Send lockscreen command
from os import system
# Debugging
from pprint import pprint


def main():
    # if there was no second argument
    # specifying the lockscreen command
    # to run when triggered, default to
    # i3lock -c 000.
    if len(argv) == 1:
        TRIGGERCMD = "i3lock -fc 000000"
    else:
        TRIGGERCMD = argv[1]

    # capture image from camera with opencv2
    CAMERA_PORT = -1  # https://stackoverflow.com/questions/59371075/opencv-error-cant-open-camera-through-video-capture
    IMAGE_PATH = "img.png"

    # Loop until triggered
    while True:
        sleep(3)

        # Capture image
        cam = VideoCapture(CAMERA_PORT)
        result, image = cam.read()
        if result:

            # Write image to file
            imwrite(IMAGE_PATH, image)

            # AI's confidence in determining if there it sees a person.
            confidence = voodoo_magic(IMAGE_PATH)
            if confidence > 89:

                # Lock the screen
                system(TRIGGERCMD)

                # Prevent lockscreen command from
                # running when already triggered
                break

        else:
            print(f"Couldn't get image from camera#{CAMERA_PORT}")


def voodoo_magic(IMAGE_PATH):
    return 95


if __name__ == '__main__':
    main()

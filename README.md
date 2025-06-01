# automatic-turret-gun

DIY project, to scare away animals from the places, where they are not welcome

## Parts

1. Raspberry Pi 5 - processing unit
2. Pimoroni Pan-Tilt Hat - movements and tracking
3. Raspberry Pi Camera 3 Wide - vision
4. Blinkt! LED Board - to debug the operations
6. OpenCV-Python for video analysis
5. some USB controlled water pump (pending) - to shoot water in the direction of detected animal

## Intended Operations

1. Constantly scan environment for approaching animals
2. Once animal is detected - track the camera on it
3. Shoot water (to debug LED Board will simulate that)

## Install Dependencies

```
sudo apt-get update
sudo apt-get install python3-pantilthat
sudo apt-get install python3-blinkt
sudo apt-get install python3-rpi-lgpio
```

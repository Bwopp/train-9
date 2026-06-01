# --- WARNING READ "FINAL" AT THE BOTTOM, PLEASE READ THROUGH FULL STEPS ---

Before running FINAL_Tracker.py, you need to configure the three main entry points at the top of the script to match your local file structure.

model = YOLO('YOUR_PATH_TO/aircraft_train-9/weights/best.pt') 
detector = YOLO('yolo11n.pt') 
cap = cv2.VideoCapture('YOUR_PATH_TO/video.mp4')


# --- SETUP ---

Required Dependencies Checklist
System Environment

Python 3.12.14

External Packages

ultralytics (Version 8.4.56)

opencv-python (Latest stable release compatible with Python 3.12)

numpy (Latest stable release compatible with Python 3.12)

Model Files

yolo11n.pt (The base object detection weights file)

best.pt (The custom classification weights file located inside the aircraft_train-9/weights/ folder)

Media

Input video file (Any target aviation video, such as an .mp4 file)


# --- SETUP STEPS ---
for mac

1. /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" (INSTALL HOMEBREW VIA TERMINAL

2. brew install python@3.12

3. python3.12 -m venv ml_env

4. source ml_env/bin/activate

5. pip install ultralytics==8.4.56 opencv-python numpy


config (YOU MUST KEEP /AIRCRAFT_TRAIN-9/WEIGHTS/BEST.PT
6. model = YOLO('path/to/aircraft_train-9/weights/best.pt')
detector = YOLO('yolo11n.pt')
cap = cv2.VideoCapture('path/to/video.mp4')



# --- FINAL ---

This has only been tested on Mac; lmk if it doesn't work.

I recommend that you only use clear-sky plane spotting videos at Auckland Airport, as the model has been specifically trained on this data; however, in the future, the model will contain data from major hubs. 

current training data includes 

auckland Airport - day - most confident
lax - night and day - less confident
frankfurt - night - less confident
paris - day - less confident

the model is only 95% confident and can only recognise 

a320
a330
a350
a380
md11
b767
b777
b747
atr 
b787

in future the model will be trained with 737 and other common aircraft.

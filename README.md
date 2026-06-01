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


This has only been tested on mac, lmk if it doesnt work.

Before running FINAL_Tracker.py, you need to configure the three main entry points at the top of the script to match your local file structure.

# --- SETUP ---
model = YOLO('YOUR_PATH_TO/aircraft_train-9/weights/best.pt') 
detector = YOLO('yolo11n.pt') 
cap = cv2.VideoCapture('YOUR_PATH_TO/video.mp4')


Required Dependencies Checklist
System Environment

Python 3.12.14

External Packages

ultralytics (YOLO11 framework)

opencv-python (OpenCV library)

numpy (Math & array library)

Model Files

yolo11n.pt (The base object detection weights file)

best.pt (The custom classification weights file located inside the aircraft_train-9/weights/ folder)

Media

Input video file (Any target aviation video, such as an .mp4 file)

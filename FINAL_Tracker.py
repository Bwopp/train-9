import cv2
import time
import numpy as np
from collections import deque
from ultralytics import YOLO

model = YOLO('WHERE ITS INSTALLED/aircraft_train-9/weights/best.pt') 
detector = YOLO('yolo11n.pt') 
cap = cv2.VideoCapture('video here.mp4')


gui_threshold = 0.80     
gui_cooldown = 4         
cooldown_duration = 2   
MAX_MEM_FRAMES = 5     

start_time = time.time()
last_gui_time = 0
waiting_for_input = False
gui_start_time = 0  
found_label = "Scanning..."

track_history = {}

print("--- TRACKER ACTIVE: ESC to Close ---")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    current_time = time.time()
    key = cv2.waitKey(1) & 0xFF
    
    if key == 27: 
        break

    
    if current_time - start_time < cooldown_duration:
        remaining = int(cooldown_duration - (current_time - start_time))
        cv2.putText(frame, f"Starting in {remaining}s...", (50, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Aircraft Tracker', frame)
        continue

   
    if waiting_for_input:
        elapsed_gui_time = current_time - gui_start_time
        remaining_gui_time = max(0.0, 2.0 - elapsed_gui_time)
        
        frame[:] = (50, 50, 50) 
        cv2.putText(frame, "CONGRATS!", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        cv2.putText(frame, f"YOU FOUND: {found_label.upper()}", (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
        
        cv2.putText(frame, f"RESUMING IN {remaining_gui_time:.1f}s...", (150, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        cv2.imshow('Aircraft Tracker', frame)
        
        if elapsed_gui_time >= 2.0:
            waiting_for_input = False
            last_gui_time = current_time
        continue

   
    results = detector.track(frame, classes=[4], conf=0.45, iou=0.4, persist=True, verbose=False)
    
    if results and len(results[0].boxes) > 0:
        boxes = results[0].boxes
        track_ids = boxes.id.int().cpu().tolist() if boxes.id is not None else [None] * len(boxes)
        
        for box, track_id in zip(boxes, track_ids):
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            crop = frame[y1:y2, x1:x2]
            
            if crop.size > 0:
                pred = model.predict(crop, verbose=False)
                raw_probs = pred[0].probs.data.cpu().numpy()
                
                if track_id is not None:
                    if track_id not in track_history:
                        track_history[track_id] = deque(maxlen=MAX_MEM_FRAMES)
                    
                    track_history[track_id].append(raw_probs)
                    
                   
                    smoothed_probs = np.mean(track_history[track_id], axis=0)
                    top1_idx = np.argmax(smoothed_probs)
                    
                    label = pred[0].names[top1_idx]
                    confidence = smoothed_probs[top1_idx]
                else:
                    top1_idx = pred[0].probs.top1
                    label = pred[0].names[top1_idx]
                    confidence = pred[0].probs.top1conf.item()
                
             
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                display_text = f"ID {track_id}: {label} ({confidence:.1%})" if track_id is not None else f"{label} ({confidence:.1%})"
                cv2.putText(frame, display_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
            
                if (confidence > gui_threshold) and (current_time - last_gui_time > gui_cooldown):
                    found_label = label
                    gui_start_time = current_time  
                    waiting_for_input = True

    cv2.imshow('Aircraft Tracker', frame)

cap.release()
cv2.destroyAllWindows()

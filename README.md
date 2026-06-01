# --- WARNING READ "FINAL" AT THE BOTTOM, PLEASE READ THROUGH FULL STEPS ---

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

2. Create new folder, (after installing homebrew) then run this cmd, cd ~/foldername (YOU MUST DO THIS EVEN IF YOU HAVE HOMEBREW ALREADY)

3. source ml_env/bin/activate

5. brew install python@3.12

6. python3.12 -m venv ml_env

7. source ml_env/bin/activate

8. pip install ultralytics==8.4.56 opencv-python numpy

9. Please keep in mind, ultralytics may have a yellow line under neath it, then you need to press cmd shift p and select python interpreter, then select (img below)
<img width="285" height="22" alt="image" src="https://github.com/user-attachments/assets/d6216d41-c088-412b-b9ab-05e2c1cac447" />

10. run the file


setup should not take longer than 5 minutes


# --- FINAL ---

This has only been tested on Mac; lmk if it doesn't work.

I recommend that you only use clear-sky plane spotting videos at Auckland Airport, as the model has been specifically trained on this data; however, in the future, the model will contain data from major hubs.  (UPDATE - I HAVE ALREADY LOADED A VIDEO, NO NEED TO CHANGED IT)

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

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

10. Nesscessary step, find a video of auckland plane spotting, download it, and insert it into the project folder, name it "auckland_landing.mp4"

11. run the file


setup should not take longer than 5 minutes


# --- FINAL ---

This has only been tested on Mac; lmk if it doesn't work.

you must download a video of auckland plane spotting online in clear blue skies, insert the video into the project folder and name it auckland_landing.mp4, other wise change the name in the final track.py file if you would rather call your video a different name.

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

In the future, the model will be trained with 737 and other common aircraft.

# --- FAQ --- 

Are there better alternatives? - Yes, fgvc-aircraft is much better at detecting aircraft; however, the dataset was developed in 2013 and fails to recognise modern planes, like the A350.

Why is it not accurate? - Train 9 was mainly trained on Auckland Airport plane-spotting videos, Frankfurt, Paris and Los Angeles airport, which means it works better in those environments. The data is accurate; however, depending on the weather and the model of aircraft, results may differ.

When will it be retrained and get smarter? - I am currently working on retraining the model; Train 10 will be out shortly, within the coming months, as training it takes a significant amount of human input.

Can you include more planes? - Yes, in Train 10, I will be including the 737, A321, Embraer family, Bombardier family, "Generic prop plane", "Generic private jet", 757, A340 and 777x.

How do I use this? - At the moment, I am working on creating an app to run this on your phone; however at the moment, it can be run through a computer using the video feature, or you can switch to webcam and direct your webcam at aircraft, additionally, you can use an external webcam, or camera, synced to the program. 


<img width="931" height="473" alt="image" src="https://github.com/user-attachments/assets/938e1fc2-3386-4e15-be34-e57a759fd9a6" />

<img width="937" height="375" alt="image" src="https://github.com/user-attachments/assets/b749aaf5-79cd-4bb7-b11f-4597a9773cec" />

<img width="911" height="369" alt="image" src="https://github.com/user-attachments/assets/3e110268-0ca3-40fc-ba16-9bb7a704d6e1" />

<img width="410" height="189" alt="image" src="https://github.com/user-attachments/assets/6def1964-8ffb-48de-8d4d-9a386ff673b4" />




# --- Please read Through [Final](#final) ---

# Train-9 Setup

## Dependencies
| Package | Version |
|---------|---------|
| Python | 3.14.4 |
| OpenCV | 4.13.0 |
| Ultralytics | 8.4.48 |
| PyTorch | 2.12.0 |
| Torchvision | 0.27.0 |
| NumPy | 2.4.4 |

## Getting the Project
```bash
git clone https://github.com/Josh532/train-9.git
```
```bash
cd train-9
```
Or download and extract the ZIP from GitHub, then navigate into the folder.

---

## Mac
Installing via Homebrew is recommended - [Homebrew Website](https://brew.sh/)

1. Install Homebrew:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Install Python 3.14:
```bash
brew install python@3.14
```

3. Create a virtual environment (Make sure you are in the train-9 directory first):
```bash
python3.14 -m venv ml_env
```

4. Activate the virtual environment:
```bash
source ml_env/bin/activate
```

5. Install dependencies:
```bash
pip install opencv-python==4.13.0 ultralytics==8.4.48 torch==2.12.0 torchvision==0.27.0 numpy==2.4.4
```

6. Run the program:
```bash
python FINAL_Tracker.py
```
A file picker will open, select your video file.

---

## Windows

1. Install Python 3.14:
```powershell
winget install Python.Python.3.14
```

2. Restart your terminal, then create a virtual environment (Make sure you are in the train-9 directory first):
```powershell
python -m venv ml_env
```

3. Activate the virtual environment:
```powershell
ml_env\Scripts\activate
```

4. Install dependencies:
```powershell
pip install opencv-python==4.13.0 ultralytics==8.4.48 torch==2.12.0 torchvision==0.27.0 numpy==2.4.4
```

5. Run the program:
```powershell
python FINAL_Tracker.py
```
A file picker will open, select your video file.

---

## Linux
1. Install Python 3.14 and Tkinter from your distro's package manager:

2. Create a virtual environment (Make sure you are in the train-9 directory first):
```bash
python3.14 -m venv ml_env
```

3. Activate the virtual environment:
```bash
source ml_env/bin/activate
```

4. Install dependencies:
```bash
pip install opencv-python==4.13.0 ultralytics==8.4.48 torch==2.12.0 torchvision==0.27.0 numpy==2.4.4
```

5. Run the program:
```bash
python FINAL_Tracker.py
```
A file picker will open, select your video file.

---

## NixOS / Nix / Nix-Darwin

1. Make sure flakes and nix-command are enabled in your configuration:
```nix
nix.settings.experimental-features = [ "nix-command" "flakes" ];
```

2. Enter the development shell (Make sure you are in the train-9 directory first):
```bash
nix develop
```

3. Run the program:
```bash
python FINAL_Tracker.py
```
A file picker will open, select your video file.

## Final

This has only been tested on Mac and NixOS

The Windows and "Legacy" Linux insturctions have not been tested, additionally the Nix instructions have only been tested on NixOS and not Nix-Darwin or Nix installed on another distro.
Please create an issue if they are wrong.

Mac instructions were recently changed and should still be working.

Your video should be using an mp4 container

Current training data includes :

| Location | Time | Confidence |
|---------|---------|---------|
| Auckland Airport | Day | Most confident |
| LAX | Night and day | Less confident |
| Frankfurt | Night | Less confident |
| Paris | Day | Less confident |

The model is only 95% confident and can only recognise:

  A320
  A330
  A350
  A380

  767
  777
  747
  787
  
  ATR
  MD11

In the future, the model will be trained with 737 and other common aircraft.

## FAQ

Are there better alternatives? - Yes, fgvc-aircraft is much better at detecting aircraft; however, the dataset was developed in 2013 and fails to recognise modern planes, like the A350.

Why is it not accurate? - Train 9 was mainly trained on Auckland Airport plane-spotting videos, Frankfurt, Paris and Los Angeles airport, which means it works better in those environments. The data is accurate; however, depending on the weather and the model of aircraft, results may differ.

When will it be retrained and get smarter? - I am currently working on retraining the model; Train 10 will be out shortly, within the coming months, as training it takes a significant amount of human input.

Can you include more planes? - Yes, in Train 10, I will be including the 737, A321, Embraer family, Bombardier family, "Generic prop plane", "Generic private jet", 757, A340 and 777x.

How do I use this? - At the moment, I am working on creating an app to run this on your phone; however at the moment, it can be run through a computer using the video feature, or you can switch to webcam and direct your webcam at aircraft, additionally, you can use an external webcam, or camera, synced to the program. 

## Further Questions

Contact me - [joshmck.site](https://joshmck.site/contact.html)
or
Leave an issue on github


<img width="931" height="473" alt="image" src="https://github.com/user-attachments/assets/938e1fc2-3386-4e15-be34-e57a759fd9a6" />

<img width="937" height="375" alt="image" src="https://github.com/user-attachments/assets/b749aaf5-79cd-4bb7-b11f-4597a9773cec" />

<img width="911" height="369" alt="image" src="https://github.com/user-attachments/assets/3e110268-0ca3-40fc-ba16-9bb7a704d6e1" />

<img width="410" height="189" alt="image" src="https://github.com/user-attachments/assets/6def1964-8ffb-48de-8d4d-9a386ff673b4" />




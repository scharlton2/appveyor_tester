# run_iric_install.py

import pyautogui, sys, time
import subprocess
import os
import tkinter as tk

def capture_and_push_artifact(path):
    pyautogui.screenshot(path)
    if os.environ.get('APPVEYOR') is not None:
        subprocess.call("appveyor PushArtifact " + path)
    return

# left = location[0]; top = location[1]; width = location[2]; height = location[3]
LEFT = 0
TOP = 1
WIDTH = 2
HEIGHT = 3

pyautogui.FAILSAFE = False
type_interval = 0.02

# place mouse on screen to start iRIC (if multiple screens)
pyautogui.moveTo(1, 1)

# minimize everything
pyautogui.hotkey('win', 'm')
time.sleep(3.0)
capture_and_push_artifact("00-vcredist_x64.png")

# verify resolution
screenWidth, screenHeight = pyautogui.size()
print("Screen resolution: {}x{}".format(screenWidth, screenHeight))

# start install (note path seps)
subprocess.Popen("prod_src/packages/runtime/data/vc2015_vcredist_x64.exe /log vc2015_vcredist_x64.log")

# wait until ready
location = pyautogui.locateOnScreen('readyDialog-2012.png')
while location is None:
    location = pyautogui.locateOnScreen('readyDialog-2012.png')
    time.sleep(20)
    capture_and_push_artifact("01-vcredist_x64.png")
capture_and_push_artifact("02-vcredist_x64.png")

# agree checkbox
pyautogui.hotkey('alt', 'a')
time.sleep(0.5)
capture_and_push_artifact("03-vcredist_x64.png")

# install button
pyautogui.hotkey('alt', 'i')
time.sleep(0.5)
capture_and_push_artifact("04-vcredist_x64.png")

# wait for finish
time.sleep(30.0)
capture_and_push_artifact("05-vcredist_x64.png")
os.system("dir")


# open log file
time.sleep(10.0)
capture_and_push_artifact("06-vcredist_x64.png")
if os.environ.get('APPVEYOR') is not None:
    subprocess.call("appveyor PushArtifact " + "vc2015_vcredist_x64.log")

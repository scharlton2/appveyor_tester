# install_vc2017_runtime.py


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
capture_and_push_artifact("00-vc2017_vcredist_x64.png")

# verify resolution
screenWidth, screenHeight = pyautogui.size()
print("Screen resolution: {}x{}".format(screenWidth, screenHeight))

# start install (note path seps)
subprocess.Popen("prod_src/packages/runtime/data/vc2017_vcredist_x64.exe /log vc2017_vcredist_x64.log")

# wait until ready
location = pyautogui.locateCenterOnScreen('agreeCheckbox-2012.png')
while location is None:
    time.sleep(1)
    location = pyautogui.locateCenterOnScreen('agreeCheckbox-2012.png')
capture_and_push_artifact("01-vc2017_vcredist_x64.png")

# agree checkbox
# Note: its better to click on checkbox since the dialog sometimes doesn't have the focus
pyautogui.moveTo(location)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(location)
time.sleep(0.5)
capture_and_push_artifact("02-vc2017_vcredist_x64.png")

# install button
pyautogui.hotkey('alt', 'i')
time.sleep(0.5)
capture_and_push_artifact("03-vc2017_vcredist_x64.png")

# wait for finish
time.sleep(30.0)
capture_and_push_artifact("04-vc2017_vcredist_x64.png")

## # close dialog
## location = pyautogui.locateCenterOnScreen('closeButton-2012.png')
## while location is None:
##     time.sleep(1)
##     location = pyautogui.locateCenterOnScreen('closeButton-2012.png')
## pyautogui.moveTo(location)  # this might not be necessary (needs further testing - at least for iric installers)
## pyautogui.click(location)
## time.sleep(0.5)
## capture_and_push_artifact("05-vc2017_vcredist_x64.png")
## 
## # push log
## if os.environ.get('APPVEYOR') is not None:
##     subprocess.call("appveyor PushArtifact " + "vc2017_vcredist_x64.log")

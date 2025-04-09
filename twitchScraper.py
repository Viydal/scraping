import pyautogui
import time

if __name__ == "__main__":
  
  time.sleep(2)
  
  endTime = time.time() + 5
  
  pyautogui.keyDown()
  while time.time() < endTime:
    pyautogui.hold('a')
  
  pyautogui.keyUp('a')
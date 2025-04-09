import pyautogui
import time

if __name__ == "__main__":
  
  time.sleep(2)
  
  endTime = time.time() + 5
  while time.time() < endTime:
    pyautogui.press('a')
    
  pyautogui.click()
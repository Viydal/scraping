import requests
import json
from pynput.keyboard import Key, Controller
import time

def retrieveMessages(channelID):
    headers = {
        'authorization': 'AUTH TOKEN'
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelID}/messages', headers=headers)

    return json.loads(r.text)

if __name__ == "__main__":
    keyboard = Controller()

    while True:
        messages = retrieveMessages(811875070606835732)
        lastMessage = messages[0]['content']

        while True:
            messages = retrieveMessages(811875070606835732)
            currentMessage = messages[0]['content']
            if (currentMessage != lastMessage):
                break

        if (currentMessage == "hello"):
            print("message detected sending response")
            keyboard.type("hi")
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
import pydirectinput
import time
import hashlib
import random

# Defining movement terms
forwardCommands = ["w", "move forward", "move forwards", "forward", "forwards", "go forward", "go forwards", "walk forward", "walk forwards"]
backCommands = ["s", "move backward", "move backwards", "back", "go back", "backwards", "hello whtbrd", "go backward", "go backwards", "walk backward", "walk backwards"]
leftCommands = ["a", "left", "go left", "move left", "walk left"]
rightCommands = ["d", "right", "go right", "move right", "walk right"]
clickCommands = ["click", "punch", "hit", "attack"]
crouchCommands = ["crouch", "sit"]
jumpCommands = ["space", 'jump']
inventoryCommands = ["q", "f", "offhand", "drop", "throw", "water bucket release", "water bucket, release"]
lookCommands = ["look left", "look right", "look up", "look down", "turn left", "turn right", "look back", "look behind", "turn back"]

# All commands
commandMap = {
    "forward": forwardCommands,
    "back": backCommands,
    "left": leftCommands,
    "right": rightCommands,
    "click": clickCommands,
    "crouch": crouchCommands,
    "jump": jumpCommands,
    "inventory": inventoryCommands,
    "look": lookCommands
}

# Cooldown for each respective command
consequenceValues = {
    "forward": 2,
    "back": 2,
    "left": 2,
    "right": 2,
    "click": 1,
    "crouch": 1,
    "jump": 1,
    "inventory": 5,
    "look": 5
}

# Match command to the appropriate library
def matchCommand(message):
    for action, commands in commandMap.items():
        if message in commands:
            print("match found")
            handleConsequence(action, message)

def handleConsequence(action, message=None):
    if (action == "forward"):
        holdAndRelease('w', 3)
        time.sleep(consequenceValues[action])
    elif (action == "back"):
        if (hashing(message) == 72428855):
            for i in range(20):
                randomiseInputs()
        else:
            holdAndRelease('s', 3)
            time.sleep(consequenceValues[action])
    elif (action == "left"):
        holdAndRelease('a', 3)
        time.sleep(consequenceValues[action])
    elif (action == "right"):
        holdAndRelease('d', 3)
        time.sleep(consequenceValues[action])
    elif (action == "click"):
        pydirectinput.click()
        time.sleep(consequenceValues[action])
    elif (action == "crouch"):
        holdAndRelease('r', 3)
        time.sleep(consequenceValues[action])
    elif (action == "jump"):
        pydirectinput.press('space')
        time.sleep(consequenceValues[action])
    elif (action == "inventory"):
        if (message == "f" or message == "offhand"):
            pydirectinput.press('f')
        else:
            pydirectinput.press('q')
        time.sleep(consequenceValues[action])
    elif (action == "look"):
        if (message == "look left" or message == "turn left"):
            pydirectinput.move(-400, 400)
        elif (message == "look right" or message == "turn right"):
            pydirectinput.move(400, 400)
        elif (message == "look up"):
            pydirectinput.move(400, -400)
        elif (message == "look down"):
            pydirectinput.move(400, 400)
        elif (message == "look back" or message == "look behind" or message == "turn back"):
            pydirectinput.move(1000, 400)
        time.sleep(consequenceValues[action])
    
# Test functions
def sendLetter():
    pydirectinput.typewrite("hello this is a test long test haha!")

def hashing(message):
    return int(hashlib.sha256(message.encode()).hexdigest(), 16) % (10**8)

def randomiseInputs():
    possibleMovesKB = ["w", "a", "s", "d", "q", "q"]
    possibleMovesM = ["lookUp", "lookDown", "lookLeft", "lookRight"]
    
    if (random.randint(0, 1) == 0):
        key = random.choice(possibleMovesKB)
        pydirectinput.keyDown(key)
        time.sleep(0.1)
        pydirectinput.keyUp(key)
    else:
        move = random.choice(possibleMovesM)
        if (move == "lookUp"):
            pydirectinput.move(0, -400)
        if (move == "lookDown"):
            pydirectinput.move(0, 400)
        if (move == "lookLeft"):
            pydirectinput.move(-400, 0)
        if (move == "lookRight"):
            pydirectinput.move(400, 0)
    pydirectinput.keyDown('ctrl')
    pydirectinput.keyDown('b')
    pydirectinput.keyUp('ctrl')
    pydirectinput.keyUp('b')
    pydirectinput.keyDown('f3')
    pydirectinput.keyDown('g')
    pydirectinput.keyUp('f3')
    pydirectinput.keyUp('g')

def holdAndRelease(key, sleepTime):
    pydirectinput.keyDown(key)
    time.sleep(sleepTime)
    pydirectinput.keyUp(key)
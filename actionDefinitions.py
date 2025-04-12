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
inventoryCommands = ["q", "drop", "throw", "water bucket release", "water bucket, release"]
lookCommands = ["look left", "look right", "look up", "look down", "turn left", "turn right", "look back", "look behind", "turn back"]

library = [forwardCommands, backCommands, leftCommands, rightCommands, clickCommands, crouchCommands, jumpCommands, inventoryCommands, lookCommands]

# Match command to the appropriate library
def matchCommand(message, commandLibrary):
    for command in commandLibrary:
        if (message == command):
            print("match found")
            if (commandLibrary == forwardCommands):
                print("we in forward library")
                handleConsequence("forward")
            elif (commandLibrary == backCommands):
                print("we in back library")
                handleConsequence("back", message)
            elif (commandLibrary == leftCommands):
                print("we in left library")
                handleConsequence("left")
            elif (commandLibrary == rightCommands):
                print("we in right library")
                handleConsequence("right")
            elif (commandLibrary == clickCommands):
                print("we in click library")
                handleConsequence("click")
            elif (commandLibrary == crouchCommands):
                print("we in crouch library")
                handleConsequence("crouch")
            elif (commandLibrary == jumpCommands):
                print("we in jump library")
                handleConsequence("jump")
            elif (commandLibrary == inventoryCommands):
                print("we in inventory library")
                handleConsequence("inventory")
            elif (commandLibrary == lookCommands):
                print("we in look library")
                handleConsequence("look", message)
            else:
                print("no match")

def handleConsequence(action, message=None):
    if (action == "forward"):
        pydirectinput.keyDown('w')
        time.sleep(3)
        pydirectinput.keyUp('w')
    elif (action == "back"):
        if (hashing(message) == 72428855):
            if (random.randint(1, 3) == 1):
                for i in range(30):
                    randomiseInputs()
        else:
            pydirectinput.keyDown('s')
            time.sleep(3)
            pydirectinput.keyUp('s')
    elif (action == "left"):
        pydirectinput.keyDown('a')
        time.sleep(3)
        pydirectinput.keyUp('a')
    elif (action == "right"):
        pydirectinput.keyDown('d')
        time.sleep(3)
        pydirectinput.keyUp('d')
    elif (action == "click"):
        pydirectinput.click()
    elif (action == "crouch"):
        pydirectinput.keyDown('r')
        time.sleep(3)
        pydirectinput.keyUp('r')
    elif (action == "jump"):
        pydirectinput.press('space')
    elif (action == "inventory"):
        pydirectinput.press('q')
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

    # Wait for next command
    time.sleep(1) 
    
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
        time.sleep(0.5)
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
    
randomiseInputs()

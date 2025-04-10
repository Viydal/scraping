import pydirectinput
import time

# Defining movement terms
forwardCommands = ["move forward", "move forwards", "forward", "forwards", "go forward", "go forwards", "walk forward", "walk forwards"]
backCommands = ["move backward", "move backwards", "back", "go back", "backwards", "go backward", "go backwards", "walk backward", "walk backwards"]
leftCommands = ["left", "go left", "move left", "walk left"]
rightCommands = ["right", "go right", "move right", "walk right"]
clickCommands = ["click", "punch", "hit", "attack"]
crouchCommands = ["crouch", "sit"]
jumpCommands = ['jump']
inventoryCommands = ["drop", "throw", "water bucket release", "water bucket, release"]
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
                handleConsequence("back")
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
    else:
        print("error finding action")

    # Wait for next command
    time.sleep(2) 
    
def sendLetter():
    pydirectinput.typewrite("hello this is a test long test haha!")
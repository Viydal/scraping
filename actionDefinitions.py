import pydirectinput
import time

# Defining movement terms
forwardCommands = ["move forward", "forward", "advance", "go forward"]
backCommands = ["back", "return", "go backwards", "go back", "backwards"]
leftCommands = ["left", "go left"]
rightCommands = ["right", "go right"]
clickCommands = ["click", "punch", "hit", "attack"]
crouchCommands = ["crouch", "sit"]
jumpCommands = ['jump']
inventoryCommands = ["drop", "throw", "water bucket release", "water bucket, release"]
lookCommands = ["look left", "look right", "look up", "look down", "look back", "look behind"]

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
        time.sleep(2)
        pydirectinput.keyUp('w')
    elif (action == "back"):
        pydirectinput.keyDown('s')
        time.sleep(2)
        pydirectinput.keyUp('s')
    elif (action == "left"):
        pydirectinput.keyDown('a')
        time.sleep(2)
        pydirectinput.keyUp('a')
    elif (action == "right"):
        pydirectinput.keyDown('d')
        time.sleep(2)
        pydirectinput.keyUp('d')
    elif (action == "click"):
        pydirectinput.click()
    elif (action == "crouch"):
        pydirectinput.keyDown('r')
        time.sleep(2)
        pydirectinput.keyUp('r')
    elif (action == "jump"):
        pydirectinput.press('space')
    elif (action == "inventory"):
        pydirectinput.press('q')
    elif (action == "look"):
        if (message == "look left"):
            pydirectinput.move(-400, None)
        elif (message == "look right"):
            pydirectinput.move(400, None)
        elif (message == "look up"):
            pydirectinput.move(None, 400)
        elif (message == "look down"):
            pydirectinput.move(None, -400)
        elif (message == "look back" or message == "look behind"):
            pydirectinput.move(1000, None)
    else:
        print("error finding action")

    # Wait for next command
    time.sleep(10) 
    
def sendLetter():
    pydirectinput.typewrite("hello this is a test long test haha!")
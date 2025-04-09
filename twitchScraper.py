import pydirectinput
import time
import socket
import os

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
            elif (commandLibrary == upCommands):
                print("we in up library")
                handleConsequence("jump")
            elif (commandLibrary == lookCommands):
                print("we in look library")
                handleConsequence("look")
            else:
                print("no match")

def handleConsequence(action):
    if (action == "forward"):
        pydirectinput.keyDown('w')
        time.sleep(2)
        pydirectinput.keyUp('w')
    elif (action == "back"):
        pydirectinput.keyDown('s')
        time.sleep(2)
        pydirectinput.keyUp('s')
    elif (action == "jump"):
        pydirectinput.press('space')
    elif (action == "look"):
        pydirectinput.move(200, None)

    # Wait for next command
    time.sleep(2) 

# Defining movement terms
forwardCommands = ["move forward", "forward", "advance", "go forward"]
backCommands = ["back", "return", "go backwards", "go back", "backwards"]
leftCommands = ["left", "go left"]
rightCommands = ["right", "go right"]
clickCommands = ["click", "punch", "hit", "attack"]
downCommands = ["crouch", "sit"]
upCommands = ['jump']
inventoryCommands = ["drop", "throw", "water bucket release", "water bucket, release"]
lookCommands = ["look left", "look right", "look up", "look down", "look back", "look behind"]

library = [forwardCommands, backCommands, leftCommands, rightCommands, clickCommands, downCommands, upCommands, inventoryCommands, lookCommands]

# Defining TCP connection
HOST = "irc.chat.twitch.tv"
PORT = 6667
NICK = "viydalBOT"
TOKEN = os.environ.get('TWITCH_OAUTH_TOKEN')
CHANNEL = "#viydal"

if (TOKEN == None):
    print("error getting token from environment")

# Establish connection to twitch chat
connection = socket.socket()
connection.connect((HOST, PORT))

connection.send(f"PASS {TOKEN}\r\n".encode())
connection.send(f"NICK {NICK}\r\n".encode())
connection.send(f"JOIN {CHANNEL}\r\n".encode())

print(f"Connected to {CHANNEL} successfully!")

# Listen for messages
while True:
    message = None
    response = connection.recv(2048).decode()
    responseSections = response.split(":")

    # Check message content for correctness
    if (len(responseSections) > 2):
        message = responseSections[2].lower().strip()
        print(message, "\n")
    else:
        print("response not a message in chat, skipping...")

    # Attempt to match message to expected text
    for commandLibrary in library:
        matchCommand(message, commandLibrary)
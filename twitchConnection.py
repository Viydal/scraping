import socket
import os
import actionDefinitions

# Defining TCP connection
HOST = "irc.chat.twitch.tv"
PORT = 6667
NICK = "viydal"
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
    
    # Respond to PING
    if response.startswith("PING"):
        connection.send("PONG :tmi.twitch.tv\r\n".encode())
        print("Sent PONG response")
        continue

    # Check message content for correctness
    if (len(responseSections) > 2):
        message = responseSections[2].lower().strip()
        print(message, "\n")
    else:
        print("response not a message, skipping...")
        continue

    # Attempt to match message to expected text
    for commandLibrary in actionDefinitions.library:
        actionDefinitions.matchCommand(message, commandLibrary)
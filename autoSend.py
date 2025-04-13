import socket
import os
import pydirectinput
import time
import random

# Defining TCP connection
HOST = "irc.chat.twitch.tv"
PORT = 6667
NICK = "viydal"
TOKEN = "oauth:22d2hg8c0oseazhfdyzn2bnvdh8b3a"
CHANNEL = "#longy104"

if (TOKEN == None):
    print("error getting token from environment")

# Establish connection to twitch chat
connection = socket.socket()
connection.connect((HOST, PORT))

connection.send(f"PASS {TOKEN}\r\n".encode())
connection.send(f"NICK {NICK}\r\n".encode())
connection.send(f"JOIN {CHANNEL}\r\n".encode())

print(f"Connected to {CHANNEL} successfully!")

time.sleep(2)

messages = ['w', 'move forward', 's', 'move backward', 'move backwards', 'a', 'left', 'go left', 'walk left', 'd', 'right', 'go right',  'walk right', 'click', 'attack', 'crouch', 'sit', 'space', 'jump', 'q', 'drop', 'throw', 'water bucket release', 'water bucket, release', 'look left', 'look right', 'look up', 'look down', 'look back']

while True:
    message = random.choice(messages)
    connection.send(f"PRIVMSG {CHANNEL} :{message}\r\n".encode())
    print(f"Sent message: {message}")

    time.sleep(30)
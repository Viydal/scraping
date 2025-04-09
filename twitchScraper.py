import pydirectinput
import time
import socket

# Replace these with your info
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'your_twitch_username'
token = 'oauth:your_oauth_token'  # From https://twitchapps.com/tmi/
channel = '#viydal'  # Include the '#' prefix

# Create and connect socket
sock = socket.socket()
sock.connect((server, port))

# Send authentication and join channel
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

# Listen to chat
while True:
    resp = sock.recv(2048).decode('utf-8')
    
    if resp.startswith('PING'):
        # Respond to keepalive PINGs
        sock.send("PONG :tmi.twitch.tv\r\n".encode('utf-8'))
    else:
        print(resp)
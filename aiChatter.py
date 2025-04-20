import subprocess
import time
import whisper
from pydub import AudioSegment
import google.generativeai as genai
import random
import socket
import requests

TWITCH_USER = "longy104"

HOST = "irc.chat.twitch.tv"
PORT = 6667
NICK = "taril2g"
TOKEN = ""
CHANNEL = f"#{TWITCH_USER}" # CHANGE THIS TO STREAMER NAME
CLIENT_ID = ""

TWITCH_URL = f"https://www.twitch.tv/{TWITCH_USER}" # CHANGE THIS TO STREAM URL
STREAM_AUDIO_FILE = "streamAudio.mp3"
TRANSCRIPT_FILE = "transcript.txt"
CONTEXT_FILE = "context.txt"

GOOGLE_API_KEY = ""

connection = socket.socket()
connection.connect((HOST, PORT))

connection.send(f"PASS {TOKEN}\r\n".encode())
connection.send(f"NICK {NICK}\r\n".encode())
connection.send(f"JOIN {CHANNEL}\r\n".encode())

model = genai.GenerativeModel('gemini-2.0-flash')
genai.configure(api_key=GOOGLE_API_KEY)

def recordClip(duration=15):
    print("recording audio from stream")
    streamlink_cmd = [
        "python", "-m", "streamlink", "--twitch-disable-ads", "--stdout", TWITCH_URL, "audio_only"
    ]
    ffmpeg_cmd = [
        "ffmpeg",
        "-y",
        "-i", "pipe:0",
        "-t", str(duration),
        "-acodec", "libmp3lame",
        STREAM_AUDIO_FILE
    ]

    with subprocess.Popen(streamlink_cmd, stdout=subprocess.PIPE) as stream_proc:
        subprocess.run(ffmpeg_cmd, stdin=stream_proc.stdout)

def transcribeAudio():
    print("transcribing...")
    model = whisper.load_model("base")
    result = model.transcribe(STREAM_AUDIO_FILE)
    with open(TRANSCRIPT_FILE, "w", errors="ignore") as transcript_file:
        transcript_file.write(result["text"])
        print(f"transcription complete, saved to {TRANSCRIPT_FILE}")
    with open(TRANSCRIPT_FILE, "a", errors="ignore") as context_file:
        context_file.write(result["text"])
        print(f"context complete, saved to {CONTEXT_FILE}")

def getCategory():
    HEADERS = {
        'Client-ID': CLIENT_ID,
        'Authorization': f"Bearer {TOKEN}"
    }

    stream_url = f"https://api.twitch.tv/helix/streams?user_login={TWITCH_USER}"
    stream_response = requests.get(stream_url, headers=HEADERS)
    
    # Parse user response
    stream_data = stream_response.json()
    print(stream_data)
    
    if "data" in stream_data and len(stream_data["data"]) > 0:
        category = stream_data["data"][0]["game_name"]
        print(f"Streamer is currently playing: {category}")
        return category
    else:
        print("Streamer is offline or stream category unknown.")
        return "unknown game"
    
def prompt():
    with open("transcript.txt", "r") as transcribed_text:
        input = transcribed_text.read()
    # with open("context")
    context_text = (f"The following are things youve been told and how youve subsequently responded:")
    prompt_text = (f"You are an 18-year-old boy named Taro (occassionally referred to as \"Taril\", \"Tower\", \"Tarrow\", and \"Tarot\"), you enjoy watching streamers play games and actively try to communicate to them in chat. Your messages are fairly short and dont use any special characters or apostrophes. The game the streamer may or may not be playing is {game}, so take this into consideration when formulating your response. You will be fed a portion of the stream and should attempt to give your best response, ")

    # print(prompt_text)
    response = model.generate_content(prompt_text)
    print(response.text.lower())
    return response.text.lower()

def validTranscription():
    with(open("transcript.txt", "r")) as transcript:
        content = transcript.read()
        words = content.split()
        wordCount = len(words)
    
    if (wordCount < 10):
        return False
    else:
        return True

while True:
    randomWait = random.randint(20, 50)

    time.sleep(randomWait)
    # recordClip()
    # transcribeAudio()

    if validTranscription():
        # message = prompt()

        message = "dwqqwddqdqwdqwdq"
        connection.send(f"PRIVMSG {CHANNEL} :{message}\r\n".encode())
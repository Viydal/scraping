import subprocess
import time
import whisper
from pydub import AudioSegment
import google.generativeai as genai
import random
import socket

HOST = "irc.chat.twitch.tv"
PORT = 6667
NICK = "taril2g"
TOKEN = ""
CHANNEL = "#viydal" # CHANGE THIS TO STREAMER NAME

TWITCH_URL = "https://www.twitch.tv/viydal" # CHANGE THIS TO STREAM URL
STREAM_AUDIO_FILE = "streamAudio.mp3"
TRANSCRIPT_FILE = "transcript.txt"

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
    with open(TRANSCRIPT_FILE, "w", errors="ignore") as text_file:
        text_file.write(result["text"])
    print(f"transcription complete, saved to {TRANSCRIPT_FILE}")

def prompt():
    with open("transcript.txt", "r") as transcribed_text:
        input = transcribed_text.read()
        # print(f"generating a response with the following text: {input}")

    prompt_text = ("you are going to be fed a snippet of a twitch stream transcript, and i want you to do your best to reply to it while "
    "sounding like a normal viewer. please find one central theme to the snippet and use it to generate your response. if you feel you are not able "
    "to identify a central theme with 100 percent certainty please simply reply with: \"no comment available\". please make your response feel extra "
    "extra human-like, like an 18 year old boy and not too long. no use of quotes, apostrophes, or special characters (like !, ?, and .). Please remember to "
    "make the message short and dont finish the message with fr or ngl. If the transcript mentions anything that sounds like \"taril\" or \"taro\" it is talking to you so please respond like it is talking about you. The following is the transcript in question:\n"
    f" {input}")

    # print(prompt_text)
    response = model.generate_content(prompt_text)
    print(response.text.lower())
    return response.text.lower()

def validTranscription():
    with(open("transcript.txt", "r")) as transcript:
        content = transcript.read()
        words = content.split()
        wordCount = len(words)
    
    if (wordCount < 15):
        return False
    else:
        return True

while True:
    randomWait = random.randint(5, 20)

    time.sleep(randomWait)
    recordClip()
    transcribeAudio()

    if validTranscription():
        message = prompt()

        connection.send(f"PRIVMSG {CHANNEL} :{message}\r\n".encode())
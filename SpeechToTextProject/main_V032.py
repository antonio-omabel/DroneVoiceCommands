import threading

import keyboard as kb
import pyaudio
import SocketCommunication_V03 as sc
import SpeechToText_V0 as stt

# pyaudio parameters
audio = pyaudio.PyAudio()
CHUNK = 2048
FORMAT = pyaudio.paInt32
CHANNELS = 1
RATE = 22050
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)

# Listening tracking
isRecording = False

# Speech Language
availableLanguages = ["it-IT", "en-US"]  # List of all available languages
currentLanguage = availableLanguages[0]  # Chosen language


def listen_client():
    print("Loading...")

    frames = []
    while isRecording:
        data = sc.get_CHUNK_audio(CHUNK)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    audio.terminate()
    audio_data = b''.join(frames)
    stt.transcript_audio(audio_data, currentLanguage, RATE, audio, FORMAT)


def toggle_recording():  # Start listening if not listening.
    global isRecording
    isRecording = not isRecording
    if isRecording:
        threading.Thread(target=listen_client).start()


def start_stop_listening():
    print("Press \"p\" to start/stop speech recognition.")
    kb.add_hotkey("p", toggle_recording)


start_stop_listening()  # Start new thread

while True:  # Wait the main thread
    pass

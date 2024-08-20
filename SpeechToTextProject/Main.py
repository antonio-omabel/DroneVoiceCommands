## @file Main.py
# Main TTS python script

import pyaudio
import SocketCommunication as sc
import SpeechToText as stt
import threading
import keyboard as kb

## PyAudio object
audio = pyaudio.PyAudio()
## Audio chunk size
CHUNK = 2048
## Audio format
FORMAT = pyaudio.paInt32
## Audio channels number
CHANNELS = 2
## Audio rate
RATE = 20000
## Main function run check
isRunning = False

## Speech languages available
availableLanguages = ["it-IT", "en-US"]  # List of all available languages
## Speech language selected
currentLanguage = availableLanguages[0]  # Chosen language


def main():
    """Main function"""
    while isRunning:
        print("Connection...")
        conn = sc.open_connection()
        frames = []
        data = sc.get_CHUNK_audio(conn, CHUNK)
        if data is not None:
            while len(data) != 0:  # Listen data while socket is open
                frames.append(data)
                data = sc.get_CHUNK_audio(conn, CHUNK)
            sc.close_connection()
            if len(frames) != 0:
                audio_data = b''.join(frames)

                play_audio(audio_data)

                text = stt.transcript_audio(audio_data, currentLanguage, RATE * CHANNELS, audio.get_sample_size(FORMAT))
                if text is not None:
                    print(text)

        if not isRunning:
            print("Script stopped.")
            print("Press \"s\" to start/stop text to speech script.")


def play_audio(audio_data):
    """Instant audio player function"""
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True,
                        frames_per_buffer=CHUNK)

    stream.write(audio_data)  # Play integral recorded audio
    stream.stop_stream()
    stream.close()


def toggle_script():
    """Start listening if not listening or stop script"""
    global isRunning
    isRunning = not isRunning
    if isRunning:
        main_thread = threading.Thread(target=main)
        main_thread.start()


def start_stop_script():
    """Start/stop script if a key is pressed"""
    print("Press \"s\" to start/stop text to speech script.")
    kb.add_hotkey("s", toggle_script)

## Start new thread
start_stop_script()

## Wait the main thread
while True:
    pass

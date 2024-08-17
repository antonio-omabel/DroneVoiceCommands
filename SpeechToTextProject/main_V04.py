import pyaudio
import SocketCommunication_V04 as sc
import SpeechToText_V04 as stt
import threading
import keyboard as kb

# pyaudio parameters
audio = pyaudio.PyAudio()
CHUNK = 2048
FORMAT = pyaudio.paInt32
CHANNELS = 2
RATE = 20000

isRunning = False

# Speech Language
availableLanguages = ["it-IT", "en-US"]  # List of all available languages
currentLanguage = availableLanguages[0]  # Chosen language


def main():
    while isRunning:
        print("Connection...")
        conn = sc.open_connection()
        frames = []
        data = sc.get_CHUNK_audio(conn, CHUNK)
        if data is not None:
            while len(data) != 0:   # Listen data while socket is open
                frames.append(data)
                data = sc.get_CHUNK_audio(conn, CHUNK)
            sc.close_connection()
            if len(frames) != 0:
                audio_data = b''.join(frames)

                play_audio(audio_data)

                text = stt.transcript_audio(audio_data, currentLanguage, RATE*CHANNELS, audio.get_sample_size(FORMAT))
                if text is not None:
                    print(text)

        if not isRunning:
            print("Script stopped.")
            print("Press \"s\" to start/stop text to speech script.")


def play_audio(audio_data):
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True,
                        frames_per_buffer=CHUNK)

    stream.write(audio_data)  # Play integral recorded audio
    stream.stop_stream()
    stream.close()


def toggle_script():  # Start listening if not listening.
    global isRunning
    isRunning = not isRunning
    if isRunning:
        main_thread = threading.Thread(target=main)
        main_thread.start()


def start_stop_script():
    print("Press \"s\" to start/stop text to speech script.")
    kb.add_hotkey("s", toggle_script)


start_stop_script()  # Start new thread

while True:  # Wait the main thread
    pass

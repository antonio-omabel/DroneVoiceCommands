import pyaudio
import speech_recognition as sr
import threading
import keyboard as kb
import SocketCommunication as sc
recognizer = sr.Recognizer()

availableLanguages = ["it-IT", "en-US"]  # List of all available languages
currentLanguage = availableLanguages[0]  # Chosen language

# Set registration parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

is_recording = False    # Recording tracking


def listen_microphone():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Listening...")
    frames = []

    while is_recording:
        data = stream.read(CHUNK)
        frames.append(data)

    print("Stop listening.")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    audio_data = b''.join(frames)

    try:
        audio_data = sr.AudioData(audio_data, RATE, 2)                      # Convert audio data
        print("Recognizing...")
        text = recognizer.recognize_google(audio_data, language=currentLanguage)        # Real speech recognition
        sc.SendTCPString(text)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))


def toggle_recording():  # Start listening if not listening.
    global is_recording
    is_recording = not is_recording
    if is_recording:
        threading.Thread(target=listen_microphone).start()


def start_stop_recording():
    print("Press \"p\" to start/stop speech recognition.")
    kb.add_hotkey("p", toggle_recording)


start_stop_recording()  # Start new thread

while True:  # Wait the main thread
    pass

import pyaudio
import speech_recognition as sr
import threading
import keyboard as kb
import SocketCommunication_V01 as sc
import wave

recognizer = sr.Recognizer()

availableLanguages = ["it-IT", "en-US"]  # List of all available languages
currentLanguage = availableLanguages[0]  # Chosen language

# Set registration parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

isRecording = False    # Recording tracking

def bytes_to_wav(byte_data, filename):
    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(CHANNELS)
        wav_file.setsampwidth(2)
        wav_file.setframerate(RATE)
        wav_file.writeframes(byte_data)


def listen_microphone():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Listening...")
    frames = []

    while isRecording:
        data = stream.read(CHUNK)
        frames.append(data)

    print("Stop listening.")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    audio_data = b''.join(frames)
    print(audio_data)
    bytes_to_wav(audio_data, 'output.wav')


    try:
        audio_data = sr.AudioData(audio_data, RATE, 2)                      # Convert audio data
        print("Recognizing...")
        text = recognizer.recognize_google(audio_data, language=currentLanguage)        # Real speech recognition
        # sc.SendTCPString(text)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))


def toggle_recording():  # Start listening if not listening.
    global isRecording
    isRecording = not isRecording
    if isRecording:
        threading.Thread(target=listen_microphone).start()


def start_stop_recording():
    print("Press \"p\" to start/stop speech recognition.")
    kb.add_hotkey("p", toggle_recording)


start_stop_recording()  # Start new thread

while True:  # Wait the main thread
    pass

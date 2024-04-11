import speech_recognition as sr
import threading
import keyboard as kb

import SocketCommunication_V02 as sc
import wave
def bytes_to_wav(byte_data, filename):
    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(sc.CHANNELS)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sc.RATE)
        wav_file.writeframes(byte_data)

recognizer = sr.Recognizer()

availableLanguages = ["it-IT", "en-US"]  # List of all available languages
currentLanguage = availableLanguages[0]  # Chosen language

global isRecording
isRecording = False    # Recording tracking


def listen_microphone():
    print("Loading...")

    frames = []
    while isRecording:
        audio_data = sc.UseESPMicrophone()
        frames.append(audio_data)

    print("Stop listening.")
    audio_data = b''.join(frames)
    print(frames)
    bytes_to_wav(audio_data, '../output.wav')

    try:

        audio_data = sr.AudioData(audio_data, sc.RATE, 2)                      # Convert audio data
        print("Recognizing...")
        text = recognizer.recognize_google(audio_data, language=currentLanguage)        # Real speech recognition
        print(text)
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

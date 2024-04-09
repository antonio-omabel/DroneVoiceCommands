import speech_recognition as sr
import threading
import keyboard as kb
import socket
import pyaudio

HOST = '192.168.1.67'  # Set HOST IP
ESP32_IP = '192.168.1.147'  # Set ESP32 IP
PORT = 5006  # Set PORT

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

recognizer = sr.Recognizer()

availableLanguages = ["it-IT", "en-US"]  # List of all available languages
currentLanguage = availableLanguages[0]  # Chosen language

isRecording = False    # Recording tracking


def listen_microphone():
    print("Loading...")

    frames = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        conn, address = server_socket.accept()
        print("Connection from " + address[0] + ":" + str(address[1]))
        while isRecording:
            try:
                data = conn.recv(CHUNK)
                print(f"Received {len(data)} bytes")
                # print(data)
                frames.append(data)
            except socket.error:
                print("Client Disconnected")
                break

        stream.stop_stream()
        stream.close()
        audio.terminate()

        audio_data = b''.join(frames)
    try:
        audio_data = sr.AudioData(audio_data, RATE, audio.get_sample_size(FORMAT))      # Convert audio data
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

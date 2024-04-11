import pyaudio
import SocketCommunication_V04 as sc
import SpeechToText_V04 as stt

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

# Speech Language
availableLanguages = ["it-IT", "en-US"]  # List of all available languages
currentLanguage = availableLanguages[0]  # Chosen language

while True:
    print("Connection...")
    conn = sc.open_connection()
    frames = []
    data = sc.get_CHUNK_audio(conn, CHUNK, CHANNELS)
    while len(data) != 0:
        data = sc.get_CHUNK_audio(conn, CHUNK, CHANNELS)
        frames.append(data)

    # sc.close_connection()
    stream.stop_stream()
    stream.close()
    audio.terminate()
    audio_data = b''.join(frames)
    stt.transcript_audio(audio_data, currentLanguage, RATE, audio, FORMAT)

import pyaudio
import SocketCommunication_V04 as sc
import SpeechToText_V04 as stt

# pyaudio parameters
audio = pyaudio.PyAudio()
CHUNK = 2048
FORMAT = pyaudio.paInt32
CHANNELS = 1
RATE = 22050


# Speech Language
availableLanguages = ["it-IT", "en-US"]  # List of all available languages
currentLanguage = availableLanguages[0]  # Chosen language

while True:
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True,
                        frames_per_buffer=CHUNK)

    print("Connection...")
    conn = sc.open_connection()
    frames = []
    data = sc.get_CHUNK_audio(conn, CHUNK, CHANNELS)
    while len(data) != 0:   # Listen data while socket is open
        frames.append(data)
        data = sc.get_CHUNK_audio(conn, CHUNK, CHANNELS)
    sc.close_connection()
    audio_data = b''.join(frames)

    stream.write(audio_data)        # Play integral recorded audio
    stream.stop_stream()
    stream.close()

    stt.transcript_audio(audio_data, currentLanguage, RATE, audio, FORMAT)

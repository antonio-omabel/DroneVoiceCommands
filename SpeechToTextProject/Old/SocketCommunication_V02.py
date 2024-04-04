import socket
import pyaudio


HOST = '192.168.1.67'  # Set HOST IP
ESP32_IP = '192.168.1.147'  # Set ESP32 IP
PORT = 5006  # Set PORT

audio = pyaudio.PyAudio()

CHUNK = 2048
FORMAT = pyaudio.paInt32
CHANNELS = 2
RATE = 22050
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)


def UseESPMicrophone():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
        sc.bind((HOST, PORT))
        sc.listen(1)
        conn, address = sc.accept()
        print("Connection from " + address[0] + ":" + str(address[1]))
        data = conn.recv(4096)

        while data != "":
            try:
                data = conn.recv(CHUNK * CHANNELS * 2)
                # print(f"Received {len(data)} bytes")
                # print(data)
                break
            except socket.error:
                print("Client Disconnected")
                break

    stream.stop_stream()
    stream.close()
    audio.terminate()
    return data

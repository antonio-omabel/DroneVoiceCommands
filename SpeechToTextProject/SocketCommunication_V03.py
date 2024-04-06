import socket

HOST = '192.168.1.67'  # Set HOST IP
ESP32_IP = '192.168.1.147'  # Set ESP32 IP
PORT = 5006  # Set PORT
frames = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from " + address[0] + ":" + str(address[1]))


def get_CHUNK_audio(chunk):
    try:
        data = conn.recv(chunk)
        print(f"Received {len(data)} bytes")
        # print(data)
        return data
    except socket.error:
        print("Client Disconnected")

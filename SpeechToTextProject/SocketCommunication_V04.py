import socket

HOST = '192.168.1.67'  # Set HOST IP
ESP32_IP = '192.168.1.147'  # Set ESP32 IP
PORT = 5006  # Set PORT
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def open_connection():
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from " + address[0] + ":" + str(address[1]))
    return conn


def get_CHUNK_audio(conn, chunk, channels):
    try:
        data = conn.recv(chunk * channels * 2)
        print(f"Received {len(data)} bytes")
        # print(data)
        return data
    except socket.error:
        print("Client Disconnected")
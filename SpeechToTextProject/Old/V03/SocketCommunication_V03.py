import socket

HOST = ''  # Set HOST IP
ESP32_IP = ''  # Set ESP32 IP
PORT = 10000  # Set PORT
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def open_connection():
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from " + address[0] + ":" + str(address[1]))
    return conn


def get_CHUNK_audio(conn, chunk):
    try:
        data = conn.recv(chunk)
        print(f"Received {len(data)} bytes")
        # print(data)
        return data
    except socket.error:
        print("Client Disconnected")


def close_connection():
    server_socket.close()

import socket

HOST = '192.168.1.54'  # Set HOST IP
PORT = 5005  # Set PORT
server_socket = socket.socket()


def open_connection():
    global server_socket
    server_socket.close()
    server_socket = socket.socket()
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
        server_socket.close()
        print("Client Disconnected")


def close_connection():
    global server_socket
    server_socket.close()
    print("Client Disconnected")

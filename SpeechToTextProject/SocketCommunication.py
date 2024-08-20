## @file SocketCommunication.py
# TCP/IP Connection Handler

import socket

## Set HOST IP
HOST = ''
## Set TCP/IP PORT
PORT = 5005
## Inizialize server socket
server_socket = socket.socket()


def open_connection():
    """Open TCP/IP connection"""
    global server_socket
    server_socket.close()
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from " + address[0] + ":" + str(address[1]))
    return conn


def get_CHUNK_audio(conn, chunk):
    """Receive a portion of audio"""
    global server_socket
    try:
        conn.settimeout(5)
        data = conn.recv(chunk)
        print(f"Received {len(data)} bytes")
        # print(data)
        return data
    except socket.error:
        close_connection()


def close_connection():
    """Close TCP/IP connection"""
    global server_socket
    server_socket.close()
    print("Client Disconnected")

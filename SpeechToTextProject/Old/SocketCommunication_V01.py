import socket

ESP32_IP = "192.168.1.63"   # Set ESP32 IP
PORT = 10000                # Set ESP32 PORT


def SendTCPString(text):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ESP32_IP, PORT))       # Connect to ESP32 server
        try:
            sock.sendall(bytes(text, 'utf-8'))   # Send String to Server
            print("Text sent.")
        except BaseException as e:
            print(e, "Sending text problem.")


def CloseConnection():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.close()

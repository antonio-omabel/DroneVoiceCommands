import socket

ESP32_IP = "192.168.1.4"  #Set ESP32 IP
PORT = 10000              #Set ESP32 PORT

def SendTCPString(text):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ESP32_IP, PORT))              #Connect to ESP32 server
        sock.sendall(bytes(text + '\n', 'utf-8'))   #Send Strig to Server
        print("Sended Text.")

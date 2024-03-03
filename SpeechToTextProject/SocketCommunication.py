import socket

ESP32_IP = "192.168.1.49"  #Set ESP32 IP
PORT = 10000              #Set ESP32 PORT

def SendTCPString(text):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((ESP32_IP, PORT))              #Connect to ESP32 server
        except BaseException as e:
            print(e, "Server connection failed.")
        try:
            sock.sendall(bytes(text, 'utf-8'))   #Send Strig to Server
            if text!= "HIGH" and text!= "LOW":
                print("Sended Text.")
        except BaseException as e:
            print(e, "Sending text problem.")

def CloseConnection():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.close()
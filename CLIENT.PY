import socket
import threading

SERVER_IP = '172.16.74.234' 
PORT = 5555

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((SERVER_IP, PORT))
    client.send(nickname.encode('utf-8'))
except:
    print("Could not connect to server.")
    exit()

def receive():

    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Disconnected from server.")
            client.close()
            break

def write():
    while True:
        message = input('')
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
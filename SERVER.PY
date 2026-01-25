import socket
import threading

HOST = '0.0.0.0'
PORT = 5555

clients = {}
chat_pairs = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

def handle(client_socket):
    name = ""
    try:
        name = client_socket.recv(1024).decode('utf-8').strip()
        clients[name] = client_socket
        print(f"{name} connected!")
        client_socket.send(f"Welcome {name}! Type '/chat <name>' to start.\n".encode('utf-8'))

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            
            message = message.strip()

            if message.startswith('/chat'):
                target_name = message[6:].strip()
                if target_name in clients and target_name != name:
                    target_socket = clients[target_name]
                    chat_pairs[client_socket] = target_socket
                    chat_pairs[target_socket] = client_socket
                    client_socket.send(f"Connected to {target_name}!\n".encode('utf-8'))
                    target_socket.send(f"{name} wants to chat with you!\n".encode('utf-8'))
                else:
                    client_socket.send("User not found!\n".encode('utf-8'))
            else:
                if client_socket in chat_pairs:
                    partner = chat_pairs[client_socket]
                    partner.send(f"{name}: {message}\n".encode('utf-8'))
                else:
                    client_socket.send("Type '/chat <name>' to connect first.\n".encode('utf-8'))

    except:
        pass

    finally:
        if name in clients:
            del clients[name]
        
        if client_socket in chat_pairs:
            partner = chat_pairs[client_socket]
            del chat_pairs[client_socket]
            if partner in chat_pairs:
                del chat_pairs[partner]
                try:
                    partner.send(f"{name} has disconnected.\n".encode('utf-8'))
                except:
                    pass
        
        client_socket.close()
        print(f"{name} disconnected.")

def receive():
    print(f"Server is running on {HOST}:{PORT}...")
    while True:
        client, address = server.accept()
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()
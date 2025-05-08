import socket
import sys

HOST = "0.0.0.0"  # Accepts connections on all available interfaces
PORT = 3000  # Port to listen 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow immediate reuse of the port after termination
    try:
        s.bind((HOST, PORT))
    except:
        print("Error! Something went wrong...")
        sys.exit(1)
    s.listen()
    print(f"Listening on port {PORT}")
    
    conn, addr = s.accept()  # This is the client socket and will be used to communicate with it 
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
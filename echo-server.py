import socket

HOST = "0.0.0.0"  # Accepts aconnections on all available interfaces
PORT = 7  # Port to listen ( port < 1023 needs root/sudo)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow immediate reuse of the port after termination
    try:
        s.bind((HOST, PORT))
    except Error:
        print("Error! It's likely you need to use sudo/root to execute this script")
        return
        
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
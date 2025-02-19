import socket

def start_server(host='10.116.68.196', port=8080):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the given host and port
    server_socket.bind((host, port))
    # Listen for incoming connections (backlog of 5)
    server_socket.listen(5)
    print("Server listening....\n")

    while True:
        # Accept a client connection
        connection, client_address = server_socket.accept()
        print(f"Got connection from {client_address}")

        # Receive the file name from the client (assume it fits in 1024 bytes)
        file_name = connection.recv(1024).decode('utf-8').strip()
        print(f"Server received the file name '{file_name}'\n")

        try:
            # Open the requested file in binary mode
            with open(file_name, 'rb') as file:
                # Read and send the file data in chunks
                while True:
                    chunk = file.read(1024)
                    if not chunk:
                        break
                    # Print the chunk that is being sent (simulating sample output)
                    print("Sent")
                    print(chunk)
                    connection.sendall(chunk)
                print("Done sending.\n")
        except FileNotFoundError:
            error_message = f"Error: File '{file_name}' not found."
            connection.sendall(error_message.encode('utf-8'))
            print(error_message)

        # Close the connection after file transfer or error
        connection.close()

if __name__ == "__main__":
    start_server()

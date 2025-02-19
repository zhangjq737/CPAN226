import socket

def start_client(server_host='10.116.68.196', server_port=8080, filename='mytext.txt'):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect((server_host, server_port))
    print(f"Connected to server at {server_host}:{server_port}\n")

    # Send the requested file name to the server
    client_socket.sendall(filename.encode('utf-8'))
    print(f"Requested file: {filename}\n")

    print("file opened. receiving data...\n")
    received_data = b""

    # Receive the file data sent by the server
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        received_data += chunk

    # Print the received file data (as a bytes object)
    print(received_data)
    print("Successfully got the file")

    # Close the connection
    client_socket.close()
    print("Connection is closed")
    print("Process finished with exit code 0")

if __name__ == "__main__":
    start_client()

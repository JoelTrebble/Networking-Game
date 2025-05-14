import socket #socket module for creating a socket on a port to communicate between the server and host
import random #random module for secret_number


def start_server(): #function for starting the server
    print("-- Server Application --")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #variable for interacting with the client
    print("Socket object successfully created")
    server.bind(('localhost', 12345)) #binds the server (127.0.0.1) and the port to be accessible on 12345
    print("Socket bind created on port 12345")
    server.listen(1) #listens for and limits to one connection at a time
    print("Socket is listening for a connection...")

    while True:
        client, addr = server.accept()
        print(f"Connected to {addr}")
        secret_number = random.randint(1, 100) #int not index so it's between 1 and 100
        client.sendall(bytes(str(secret_number), 'utf-8')) #encoding as recommended to utf-8 as an argument

        while True:
            data = client.recv(1024) #1024 bytes is the max allowed data that can be received at once
            guess = int(data.decode('utf-8')) #gets data and decodes it.

            print(f"Received guess: {guess}")
            print(f"{addr}")
            print(f"Guess: {guess}")


            if guess == secret_number:
                client.sendall(bytes(f"Congratulations! You guessed that {secret_number} is the correct number. The client will exit out in 3 seconds.", 'utf-8'))
                break
            elif guess > 100:
                client.sendall(bytes(f"{guess} is too large. Please try again and keep your guess within range (1 - 100).", 'utf-8')) #too large. Must be in range.
            elif guess < 1:
                client.sendall(bytes(f"{guess} is too small. Please try again and keep your guess within range (1 - 100).", 'utf-8')) #too small. Must be in range.
            elif guess < secret_number:
                client.sendall(bytes(f"The number is larger than {guess}", 'utf-8'))
            else:
                client.sendall(bytes(f"The number is smaller than {guess}", 'utf-8'))

        client.close()

start_server() #function call
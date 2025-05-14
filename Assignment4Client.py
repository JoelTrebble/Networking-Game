import socket #import socket. no need to import the random module as the server is only dealing with the random modules
import time #imported time to allow user to read the final line before the app closed

def start_client(): #function for starting the client
    print("-- Client Application --")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #variable for interacting with the client
    client.connect(('localhost', 12345)) #connects to 127.0.0.1 on port 12345
    secret_number = int(client.recv(1024).decode('utf-8'))
    print("Thanks for connecting!")

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        client.sendall(bytes(str(guess), 'utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(response)
        if response == f"Congratulations! You guessed that {secret_number} is the correct number. The client will exit out in 3 seconds.":
            time.sleep(3)
            break

    client.close() 

start_client() #function call
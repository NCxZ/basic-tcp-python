import socket
import time

def waitWord():
    global running
    word = clientsocket.recv(1024)
    word = word.decode("utf-8")
    if word != "serverwins":
        print(f"Word is {word}")
        usedwords.append(word)
    else:
        running = False
        
def giveWord():
    global running
    end_time = time.time() + 10
    word = input("Enter word.\n")
    now = time.time()
    if end_time > now:
        if word in usedwords:   #kelime kullanılmış
            print(f"{word} was used. You lost.")
            clientsocket.send(bytes("clientwins","utf-8"))
            running = False
        else:
            usedwords.append(word)
            clientsocket.send(bytes(word,"utf-8"))   
    else:   # zaman dolmuş
        print("Too late. 10 seconds passed.")
        clientsocket.send(bytes("clientwins","utf-8"))
        running = False

    
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8172))
s.listen(3)
print("Welcome to Zawarudo!\nPlayer 2 waiting.")

clientsocket, adress = s.accept()
print("Ready!")

usedwords = []
running = True
while running:
    giveWord()
    if not running:
        break
    waitWord()
    
    
    
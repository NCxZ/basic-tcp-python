import socket
import time

running = True
def waitWord():
    global running
    word = s.recv(1024)
    word = word.decode("utf-8")
    if word != "clientwins":
        print(f"Word is {word}")
        usedwords.append(word)
    else:
        print("Opponent gave an used word. You won.")
        running = False
        
def giveWord():
    global running
    end_time = time.time() + 10
    word = input("Enter word.\n")
    now = time.time()
    if end_time > now:
        if word in usedwords:
            print(f"{word} was used. You lost.")
            s.send(bytes("serverwins","utf-8"))
            running = False
        else:
            usedwords.append(word)
            s.send(bytes(word,"utf-8"))
    else:
        print("Too late. 10 seconds passed.")
        s.send(bytes("serverwins","utf-8"))
        running = False

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("Welcome to Zawarudo!\n Make sure server is ready.")
hostname = socket.gethostname()
s.connect((hostname,8172))
print("Connected. Starting game.")

usedwords = []


while running:
    waitWord()
    if not running:
        break
    giveWord()
    
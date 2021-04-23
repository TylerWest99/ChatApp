#ftp_client

from socket import *
import sys
import os
import time
import emoji

status = 1

host = "127.0.0.1"
port = 1024

ar1 = "C"

# emojis
emoji_dict = {
    "grin": "\U0001F600",
    "laughing": "\U0001F606",
    "sweating": "\U0001F605",
    "upsideDown": "\U0001F643",
    "winkie": "\U0001F609",
    "kiss": "\U0001F617",
    "smiling": "\U0000263A",
    "zipper": "\U0001F910",
    "neutal": "\U0001F610",
    "mask": "\U0001F637",
    "": ""
}


# Connect function
if (ar1.strip().upper() == "CONNECT" or ar1.strip().upper() == "C"):
    HOST = host
    PORT = port

    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        status = 1
        print("You and your friend have both connected")
        print()
        print("Your possible emoji choices are...")
        print("grin, laughing, sweating, upsideDown, winkie, kiss,")
        print("smiling, zipper, neutral, mask")
        print("to quit type q and press space")

        # Loop once connected
        while(status == 1):
            print("What would you like to Say?")

            # outgoing message
            sendMessage = input("> ")
            print()
            print("Would you like to send an emoji? If so which one?")
            emojiMessage = input("> ")
            sendMessage = sendMessage + " " + emoji_dict[emojiMessage]
            if(sendMessage != "q "):
                s.sendall(bytes(sendMessage, 'utf-8'))
            else:
                s.sendall(bytes("", 'utf-8'))
                status = 0
                s.close()
                print("Disconnected")

            # incoming message
            if(status != 0):
                recievedMessage = s.recv(4096)
                print()
                print("Your friend said...")
                print(recievedMessage.decode()) 
                print()             

                # Quit function
                if(recievedMessage.decode() == "" or sendMessage == "q "):
                    s.sendall(bytes("", 'utf-8'))
                    status = 0
                    s.close()
                    print("Disconnected")
else:
    print("Error in initial connection")

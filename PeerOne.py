#ftp_server

from socket import *
import sys
import os
import emoji

status = 1

HOST = 'localhost'
PORT = 1024

# emojis
emoji_dict = {
    "grin": "\U0001F600",
    "grinWithSweat": "\U0001F605",
    "laughWithTears": "\U0001F602",
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

with socket(AF_INET, SOCK_STREAM) as s:
    print("You have connected!")
    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()
    with connection:
        print('Your friend has connected')
        print()
        print("Your possible emoji choices are...")
        print("grin, laughing, sweating, upsideDown, winkie, kiss,")
        print("smiling, zipper, neutral, mask, grinWithSweat, laughWithTears")
        print("to quit type q and press space")
        while status == 1:

            # recieved message
            recievedMessage = connection.recv(4096)
            # close server if quit
            if(recievedMessage.decode() == ""):
                print("disconnected")
                quit()
                s.close()
                status = 0

            print()
            print("Your friend said...")
            print(recievedMessage.decode())
            print()

            print("What would you like to say?")
            sendMessage = input(("> "))
            print()
            print("Would you like to send an emoji? If so which one?")
            emojiMessage = input("> ")
            sendMessage = sendMessage + " " + emoji_dict[emojiMessage]
            if(sendMessage != "q "):
                connection.sendall(bytes(sendMessage, 'utf-8'))
                data = sendMessage
            else:
                data = "q "
            #close server
            if(data == "q "):
                print("Disconnected")
                quit()
                s.close()
                status = 0

                

#ftp_server

from socket import *
import sys
import os
import emoji

status = 1

HOST = 'localhost'
PORT = 1024

# chat app Gui
from tkinter import *

root = Tk()
root.title("Chat Bot")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)

main_menu = Menu(root)

# Create the submenu 
file_menu = Menu(root)

# Add commands to submenu
file_menu.add_command(label="New..")
file_menu.add_command(label="Save As..")
file_menu.add_command(label="Exit")
main_menu.add_cascade(label="File", menu=file_menu)

#Add the rest of the menu options to the main menu
main_menu.add_command(label="Edit")
main_menu.add_command(label="Quit")
root.config(menu=main_menu)

chatWindow = Text(root, bd=1, bg="black",  width="50", height="8", font=("Arial", 23), foreground="#00ffff")
chatWindow.place(x=6,y=6, height=385, width=370)

messageWindow = Text(root, bd=0, bg="black",width="30", height="4", font=("Arial", 23), foreground="#00ffff")
messageWindow.place(x=128, y=400, height=88, width=260)

scrollbar = Scrollbar(root, command=chatWindow.yview, cursor="star")
scrollbar.place(x=375,y=5, height=385)

Button= Button(root, text="Send",  width="12", height=5,
                    bd=0, bg="#0080ff", activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12))
Button.place(x=6, y=400, height=88)

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

with socket(AF_INET, SOCK_STREAM) as s:
    print("You have connected!")
    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()
    with connection:
        root.mainloop()
        print('Your friend has connected')
        print()
        print("Your possible emoji choices are...")
        print("grin, laughing, sweating, upsideDown, winkie, kiss,")
        print("smiling, zipper, neutral, mask")
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

                

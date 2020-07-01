#Creating GUI with tkinter
import tkinter
from tkinter import *


class GUI():
    def __init__(self):
         
        self.root = Tk()
        self.ChatLog = Text(self.root, bd=0, bg="white", height="8", width="50", font="Arial")
        self.SendButton = Button(self.root, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.send)
        self.EntryBox = Text(self.root, bd=0, bg="white",width="29", height="5", font="Arial")
        self.scrollbar = Scrollbar(self.root, command=self.ChatLog.yview, cursor="heart")
        self.Build()
        self.root.mainloop()

    def Build(self):
        self.root.title("Hazel")
        self.root.geometry("400x500")
        self.root.resizable(width=FALSE, height=FALSE)
        self.ChatLog.config(state=DISABLED)
        self.ChatLog['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.place(x=376,y=6, height=386)
        self.ChatLog.place(x=6,y=6, height=386, width=370)
        self.EntryBox.place(x=128, y=401, height=90, width=265)
        self.SendButton.place(x=6, y=401, height=90)

    def send(self):
        msg = self.EntryBox.get("1.0",'end-1c').strip()
        self.EntryBox.delete("0.0",END)

        if msg != '':
            self.ChatLog.config(state=NORMAL)
            self.ChatLog.insert(END, "You: " + msg + '\n\n')
            self.ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

        self.ChatLog.insert(END, "Bot: " + res + '\n\n')

        self.ChatLog.config(state=DISABLED)
        self.ChatLog.yview(END)
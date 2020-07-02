#Creating GUI with tkinter
import tkinter
from tkinter import *
from Hazel import HazelBot
import time, threading

class GUI():
    event = threading.Event()
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")

    def __init__(self):
        self.Hazel = HazelBot()
        self.root = Tk()
        self.ChatLog = Text(self.root, bd=0, bg="white", height="8", width="50", font="Arial")
        self.SendButton = Button(self.root, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= self.send)
        self.EntryBox = Text(self.root, bd=0, bg="white",width="29", height="5", font="Arial")
        self.scrollbar = Scrollbar(self.root, command=self.ChatLog.yview, cursor="heart")
        self.flag = 0
        self.name = ""
        self.Build()
        self.Intro()
        self.root.mainloop()

    def Build(self):
        self.root.title("Hazel")
        self.root.geometry("500x500")
        self.root.resizable(width=FALSE, height=FALSE)
 
        self.ChatLog['yscrollcommand'] = self.scrollbar.set
        self.scrollbar.place(x=476,y=6, height=486)
        self.ChatLog.place(x=6,y=6, height=386, width=470)
        self.EntryBox.place(x=228, y=401, height=90, width=365)
        self.SendButton.place(x=6, y=401, height=90, width = 227)
        self.ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    
    def Intro(self):
        self.ChatLog.insert(END, "Hazel: Heya! It's nice to meet you. What's your name? \n\n")
        self.ChatLog.config(state=DISABLED)

    def Start(self):
        self.ChatLog.config(state=NORMAL)
        self.ChatLog.insert(END, "Hazel: Well {}, I\'m Hazel, a friendly chat bot! \n\n".format(self.name))
        self.ChatLog.insert(END,"Hazel: Could you spend some time with me?\n\n")
        self.ChatLog.config(state=DISABLED)
    
    def parseResponse(self, msg, flag):
        if flag == 0:
            self.name = msg
            self.flag += 1
            return "Oh, so your name is " + msg + "? That's awesome!"
        if (flag == 1):
            if msg in self.negative_responses:
                self.flag = 999
                return "Ok, bye!"
            else:
                self.flag += 1
                return "Thank you so much!"
        else:
            if not(self.Hazel.make_exit(msg)):
                return self.Hazel.match_reply(msg)
            else:
                self.root.destroy()
                return ''
            

    def send(self):
        msg = self.EntryBox.get("1.0",'end-1c').strip()
        self.EntryBox.delete("0.0",END)

        if msg != '':
            self.ChatLog.config(state=NORMAL)
            self.ChatLog.insert(END, "You: " + msg + '\n\n')
            self.ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
        res = self.parseResponse(msg, self.flag)
        self.ChatLog.insert(END, "Hazel: " + res + '\n\n')
        if self.flag == 2:
            msg = self.Hazel.chat()
            self.ChatLog.insert(END, "Hazel: " + msg + '\n\n')
            self.flag +=1
        self.ChatLog.config(state=DISABLED)
        self.ChatLog.yview(END)
        if self.flag == 1:
            self.Start()
        if self.flag == 999:
            self.event.wait(1)
            self.root.destroy()
            

    
    


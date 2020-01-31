# -*- coding: utf-8 -*-
import tkinter
from classes.disneyBot import disneyChatBot

def decoupeuse(string, size):
    split = string.split(' ')
    chariote = []
    while split:
        printable = ''
        while split and len(' '.join([printable,split[0]])) < size:
            if split:
                printable = ' '.join([printable,split.pop(0)])
            else:
                break
        chariote.append(printable)
    return chariote



class App():
    def __init__(self, bot):
        self.bot = bot
        self.root = tkinter.Tk()
        self.root.title("Disney Bot 3000")
        
        messages_frame = tkinter.Frame(self.root)
        self.my_msg = tkinter.StringVar()
        
        scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.

        self.list_msg = tkinter.Listbox(messages_frame, height=30, width=100, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.list_msg.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.list_msg.pack()
        
        messages_frame.pack()
        
        text_input = tkinter.Entry(self.root, textvariable=self.my_msg, width=50)
        text_input.bind("<Return>", self.questionne)
        text_input.bind("<Escape>", lambda f: self.root.destroy())
        text_input.pack()
        
        send_button = tkinter.Button(self.root, text="Send", command=self.questionne)
        send_button.pack()
        tkinter.mainloop()
        
    def questionne(self,event=None):
        msg = self.my_msg.get()
        self.my_msg.set("")  # Clears input field.
        if msg == '':
            return None
        if msg == "quit":
            self.root.destroy()
        else:
            self.list_msg.insert(tkinter.END, "Moi : "+msg)
            self.list_msg.itemconfig(self.list_msg.size()-1, {'bg':'red'})
            for line in decoupeuse(self.bot.repond(msg),110):
                self.list_msg.insert(tkinter.END, line)
                
    def on_closing(self,event=None):
        """This function is to be called when the window is closed."""
        self.my_msg.set("{quit}")
        self.send()
    

app = App(disneyChatBot())
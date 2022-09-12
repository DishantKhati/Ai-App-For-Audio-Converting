from gtts import gTTS
import os
from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Ai-saver")
def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    language = 'hi'
    myobj=gTTS(text=INPUT, lang=language)
    myobj.save("D:\\AiSaves\\welcome.mp3")
    os.system("D:\\AiSaves\\welcome.mp3")
l=Label(text = "Enter the Statement")
inputtxt = Text(root,height=20,width=50,bg="white")
Display=Button(root, height = 5,width = 15,text ="send" ,command = lambda:Take_input())
Display.place(x=190,y=355)
l.pack()
inputtxt.pack()
mainloop()

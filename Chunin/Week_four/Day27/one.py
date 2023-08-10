#Creating Windows and Labels with tkinter
from tkinter import *
import tkinter

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
#Label

my_label = Label(text="I am a Label", font=("Arial", 24, "italic"))
my_label.pack()

my_label["text"] = "New Text"


#Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry
input = Entry(width=10)
input.pack()
print(input.get())




window.mainloop()
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
root = Tk()
root.configure(background="#2D2B30")
root.minsize(200, 200)
root.geometry("300x300+500+500")


label = Label(root, 
                text = "Label_1",
                bg = "#2D2B30",
                fg = "white",
                font = ("Impact", 60))
label.pack()
#def test() :
#    msg=messagebox.showinfo( "Hello Python", "Hello World")
#B = Button(root, text ="Hello", command = test())
#B.place(x=50,y=50)

def show():
   name = askstring("Input", "Enter you name")
   print(name)
def pr() :
   print("test")
B = Button(root, text ="Click", command = pr)
B.place(x=50,y=50)
root.mainloop()
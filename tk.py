from tkinter import *
from tkinter import messagebox
import random

def no():
    messagebox.showinfo('', 'I knew it!!')
    quit()

def motionMouse(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = Tk()
root.geometry('600x600')
root.title('Survey')
root.resizable(width=False, height=False)
root['bg'] = "white"
label = Label(root, text='Are you gay?', font=('Arial', 10), bg='white')
label.pack()


btnYes = Button(root, text='No', font=('Arial', 30, 'bold'))
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)

btnNo = Button(root, text='Yes', font=('Arial', 30, 'bold'), command=no)
btnNo.place(x=350, y=100)

root.mainloop()

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Label Example')

# Frame as Widget container
frame1 = ttk.Frame(root)
frame1.grid()

# Image
pencil_image = PhotoImage(file='pencil.png')

# Label1
label1 = ttk.Label(
    frame1,
    text='Will schools be open this fail?',
    image=pencil_image,
    compound='top',
    padding=(20))
label1.grid(row=0,column=0)

#ウィンドウの表示開始
root.mainloop()
import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("640x480+500+500")

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='sunken', borderwidth=2)
# canvas.pack(side="left", fill=tkinter.BOTH, expand=True)
canvas.pack(side="top")

button1 = tkinter.Button(mainWindow, text="Button 1")
button2 = tkinter.Button(mainWindow, text="Button 2")
button3 = tkinter.Button(mainWindow, text="Button 3")

button1.pack(side='top', anchor='n')
button2.pack(side='top', anchor='s')
button3.pack(side='top', anchor='e')


mainWindow.mainloop()

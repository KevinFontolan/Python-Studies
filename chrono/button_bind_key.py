from tkinter import Button, Frame, Tk


class MyClass:
    def __init__(self, button_enter):
        frame = Frame(button_enter)
        frame.pack()

        self.button = Button(frame, text="Hello", command=self.func)
        self.button.pack(side='left')

        button_enter.bind('a', self.func)

    def func(self, _event=None):
        print("Hello, world")


mainWindow = Tk()
abc = MyClass(mainWindow)
mainWindow.mainloop()

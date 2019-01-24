# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

import tkinter

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry("640x480-8-200")
padding = 8
mainWindow['padx'], mainWindow['pady'] = padding, padding

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky="sw", columnspan=1)

keys = [[('1', 1), ('2', 1), ('3', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('/', 1)],
        [('0', 1), ('CE', 1), ('=', 1), ('*', 1)],
        ]

keypad = tkinter.Frame(mainWindow)
keypad.grid(row=1, column=0, sticky='nsew')
keypad['pady'] = 8

r = 0
for key in keys:
    col = 0
    for val in key:
        but = tkinter.Button(
            keypad, text=val[0])
        but.grid(row=r, column=col, sticky=tkinter.E +
                 tkinter.W, columnspan=val[1])
        col += 1
    r += 1

mainWindow.update()
mainWindow.maxsize(keypad.winfo_width() + 2*padding,
                   result.winfo_height() + keypad.winfo_height() + 2*padding)


tkinter.mainloop()

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import math


def parabola(page, size):
    x = 0
    y = 0
    while y <= 400:
        y = x ** 2 / 200
        plot(page, x, y)
        plot(page, -x, y)
        x += 1

# Modify the circle function so that it allows the colour of the circle to be specified
# and defaults to red if a colour is not given. You may want to review the previous lectures
# about named parameters and default values.


def circle(page, radius, g, h, colour="red"):
    page.create_oval(g + radius, h + radius, g - radius,
                     h - radius, outline=colour, width=1)

#     for x in range(g * 10, (g + radius) * 10):
#         x /= 10
#         print(x)
#         y = h + math.sqrt(radius ** 2 - ((x-g) ** 2))
#         plot(page, x, y)
#         plot(page, x, 2 * h - y)
#         plot(page, 2 * g - x, y)
#         plot(page, 2 * g - x, 2 * h - y)


def drawAxes(draw_canvas):
    draw_canvas.update()
    x_origin = draw_canvas.winfo_width() / 2
    y_origin = draw_canvas.winfo_height() / 2
    draw_canvas.configure(
        scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    draw_canvas.create_line(-x_origin, 0, x_origin, 0,
                            fill="black", width=1.1, arrow="last", arrowshape="8 10 4")
    draw_canvas.create_line(0, y_origin, 0, -y_origin,
                            fill="blue", arrow="last", arrowshape="8 10 4")
    print(locals())


def plot(plot_canvas, x, y):
    plot_canvas.create_line(x, -y, x + 1, -y + 1, fill='red')


mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry("1200x800")

c_width = 1200
c_height = 800
canvas = tkinter.Canvas(mainWindow, width=c_width, height=c_height)
canvas.grid(row=0, column=0)

drawAxes(canvas)

parabola(canvas, 100)
parabola(canvas, 200)
for i in range(0, 200):
    if i % 2 == 0:
        circle(canvas, 3*i, i, i, "blue")
    elif i % 3 == 0:
        circle(canvas, 3*i, i, i, "green")
    else:
        circle(canvas, 3*i, i, i)

mainWindow.minsize(1200, 800)
mainWindow.maxsize(1200, 800)

tkinter.mainloop()

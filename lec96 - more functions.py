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


def circle(page, radius, g, h):
    for x in range(g * 10, (g + radius) * 10):
        x /= 10
        print(x)
        y = h + math.sqrt(radius ** 2 - ((x-g) ** 2))
        plot(page, x, y)
        plot(page, x, 2 * h - y)
        plot(page, 2 * g - x, y)
        plot(page, 2 * g - x, 2 * h - y)


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
for i in range(10):
    circle(canvas, 5*i, i, i)

mainWindow.minsize(1200, 800)
mainWindow.maxsize(1200, 800)

tkinter.mainloop()

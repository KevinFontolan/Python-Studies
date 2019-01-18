# A basic game where Schala beats Devil Soros.

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import random

import time


def load_schala(game_imgs):
    schala = 'schala'
    extension = 'png'

    # For each Schala action, retrieve images for the character stances
    for stance in range(1, 3):
        name = 'chrono/{}{}.{}'.format(str(schala),
                                       stance, extension)
        image = tkinter.PhotoImage(file=name)
        game_imgs.append((stance, image))


def load_powerschala(game_imgs):
    powerschala = 'schalap'
    extension = 'png'

    # For each Schala action, retrieve images for the character stances
    for stance in range(1, 3):
        name = 'chrono/{}{}.{}'.format(str(powerschala),
                                       stance, extension)
        image = tkinter.PhotoImage(file=name)
        game_imgs.append((stance, image))


def load_soros(game_imgs):
    soros = 'soros'
    extension = 'png'

    for sorosface in range(1, 4):
        name = 'chrono/{}{}.{}'.format(soros, str(sorosface), extension)
        image = tkinter.PhotoImage(file=name)
        game_imgs.append((sorosface, image))


def load_forest(game_imgs):
    forest = ['forestbot', 'foresttop']
    extension = 'png'

    for crop in forest:
        name = 'chrono/{}.{}'.format(str(crop), extension)
        image = tkinter.PhotoImage(file=name)
        game_imgs.append((crop, image))


def load_power(game_imgs):
    pwr = 'power'
    extension = 'png'

    for i in range(1, 7):
        name = 'chrono/{}{}.{}'.format(pwr, i, extension)
        image = tkinter.PhotoImage(file=name)
        game_imgs.append((pwr, image))


def _spawn_forest():
    tkinter.Label(top_frame, image=forest[0][1], borderwidth=0).grid(
        row=0, column=0)
    next_stance = schala.pop(0)
    schala.append(next_stance)
    tkinter.Label(player_char_frame, image=next_stance[1], borderwidth=0).grid(
        row=0, column=0)
    tkinter.Label(bot_frame, image=forest[1][1], borderwidth=0).grid(
        row=0, column=0)


def _schala_move():
    next_stance = schala.pop(0)
    # Add it to the back of the deck
    schala.append(next_stance)
    # Add the image to a Label and display the Label
    tkinter.Label(player_char_frame, image=next_stance[1], borderwidth=0).grid(
        row=0, column=0)


def _schala_power():
    next_stance = powerschala.pop(0)
    # Add it to the back of the deck
    powerschala.append(next_stance)
    # Add the image to a Label and display the Label
    tkinter.Label(player_char_frame, image=next_stance[1], borderwidth=0).grid(
        row=0, column=0)
    next_power = power.pop(0)
    power.append(next_power)
    tkinter.Label(player_char_frame, image=next_power[1], borderwidth=0).grid(
        row=0, column=1)


power = []
schala = []
powerschala = []
soros = []
forest = []

mainWindow = tkinter.Tk()

mainWindow.title("Schala vs Devil Soros")
mainWindow.geometry("640x480")
mainWindow.configure(background="black")
mainWindow.maxsize(width=640, height=700)

top_frame = tkinter.Frame(
    mainWindow, relief="sunken", borderwidth=0, background="black")
top_frame.grid(row=0, column=0, sticky="ew",
               columnspan=3, rowspan=1)

char_frame = tkinter.Frame(
    mainWindow, relief="sunken", borderwidth=0, background="black")
char_frame.grid(row=1, column=0, sticky="ew",
                columnspan=3, rowspan=2)
char_frame['padx'] = 20

bot_frame = tkinter.Frame(
    mainWindow, relief="sunken", borderwidth=0, background="black")
bot_frame.grid(row=3, column=0, sticky="ew",
               columnspan=3, rowspan=1)

player_char_frame = tkinter.Frame(char_frame, background="black")
player_char_frame.grid(
    row=0, column=0, sticky="ew", columnspan=3, rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=2, column=1, columnspan=3, rowspan=1)

move_button = tkinter.Button(
    button_frame, text="Move forward", command=_schala_move)
move_button.grid(row=0, column=0, sticky="es")

power_button = tkinter.Button(
    button_frame, text="Zeal Light", command=_schala_power)
power_button.grid(row=0, column=1, sticky="se")

load_power(power)
load_powerschala(powerschala)
load_schala(schala)
load_soros(soros)
load_forest(forest)

_spawn_forest()

print(schala)
print(soros)
print(forest)


mainWindow.mainloop()

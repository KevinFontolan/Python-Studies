# A basic game where Schala beats Devil Soros.

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import random

import time


def load_schala(game_imgs):
    schala = ['schala', 'schalap']
    extension = 'png'

    # For each Schala action, retrieve images for the character stances
    for action in schala:
        for stance in range(1, 3):
            name = 'chrono/{}{}.{}'.format(str(action),
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


def _spawn_schala(frame):
    next_stance = schala.pop(0)
    schala.append(next_stance)
    tkinter.Label(frame, image=next_stance[1], relief='raised').pack(
        side="left")


schala = []
soros = []
forest = []

mainWindow = tkinter.Tk()

mainWindow.title("Schala vs Devil Soros")
mainWindow.geometry("640x480")
mainWindow.configure(background="black")

char_frame = tkinter.Frame(
    mainWindow, relief="sunken", borderwidth=0, background="black")
char_frame.grid(row=0, column=0, sticky="ew",
                columnspan=3, rowspan=2)

player_char_frame = tkinter.Frame(char_frame, background="black")
player_char_frame.grid(
    row=0, column=0, sticky="ew", columnspan=3, rowspan=2)

load_schala(schala)
load_soros(soros)
load_forest(forest)

for i in range(1, 10):
    _spawn_schala(player_char_frame)


print(schala)
print(soros)
print(forest)

mainWindow.mainloop()


#
# def _schala_move(frame):
#     while True:
#         next_stance = deck.pop(0)
#     # Add it to the back of the deck
#     deck.append(next_card)
#     # Add the image to a Label and display the Label
#     tkinter.Label(frame, image=next_card[1], relief='raised').pack(
#         side="left")
#     # Now, return the card's face value
#     return next_card
#
# def _deal_card(frame):
#     # Pop the next card off the top of the deck
#     next_card = deck.pop(0)
#     # Add it to the back of the deck
#     deck.append(next_card)
#     # Add the image to a Label and display the Label
#     tkinter.Label(frame, image=next_card[1], relief='raised').pack(
#         side="left")
#     # Now, return the card's face value
#     return next_card
#
#
# def score_hand(hand):
#     # Calculate the total score of all cards in the list
#     # Only one ace can have the value of 11, and it will be reduced to 1 if the hand would bust
#     score = 0
#     ace = False
#     for next_card in hand:
#         card_value = next_card[0]
#         if card_value == 1 and not ace:
#             ace = True
#             card_value = 11
#         score += card_value
#         # If we would bust, check if there is an ace and subtract 10 if so
#         if score > 21 and ace:
#             ace = False
#             score -= 10
#     return score
#
#
# def deal_dealer():
#     dealer_score = score_hand(dealer_hand)
#     # Dealer draws until he reaches a score of 17
#     while 0 < dealer_score < 17:
#         dealer_hand.append(_deal_card(dealer_card_frame))
#         dealer_score = score_hand(dealer_hand)
#         dealer_score_label.set(dealer_score)
#
#     player_score = score_hand(player_hand)
#     # Win/Lose conditions
#     if player_score > 21:
#         result_text.set("Dealer wins.")
#     elif dealer_score > 21 or dealer_score < player_score:
#         result_text.set("Player wins.")
#     elif dealer_score > player_score:
#         result_text.set("Dealer wins.")
#     else:
#         result_text.set("Draw!")
#
#
# def deal_player():
#     player_hand.append(_deal_card(player_card_frame))
#     player_score = score_hand(player_hand)
#     # Lose condition
#     player_score_label.set(player_score)
#     if player_score > 21:
#         result_text.set("Dealer wins.")
#
#
# def new_game():
#     global dealer_card_frame
#     global player_card_frame
#     global dealer_hand
#     global player_hand
#     # Embedded frame to hold the dealer card images
#     dealer_card_frame.destroy()
#     dealer_card_frame = tkinter.Frame(card_frame, background="green")
#     dealer_card_frame.grid(
#         row=0, column=1, sticky="ew", columnspan=3, rowspan=2)
#     # Embedded frame to hold the player card images
#     player_card_frame.destroy()
#     player_card_frame = tkinter.Frame(card_frame, background="green")
#     player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)
#
#     # Resetting the victory text
#     result_text.set("Game's on!")
#
#     # Create the list to store the dealer's and the player's hands
#     dealer_hand = []
#     player_hand = []
#     initial_deal()
#
#
# def initial_deal():  # Initiate the game
#     deal_player()
#     dealer_hand.append(_deal_card(dealer_card_frame))
#     dealer_score_label.set(score_hand(dealer_hand))
#     deal_player()
#
#
# def shuffle():
#     random.shuffle(deck)
#     result_text.set("Deck shuffled.")
#
#
# def play():
#     initial_deal()
#     mainWindow.mainloop()
#
#
# # Set up the screen and frames for the dealer and the player
# mainWindow = tkinter.Tk()
#
# mainWindow.title("Blackjack")
# mainWindow.geometry("640x480")
# mainWindow.configure(background="green")
#
# result_text = tkinter.StringVar()
# result = tkinter.Label(mainWindow, textvariable=result_text)
# result.grid(row=0, column=0, columnspan=3)
#
# card_frame = tkinter.Frame(
#     mainWindow, relief="sunken", borderwidth=1, background="green")
# card_frame.grid(row=1, column=0, sticky="ew",
#                 columnspan=3, rowspan=2)
#
# # Embedded frames to hold the card images
# dealer_card_frame = tkinter.Frame(card_frame, background="green")
# dealer_card_frame.grid(
#     row=0, column=1, sticky="ew", columnspan=3, rowspan=2)
#
# player_card_frame = tkinter.Frame(card_frame, background="green")
# player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)
#
# # Score labels
# dealer_score_label = tkinter.IntVar()
#
# tkinter.Label(card_frame, text="Dealer", background="green",
#               fg="white").grid(row=0, column=0)
# tkinter.Label(card_frame, textvariable=dealer_score_label,
#               background="green", fg="white").grid(row=1, column=0)
#
# player_score_label = tkinter.IntVar()
#
# tkinter.Label(card_frame, text="Player", background="green",
#               fg="white").grid(row=2, column=0)
# tkinter.Label(card_frame, textvariable=player_score_label,
#               background="green", fg="white").grid(row=3, column=0)
#
# # Buttons
# button_frame = tkinter.Frame(mainWindow)
# button_frame.grid(row=3, column=0, columnspan=3, sticky="w")
#
# dealer_button = tkinter.Button(
#     button_frame, text="Dealer", command=deal_dealer)
# dealer_button.grid(row=0, column=0)
#
# player_button = tkinter.Button(
#     button_frame, text="Player", command=deal_player)
# player_button.grid(row=0, column=1)
#
# restart_button = tkinter.Button(
#     button_frame, text="New Game", command=new_game)
# restart_button.grid(row=0, column=2)
#
# shuffle_button = tkinter.Button(
#     button_frame, text="Shuffle", command=shuffle)
# shuffle_button.grid(row=0, column=3)
#
# # Load cards
# cards = []
# load_images(cards)
# print(cards)
#
# # Create a new deck of cards and shuffle them
# shuffle()
#
# # Create the list to store dealer's and player's hands
# dealer_hand = []
# player_hand = []
#
# # Importing
# if __name__ == "__main__":
#     play()

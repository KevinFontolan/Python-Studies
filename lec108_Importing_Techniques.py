# from lec101_blackjack import * # This one does not import entities started by "_"
import lec101_blackjack

print(__name__)

# Sorting globals so we can print them
g = sorted(globals())

# Printing globals
for x in g:
    print(x)

# Testing function started by "_"
lec101_blackjack._deal_card(lec101_blackjack.dealer_card_frame)
lec101_blackjack.play()

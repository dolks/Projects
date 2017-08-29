import random

"""
Class defining the cards used in gameplay. Each card 
has both a face and a value, represented by integers.
"""


class Card:

    def __init__(self, face, value):
        self.face = face
        self.value = value

    def __str__(self):
        return "(" + str(self.face) + "," + str(self.value) + ")"

"""
Class defining the player. Each player object has a name,
total money (int), and a hand of cards used in gameplay 
(represented by a list of Card objects).
"""


class Player:

    def __init__(self, name, money, hand):
        self.name = name
        self.money = money
        self.hand = hand

    def hit(self, card):
        self.hand.append(card)

    def make_bet(self):
        while True:
            try:
                amt = float(raw_input('Enter bet amount: '))
            except:
                print 'Input is not a valid number.'
            else:
                if amt > self.money:
                    print 'You don\'t enough money for that bet'
                else:
                    self.money -= amt
                    print 'You bet ' + str(amt)
                    print 'You have ' + str(self.money) + ' remaining.'
                    break


def make_deck():
    i = 0
    value = 1
    face = 0
    deck = []
    while i < 52:
        if value == 14:
            value = 1
            face += 1
        crd = Card(face, value)
        deck.append(crd)
        value += 1
        i += 1

    random.shuffle(deck)
    return deck





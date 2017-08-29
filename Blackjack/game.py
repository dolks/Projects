class Card:

    def __init__(self, value, face):
        self.value = value
        self.face = face


class Player:

    def __init__(self, name, money, hand):
        self.name = name
        self.money = money
        self.hand = hand

    def hit(self, card):
        self.hand.append(card)
        # INSERT LOGIC FOR TOTAL VALUE OF HAND HERE?

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







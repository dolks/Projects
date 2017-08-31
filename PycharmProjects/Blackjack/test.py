import random
lst = [1,2,3]
lst.append(4)

print lst


class thingy:

    def __init__(self, name):
        self.name = name


x = thingy('hey')


def make_bet(money):
    while True:
        try:
            amt = float(raw_input('Enter bet amount: '))
        except:
            print 'Input is not a valid number.'
        else:
            if amt > money:
                print 'You don\'t enough money for that bet'
            else:
                money -= amt
                print 'You bet ' + str(amt)
                print 'You have ' + str(money) + ' remaining.'
                break


make_bet(40)


deck = []
#deck = make_deck()
random.shuffle(deck)

for card in deck:
    print card

lst = [1,2,3]

x = lst.pop(0)

print x

print lst[0]



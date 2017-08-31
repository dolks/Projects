import random

"""
Class defining the cards used in gameplay. Each card 
has both a face and a value, represented by integers.
"""
class Card:

    card_faces = {0: 'Spades', 1: 'Clubs', 2: 'Hearts', 3: 'Diamonds'}
    card_values = {1: 'Ace', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                   8: '8', 9: '9', 10: '10', 11: 'Jack', 12: 'Queen', 13: 'King'}

    def __init__(self, face, value):
        self.face = face
        self.value = value

    def __str__(self):
        return Card.card_values[self.value] + " of " + Card.card_faces[self.face]



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
        if self.money == 0:
            print 'You have no money left to bet with.'
            return 0
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
                    return amt

"""
Creates and randomizes deck of cards. The 'deck' is really
a list of Card objects.
"""
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


name = raw_input('Enter your name: ')
while True:
    try:
        money = float(raw_input('How much money do you have to bet with?'))
    except TypeError:
        print 'Amount must be a number.'
    else:
        break

p1 = Player(name, money, [])

dealer = Player('dealer', 0, [])

dck = make_deck()
keep_playing = True


while keep_playing:

    p1.hit(dck.pop(0))
    p1.hit(dck.pop(0))

    print 'You were dealt the ' + str(p1.hand[0]) + ' and the ' + str(p1.hand[1])

    # Checking for face cards.
    if p1.hand[0].value > 10:
        p1.hand[0].value = 10

    if p1.hand[1].value > 10:
        p1.hand[1].value = 10

    # Code to check if first card is an ace.
    if p1.hand[0].value == 1:
        while True:
            try:
                answer = int(raw_input('Would you like your ' + str(p1.hand[0]) + ' to be a 1 or 11?'))
            except TypeError:
                print 'Answer must be an integer of 1 or 11.'
            else:
                if answer == 1:
                    break
                elif answer == 11:
                    p1.hand[0].value = 11
                    break
                else:
                    print 'Answer must be 1 or 11.'

    # Code to check if second card value is an ace.
    if p1.hand[1].value == 1:
        while True:
            try:
                answer = int(raw_input('Would you like your ' + str(p1.hand[1]) + ' to be a 1 or 11?'))
            except:
                print 'Response must be an integer of 1 or 11.'
            else:
                if answer == 1:
                    break
                elif answer == 11:
                    p1.hand[1].value = 11
                    break
                else:
                    print 'Response must be 1 or 11.'



    bet = p1.make_bet()

    player_lost = False
    player_total = p1.hand[0].value + p1.hand[1].value
    while True:

        response = raw_input('Would you like to hit or stand? ')
        if response.lower() == 'hit' or response.lower() == 'h':

            p1.hit(dck.pop(0))
            print 'You were dealt the ' + str(p1.hand[len(p1.hand)-1])

            if p1.hand[len(p1.hand)-1].value > 10:
                p1.hand[len(p1.hand)-1] = 10
            # Checks if card received on hit is an ace
            if p1.hand[len(p1.hand)-1].value == 1:
                while True:
                    try:
                        answer = int(raw_input('Would you like your ' + str(p1.hand[len(p1.hand)-1]) + ' to be a 1 or 11?'))
                    except:
                        print 'Answer must be an integer of 1 or 11.'
                    else:
                        if answer == 1:
                            break
                        elif answer == 11:
                            p1.hand[len(p1.hand)-1].value = 11
                            break
                        else:
                            print 'Answer must be 1 or 11.'

            player_total += p1.hand[len(p1.hand)-1].value

            # For loop and conditional to ensure player's total isn't greater than 21.
            if player_total > 21:
                print p1.name + ' lost this round!'
                player_lost = True
                dealer.money += bet
                break

        elif response.lower() == 'stand' or response.lower() == 's':
            break

        else:
            print 'Invalid response.'
            print 'Valid responses include: \'stand\' (or \'s\') and \'hit\' (or \'h\').'

    if not player_lost:
        # Dealer's turn
        dealer.hit(dck.pop(0))
        dealer.hit(dck.pop(0))

        print 'The dealer was given the ' + str(dealer.hand[0]) + ' and the ' + str(dealer.hand[1])

        # Checks for face cards.
        if dealer.hand[0].value > 10:
            dealer.hand[0].value = 10
        if dealer.hand[1].value > 10:
            dealer.hand[1].value = 10

        # Both cards are aces.
        if dealer.hand[0].value == 1 and dealer.hand[1].value == 1:
            dealer.hand[0].value = 11
        # First card is ace.
        elif dealer.hand[0].value == 1:
            dealer.hand[0].value = 11
        # Second card value is an ace.
        elif dealer.hand[1].value == 1:
            dealer.hand[1].value = 11
        # Neither of the cards are aces.
        else:
            pass

        dealer_total = dealer.hand[0].value + dealer.hand[1].value
        print str(dealer_total)
        while dealer_total < 17:
            # Loop to keep hitting for dealer until they reach 17 or more
            dealer.hit(dck.pop(0))
            print 'The dealer was given the ' + str(dealer.hand[len(dealer.hand) - 1])

            # Checks for face cards.
            if dealer.hand[len(dealer.hand)-1].value > 10:
                dealer.hand[len(dealer.hand)-1].value = 10

            # Conditional to check if card given was an ace.
            if dealer.hand[len(dealer.hand) - 1].value == 1:
                if dealer_total + 11 < 21:
                    dealer.hand[len(dealer.hand) - 1].value = 11
                else:
                    dealer.hand[len(dealer.hand) - 1].value = 1
            dealer_total += dealer.hand[len(dealer.hand)-1].value

        # Final conditionals to see who won the round.
        if dealer_total > 21:
            print p1.name + ' wins! You earned ' + str(bet)
            p1.money += bet * 2
        elif dealer_total >= player_total:
            print 'The dealer wins!'
        else:
            print p1.name + ' wins! You earned ' + str(bet)
            p1.money += bet*2

    print 'Your remaining money is: ' + str(p1.money)
    while True:
        try:
            response = str(raw_input('Would you like to keep playing? '))
        except TypeError:
            print 'Invalid response. Response must be \'yes\' or \'no\'.'
        else:
            if response.lower() == 'yes' or response.lower() == 'y' \
                or response.lower() == 'yea' or response.lower() == 'ye':

                # Resets players hands and deck.
                del p1.hand[:]
                del dealer.hand[:]
                del dck[:]
                dck = make_deck()
                break
            elif response.lower() == 'n' or response.lower() == 'no':
                keep_playing = False
                break

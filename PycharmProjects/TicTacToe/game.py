def printboard(brd, cmd):
    # Clears board of spaces. Resets dict brd.
    if cmd.lower() == 'clear':
            print '**************************' #len ==26
            print '*       |        |       *'
            print '*       |        |       *'
            print '*       |        |       *'
            print '*------------------------*'
            print '*       |        |       *'
            print '*       |        |       *'
            print '*       |        |       *'
            print '*------------------------*'
            print '*       |        |       *'
            print '*       |        |       *'
            print '*       |        |       *'
            print '**************************'

            brd = {'tl': ' ', 'tm': ' ', 'tr': ' ', 'ml': ' ',
             'mm': ' ', 'mr': ' ', 'bl': ' ', 'bm': ' ',
             'br': ' '}
    elif cmd.lower() == 'play' or cmd.lower() == 'p' \
            or cmd.lower() == 'ply':
        print '**************************'  # len ==26
        print '*       |        |       *'
        print '*   ',brd['tl'],' |   ',brd['tm'],'  |   ',brd['tr'],' *'
        print '*       |        |       *'
        print '*------------------------*'
        print '*       |        |       *'
        print '*   ', brd['ml'], ' |   ', brd['mm'], '  |   ', brd['mr'], ' *'
        print '*       |        |       *'
        print '*------------------------*'
        print '*       |        |       *'
        print '*   ', brd['bl'], ' |   ', brd['bm'], '  |   ', brd['br'], ' *'
        print '*       |        |       *'
        print '**************************'
    else:
        print 'Invalid cmd in printBoard(brd, cmd).'

def insertXO(brd, trn):

    print 'Type what space you want to put your X or O.'
    maketurn = True

    # Loop to check for invalid input.
    while maketurn:
        resp = raw_input('(For example, type \'top left\' or \'tl\' or type \'clear\' to reset): ')

        if resp.lower() == 'clear' or resp.lower() == 'clr' \
            or resp.lower() == 'cl' or resp.lower() == 'c':
            printboard(brd, 'clear')
            maketurn = False

        elif resp.lower() == 'tl' or resp.lower() == 'top left' \
            or resp.lower() == 'tm' or resp.lower() == 'top middle' \
            or resp.lower() == 'tr' or resp.lower() == 'top right' \
            or resp.lower() == 'bl' or resp.lower() == 'bottom left' \
            or resp.lower() == 'bm' or resp.lower() == 'bottom middle' \
            or resp.lower() == 'br' or resp.lower() == 'bottom right' \
            or resp.lower() == 'mr' or resp.lower() == 'middle right' \
            or resp.lower() == 'mm' or resp.lower() == 'middle middle' \
                or resp.lower() == 'ml' or resp.lower() == 'middle left':

            if resp.lower() == 'top left':
                resp = 'tl'
            elif resp.lower() == 'top middle':
                resp = 'tm'
            elif resp.lower() == 'top right':
                resp = 'tr'
            elif resp.lower() == 'bottom left':
                resp = 'bl'
            elif resp.lower() == 'bottom middle':
                resp = 'bm'
            elif resp.lower() == 'bottom right':
                resp = 'br'
            elif resp.lower() == 'middle middle':
                resp = 'mm'
            elif resp.lower() == 'middle left':
                resp = 'ml'
            elif resp.lower() == 'middle right':
                resp = 'mr'
            # Conditional to ensure space isn't already taken.
            if brd[resp] == 'X' or brd[resp] == 'O':
                    print resp + ' is already taken.'
            else:
                maketurn = False
        else:
            print 'Invalid response in insertXO(brd, resp, trn).'
            print 'Type what space you want to put your X or O.'
    # Player one's turn.
    if resp.lower() == 'clear' or resp.lower() == 'clr' \
            or resp.lower() == 'cl' or resp.lower() == 'c':
        return

    if not trn:

        if resp.lower() == 'tl' or resp.lower() == 'top left':
            brd['tl'] = 'X'
            printboard(brd, 'play')
        elif resp.lower() == 'tm' or resp.lower() == 'top middle':
            brd['tm'] = 'X'
            printboard(brd, 'play')
        elif resp.lower() == 'tr' or resp.lower() == 'top right':
            brd['tr'] = 'X'
            printboard(brd, 'play')
        elif resp.lower() == 'ml' or resp.lower() == 'middle left':
            brd['ml'] = 'X'
            printboard(brd, 'play')
        elif resp.lower() == 'mm' or resp.lower() == 'middle middle':
            brd['mm'] = 'X'
            printboard(brd, 'play')
        elif resp.lower() == 'mr' or resp.lower() == 'middle right':
            brd['mr'] = 'X'
            printboard(brd, 'play')
        elif resp.lower() == 'bl' or resp.lower() == 'bottom left':
            brd['bl'] = 'X'
            printboard(brd, 'play')
        elif resp.lower() == 'bm' or resp.lower() == 'bottom middle':
            brd['bm'] = 'X'
            printboard(brd, 'play')
        elif resp.lower() == 'br' or resp.lower() == 'bottom right':
            brd['br'] = 'X'
            printboard(brd, 'play')
        else:
            print 'Invalid response in insertXO(brd, resp, trn).'
    # Player two's turn.
    else:
        if resp.lower() == 'tl' or resp.lower() == 'top left':
            brd['tl'] = 'O'
            printboard(brd, 'play')
        elif resp.lower() == 'tm' or resp.lower() == 'top middle':
            brd['tm'] = 'O'
            printboard(brd, 'play')
        elif resp.lower() == 'tr' or resp.lower() == 'top right':
            brd['tr'] = 'O'
            printboard(brd, 'play')
        elif resp.lower() == 'ml' or resp.lower() == 'middle left':
            brd['ml'] = 'O'
            printboard(brd, 'play')
        elif resp.lower() == 'mm' or resp.lower() == 'middle middle':
            brd['mm'] = 'O'
            printboard(brd, 'play')
        elif resp.lower() == 'mr' or resp.lower() == 'middle right':
            brd['mr'] = 'O'
            printboard(brd, 'play')
        elif resp.lower() == 'bl' or resp.lower() == 'bottom left':
            brd['bl'] = 'O'
            printboard(brd, 'play')
        elif resp.lower() == 'bm' or resp.lower() == 'bottom middle':
            brd['bm'] = 'O'
            printboard(brd, 'play')
        elif resp.lower() == 'br' or resp.lower() == 'bottom right':
            brd['br'] = 'O'
            printboard(brd, 'play')
        else:
            print 'Invalid response in insertXO(brd, resp, trn).'

def checkboard(brd):

    if brd['tl'] == 'X' and brd['tm'] == 'X' and brd['tr'] == 'X'\
            or brd['tl'] == 'X' and brd['mm'] == 'X' and brd['br'] == 'X' \
            or brd['tl'] == 'X' and brd['ml'] == 'X' and brd['bl'] == 'X' \
            or brd['ml'] == 'X' and brd['mm'] == 'X' and brd['mr'] == 'X' \
            or brd['tm'] == 'X' and brd['mm'] == 'X' and brd['bm'] == 'X' \
            or brd['tr'] == 'X' and brd['mm'] == 'X' and brd['bl'] == 'X' \
            or brd['tr'] == 'X' and brd['mr'] == 'X' and brd['br'] == 'X' \
            or brd['br'] == 'X' and brd['bm'] == 'X' and brd['br'] == 'X':
                return 'p1'

    elif brd['tl'] == 'O' and brd['tm'] == 'O' and brd['tr'] == 'O'\
            or brd['tl'] == 'O' and brd['mm'] == 'O' and brd['br'] == 'O' \
            or brd['tl'] == 'O' and brd['ml'] == 'O' and brd['bl'] == 'O' \
            or brd['ml'] == 'O' and brd['mm'] == 'O' and brd['mr'] == 'O' \
            or brd['tm'] == 'O' and brd['mm'] == 'O' and brd['bm'] == 'O' \
            or brd['tr'] == 'O' and brd['mm'] == 'O' and brd['bl'] == 'O' \
            or brd['tr'] == 'O' and brd['mr'] == 'O' and brd['br'] == 'O' \
            or brd['br'] == 'O' and brd['bm'] == 'O' and brd['br'] == 'O':
                return 'p2'

    else:
        return None

#def clearBoard(brd)?
#set all board values to false then printBoard?

player1 = raw_input('Enter Player One name: ')
print player1,' will be X\'s'
player2 = raw_input('Enter Player Two name: ')
print player2,'will be O\'s'

board = {'tl': ' ', 'tm': ' ', 'tr': ' ', 'ml': ' ',
             'mm': ' ', 'mr': ' ', 'bl': ' ', 'bm': ' ',
             'br': ' '}

#boolean for while loop to continue playing
keep_playing = True

#boolean for switching turns
turn = True
response = 'clear'

printboard(board, response)
while keep_playing:
    if turn:
        print 'It is ' + player1 + '\'s turn.'
        turn = False
    else:
        print 'It is ' + player2 + '\'s turn.'
        turn = True

    insertXO(board, turn)
    win = checkboard(board)

    if win is not None:
        if win == 'p1':
            print player1 + ' WINS!'
        else:
            print player2 + ' WINS!'
        response = raw_input('Would you like to play again? (Y/N)')
        while response.lower() != 'yes' and response.lower() != 'no' \
                and response.lower() != 'y' and response.lower() != 'n':
            response = raw_input('Invalid input. Type \'yes\' or \'no\': ')
        if response.lower() == 'y' or response.lower() == 'yes':
            printboard(board, 'clear')
        else:
            keep_playing = False
def printboard(brd, cmd):

    # Clears board of spaces. Resets dict brd.
    if cmd.lower() == 'clear' or cmd.lower() == 'clr' \
        or cmd.lower() == 'cl' or cmd.lower() == 'c':
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

"""
print len('**************************')
x = 'hello'
x = False

print x
x = 'hello'

print x

"""
board = {'tl': ' ', 'tm': ' ', 'tr': ' ', 'ml': ' ',
             'mm': ' ', 'mr': ' ', 'bl': ' ', 'bm': ' ',
             'br': ' '}
printboard(board, 'play')
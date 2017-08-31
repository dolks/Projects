try:
    for i in ['a', 'b', 'c']:
        i**2

except TypeError:
    print 'oh noes error'

try:
    x = 5
    y = 0

    z = x/y

except:
    print 'error stuff idk'

finally:
    print 'finally i print some shit'\


def ask():
    while True:
        try:
            x = int(raw_input('Enter an int: '))

        except:
            print 'oh no thats not an int you fuck'

        else:
            print x**2
            break


ask()

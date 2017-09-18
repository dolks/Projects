import math

"""
Function that returns pi up to the nth decimal place.
Note that it can only show up to 11 decimal places after
the decimal point.
"""

def pitonth(n):
    while True:
        try:
            num = int(n)
        except TypeError:
            print 'Number entered must be an integer.'
        else:
            result = ("%." + str(num) + "f") % math.pi
            return float(result)
def gensquares(n):
    for num in range(1,n):
        yield num**2

for num in gensquares(10):
    print num

import random

def randnum(low, high, n):
    count = 0
    while count<n:
        yield random.randrange(low, high)
        count+=1

for num in randnum(30, 50, 4):
    print num

s = 'hello'

s_iter = iter(s)
print s_iter.next()
print s_iter.next()
print s_iter.next()



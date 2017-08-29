print 'stuffses'

x = 3

if x + 3 == 6:
    print x,'+ 3 = 6'
else:
    print x,' + 3 != 6'

lst = [5,2,1,4]
print lst

lst.sort()
print lst

"""for num in lst:
    print num
"""
dct = {'k1':10, 'k2':20, 'k3':30}

for k,v in dct.iteritems():
    print k,v

print dct['k1']
def word_lengths(phrase):
    return map(len, phrase.split())

print word_lengths('How long are the words in this phrase')

def digits_to_num(digits):
    return reduce(lambda x,y: x*10 + y, digits)

print digits_to_num([1,2,3,4,5])

def filter_list(lst, letter):
    return filter(lambda x: x[0]==letter, lst)

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
print filter_list(l,'h')

def concatenate(L1, L2, connector):
    return [tuple[0] + connector + tuple[1] for tuple in zip(L1, L2)]

print concatenate(['A', 'B'], ['a', 'b'], '-')

def d_list(lst):
    dct = {}
    for count, thing in enumerate(lst):
        dct[thing] = count

    return dct

print d_list(['hey','wassup', 'ees me'])

def count_match_index(lst):
    amt = 0
    for count, num in enumerate(lst):
        if count == num:
            amt+=1

    return amt

print count_match_index([0,2,2,1,5,5,6,10])

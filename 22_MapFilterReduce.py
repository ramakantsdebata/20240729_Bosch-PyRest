lst = ["ramakant", "manish", "abhijeet", "vinayak", "shankar", "rakesh"]

## Map - Capitalise all name ###########################

resMap = list(map(str.capitalize, lst))
print(resMap)

## Filter - Names having 'r' ##########################

def HasR(word):
    if 'r' in word:
        return True
    else:
        return False
    
# resFil = list(filter(HasR, lst))
resFil = list(filter(lambda word: True if 'r' in word else False, lst))
print(resFil)

## Reduce ###########################################

from functools import reduce

def Concat( a, b):
    return a + " " + b

resRed = reduce(Concat, lst)
print(resRed)
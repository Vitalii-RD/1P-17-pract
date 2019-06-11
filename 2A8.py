import itertools, datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
from random import randrange

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spade', 'club', 'heart', 'diamond']

deck = list(itertools.product(vals, suits))
print("STANDARD DECK:")
for i in deck:
    print("{} of {}".format(i[0],i[1]))

def sattoloCycle(items):
    i = len(items)
    while i > 1:
        i = i - 1
        j = randrange(i)
        items[j], items[i] = items[i], items[j]
    return
sattoloCycle(deck)
print("NEW DECK:")
for i in deck:
    print("{} of {}".format(i[0],i[1]))

printTimeStamp("Коробов Даніїл, Дудник Віталій")

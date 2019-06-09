import datetime
from random import randint

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

article = ["the", "a", "one", "some", "any"]
noun = ["boy", "girl", "dog", "town", "car"]
verb = ["drove", "jumped", "ran", "walked", "skipped"]
preposition = ["to", "from", "over", "under", "on"]
listok = [article, noun, verb, preposition, article, noun]
for i in range(10):
    sentence = []
    for j in listok:
        sentence.append(j[randint(0,len(j)-1)])
    sentence[0] = sentence[0].capitalize()
    print(str(i+1)+":"," ".join(sentence))
printTimeStamp("Віталій Дудник")
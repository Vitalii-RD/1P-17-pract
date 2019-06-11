import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

import random
bukwa = (input("Буква:")).lower()
if bukwa in "aouei":
    print("Голосна")
elif bukwa == "y":
    rand = random.randint(0,1)
    if rand == 1:
        print("Голосна")
    else:
        print("Приголосна")
else:
    print("Приголосна")

printTimeStamp("Віталій Дудник")


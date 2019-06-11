import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

while True:
    coins = int(input("Кількість копійок: "))
    if coins > 0:
        break

fifty_cent = coins // 50
twenty_five__cent = (coins % 50) // 25
five_cent  = ((coins % 50) % 25 )// 5
two_cent   = (((coins % 25) % 10) % 5) // 2
one_cent   = (((coins % 25) % 10) % 5) % 2
print("50:", fifty_cent, "\n" +
    "25:", twenty_five__cent, "\n" +
    "5:", five_cent, "\n" +
    "2:", two_cent, "\n" +
    "1:", one_cent)

printTimeStamp("Віталій Дудник")
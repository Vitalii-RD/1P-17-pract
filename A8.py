import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

shtuka = int(input("Кількість штукчок: "))
shtukencia = int(input("Кількість штукенцій: "))
veight = shtuka*75 + shtukencia*112
print(veight/1000,"кг")

printTimeStamp("Віталій Дудник")

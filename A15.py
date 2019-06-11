import datetime

def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

n= int(input("Введіть число: "))
print("Сумма чисел: ", (n*(n+1))/2)

printTimeStamp("Даніїл Коробов")
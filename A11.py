import datetime

def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

numbers=[(int(input("Введіть число: "))) for x in range(3)]
print("Максимальне значення: ", max(numbers))
print("Середнє значення: ", sum(numbers)-min(numbers)-max(numbers))
print("Мінімальне значення : ", min(numbers))

printTimeStamp("Даніїл Коробов")
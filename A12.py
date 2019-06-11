import datetime

def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

numbers=[]
x = int(input("Введіть значення: "))
try:
    while x != 0:
        numbers.append(x)
        x = int(input("Введіть значення: "))
    print("Середнє значення: ", sum(numbers) / len(numbers))

except ZeroDivisionError:
    print("Помилка!")

printTimeStamp("Даніїл Коробов")


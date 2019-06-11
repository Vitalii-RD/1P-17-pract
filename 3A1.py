import datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
while True:
    x = input("Число 1: ")
    y = input("Чисол 2: ")
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        break
    else:
        print("Введено НЕ число")
def ggd(x,y):
    if x == y:
        return x
    elif x > y:
        return ggd(x - y, x)
    else:
        return ggd(x, y-x)
print(ggd(x,y))
printTimeStamp("Коробов Даніїл, Дудник Віталій")
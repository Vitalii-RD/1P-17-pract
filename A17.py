import math,datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

n= int(input("Введіть кількість сторін: "))
s= int(input("Введіть довжину сторони: "))
if n<3 or s<=0:
    print("Некорктні дані!")
else:
    print("Площа цьго полігону: ", (n*math.pow(s,2))/(4*math.tan(math.pi/n)))

printTimeStamp("Даніїл Коробов")
from math import factorial
import datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
a = lambda n,r: int(factorial(n) / (factorial(r) * factorial(n-r)))
while True:
    height = input("Введіть висоту трикутника: ")
    if height.isdigit():
        break
    else:
        print("Це не число")
height = int(height)
for n in range(height):
    for r in range(n+1):
        if r == 0:
            print(" "*(height-n)+str(a(n,r)),end=" ")
        else:
            print(a(n,r),end=" ")
    print("")
printTimeStamp("Коробов Даніїл, Дудник Віталій")

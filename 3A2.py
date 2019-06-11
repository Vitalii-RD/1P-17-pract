import datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
while True:
    n = input("Введіть бажане число Каталана: ")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Це не число!")
def Catalan_namber(n):
    if n >= 2:
        c = ((2 * ((2*n) - 1)) / (n+1)) * Catalan_namber(n-1)
        return int(c)
    else:
        return 1
print(Catalan_namber(n))
printTimeStamp("Коробов Даніїл, Дудник Віталій")
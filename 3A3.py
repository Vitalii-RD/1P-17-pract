import datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
while True:
    x = input("Введіть число: ")
    n = input("Введіть степінь: ")
    if n.isdigit() and is_number(x):
        x = int(x)
        n = int(n)
        break
    else:
        print("Введено не додатнє число!")
def stepin(x, n):
    if n == 0:
        return 1
    else:
        return x * stepin(x,n-1)
print(stepin(x,n))
printTimeStamp("Коробов Даніїл, Дудник Віталій")
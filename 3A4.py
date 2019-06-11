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
    if is_number(n) and is_number(x):
        x = int(x)
        n = int(n)
        break
    else:
        print("Введено не додатнє число!")
print(x,n)
def stepin(x, n):
    if n == 0:
        return 1
    elif n > 0 and n % 2 == 0:
        return stepin(x, n/2 )**2
    elif n > 0 and n % 2 != 0:
        return x * stepin(x,n-1)
    elif n < 0 :
        return 1 / stepin(x, -n)
print(stepin(x,n))
printTimeStamp("Коробов Даніїл, Дудник Віталій")
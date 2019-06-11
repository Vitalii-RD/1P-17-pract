import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

def func(n,m):
    d = min(n,m)
    while n % d != 0 or m % d != 0:
        d -= 1
    return d
n = int(input("Введіть 1-ше число: "))
m = int(input("Введіть 2-ше число: "))
print("НСД:",func(n,m))

printTimeStamp("Віталій Дудник")
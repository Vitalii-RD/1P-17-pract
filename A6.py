import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

c = int(input("Температура(в цельсія): "))
while True:
    number = input("Введіть 4-значне число: ")
    if len(number) == 4:
        break
suma = sum([int(i) for i in number])
print(suma)

printTimeStamp("Віталій Дудник")

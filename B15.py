import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

year = int(input("Рік: "))
if year % 400 == 0:
    print("Високосний")
elif year % 100:
    print("Невисокосний")
elif year % 4:
    print("Високосний")
else:
    print("Невисокосний")

printTimeStamp("Віталій Дудник")
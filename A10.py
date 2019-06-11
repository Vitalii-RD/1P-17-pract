import datetime
def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

print("Проміжо часу: ")
days1 = int(input("Дні: "))
hours1 = int(input("Години: "))
minutes1 = int(input("Хвилини: "))
seconds1 = int(input("Секунди: "))
sec = datetime.timedelta(days = days1, hours = hours1, minutes = minutes1, seconds = seconds1)
print(sec.total_seconds())

printTimeStamp("Віталій Дудник")

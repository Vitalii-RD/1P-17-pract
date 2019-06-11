import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

result = ""
q = int(input("Введіть число для конвертації: "))
while q != 0:
    r = q % 2
    result += str(r)
    q //=2
print("Двійкове представлення:",result)

printTimeStamp("Віталій Дудник")
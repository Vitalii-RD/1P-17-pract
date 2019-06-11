import datetime

def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

bukhanka = int(input("Ведіть кількість буханок: ".rjust(43)))
print("Звичайна вартість буханок: {:>10.2f}".rjust(53).format(bukhanka*8.50))
print("Вартість буханок зі скидкою: {:>10.2f}".rjust(55).format(bukhanka*8.50*0.6))

printTimeStamp("Даніїл Коробов")

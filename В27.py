import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))


print("Десяткова ","%8s" % "Символ","%10s" % "Двійкова","%10s" % "Вiсімкова","%15s" % "Шістнадцяткова")
for i in range(128):
    print("%5s" % i, "%10s" % chr(i), "%12s" % bin(i), "%9s" % oct(i), "%10s" % hex(i))

printTimeStamp("Віталій Дудник")

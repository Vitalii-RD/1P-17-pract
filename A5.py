import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

c = int(input("Температура(в цельсія): "))
f = round((9/5)*c)+32
k = c + 273
print("Цельсій", "%18s" % "Фаренгейт", "%18s" % "Кельвін")
print("%4s"%c,"%9s"% " - ", "%7s"% f, "%11s"% " - ", "%8s"%k)

printTimeStamp("Віталій Дудник")

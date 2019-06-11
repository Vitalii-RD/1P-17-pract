import datetime
def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

cm = float(input("Введіть зріст у см: "))
d = cm / 2.54
f = d / 12
print("Дюйми - %.3f" % d,'\n'+"Фути - %.3f" % f)
f = int(d // 12)
d = round(d-f*12)
print("Ваш зріст {} футів і {} дюймів".format(f,d))

printTimeStamp("Віталій Дудник")

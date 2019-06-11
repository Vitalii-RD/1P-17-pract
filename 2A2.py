import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

listok1 = []
while True:
    number = input("Введіть число:")
    if number == "":
        break
    elif not number.isdigit():
        print("Це не число")
    else:
        listok1.append(int(number))
average = sum(listok1) / len(listok1)
listok2 = []
listok3 = []
for i in listok1:
    if i < average:
        listok2.append(i)
    else:
        listok3.append(i)

print("1:", listok2)
print("2:", listok3)
printTimeStamp("Віталій Дудник")
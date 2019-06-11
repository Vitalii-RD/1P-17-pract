import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

while True:
    imei = input("IMEI: ")
    if len(imei) == 15:
        break
    else:
        print("Ви ввели не 15 символів, а", len(imei))
odd =  [int(i) for i in imei[:14:2]]
even = [int(i)*2 for i in imei[1:14:2]]
even = [int(str(i)[0])+int(str(i)[1]) if i > 9 else i for i in even]
print(odd)
print(even)
suma = str(sum(even)+ sum(odd))
if int(suma[-1]) == 0:
    print("Цифра Луна - 0")
else:
    lun = 10 - int(suma[-1])
    print("Цифра Луна -", lun)

printTimeStamp("Віталій Дудник")
import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

time = int(input("Час вдома: "))
home = input("Місце проживання: ")
if home == "Будинок" and time >= 18:
    print("Вам підходить в'єтнамське порося")
elif home == "Будинок" and 10<= time <= 17 :
    print("Вам підходить собака")
elif home == "Будинок" and time < 10 :
    print("Вам підходить змія")
elif home == "Квартира" and time >= 10:
    print("Вам підходить кішка")
elif home == "Квартира" and time <10:
    print("Вам підходить хом'як")
elif home == "Гуртожиток" and time >= 6 :
    print("Вам підходять рибки")
elif home == "Гуртожиток" and time < 6 :
    print("Вам підходить мурашник")

printTimeStamp("Віталій Дудник")
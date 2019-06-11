import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

v = float(input("Швидкість вітру(км/год): "))
t = int(input("Температура вітру(в градусах Цельсія): "))
if t >10 or v > 4.8:
    if v > 4.8:
        print("Індекс некоректний для швидкості вітру більше 4.8 км/год")
    if t >10:
        print("Індекс некоректний для температури більше 10 градусів Цельсія")
else:
    WCI = 13.12 + 0.6215 * t - 11.37 * v + 0.3965 * t * v
    print("Індекс прохолодності вітру",round(WCI))

printTimeStamp("Віталій Дудник")
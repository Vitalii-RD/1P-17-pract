import math,datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

week= {"понеділок": True,"вівторок": True,"середа":True,"четвер":True,"п'ятниця":True,"субота":False,"неділя":False}
try:
    holiday = input("Введіть день відпустки(якщо її немає то '0'): ").lower()
    week[holiday] = False
    day = input("Введіть день тиждня: ").lower()
    if week[day]:
        print("Дзінь-дзілінь!")
    else:
        print("Насолоджуйся сном))")
except KeyError:
    print("Такого дня не існує!")

printTimeStamp("Даніїл Коробов")
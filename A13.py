import datetime

def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

money = float(input("Введіть гроші, які покладите на рахунок: "))
for year in range(1,4):
    money = money * 1.14
    print("Грошей на балансі через {} рік: {:.2f}".format(year, money))

printTimeStamp("Даніїл Коробов")


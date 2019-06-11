import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

import  re
format1 = "[A-Z]{3}[0-9]{3}"
format2 = "[0-9]{4}[A-Z]{3}"
row_sumbol = input("Введіть рядок для перевірки:")
match1 = re.match(format1, row_sumbol)
match2 = re.match(format2, row_sumbol)
if match1:
    print("Співпало з форматом: 3 великі літери, 3 цифри")
elif match2:
    print("Співпало з форматом: 4 цифри, 3 великі літери")
else:
    print("Не співпадає з шаблоном")

printTimeStamp("Віталій Дудник")
import math,datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))


import time
sec= float(input("Введіть секунди: "))
vremya= time.gmtime(sec)
print(time.strftime('{}:{}:{}:{}'.format(vremya[2]-1,vremya[3] if vremya[3]> 9 else "0"+str(vremya[3]),vremya[4] if vremya[4]> 9 else "0"+str(vremya[4]),
                                         vremya[5] if vremya[5]> 9 else "0"+str(vremya[5]))))

printTimeStamp("Даніїл Коробов")
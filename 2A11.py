import random
import  datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
points =[]
for i in range(1000):
    points.append(random.randint(2,12))
print(" 2: {}%\n 3: {}%\n 4: {}%\n 5: {}%\n 6: {}%\n 7: {}%\n 8: {}%\n 9: {}%\n 10: {}%\n 11: {}%\n 12: {}% "
      .format(points.count(2)/10, points.count(3)/10, points.count(4)/10, points.count(5)/10, points.count(6)/10, points.count(7)/10,
              points.count(8)/10, points.count(9)/10, points.count(10)/10, points.count(11)/10, points.count(12)/10, ))
printTimeStamp("Коробов Даніїл, Дудник Віталій")


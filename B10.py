import math,datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

t1 = math.radians(float(input("Широта  т.1(в градусах): ")))
g1 = math.radians(float(input("Довгота т.1(в градусах): ")))
t2 = math.radians(float(input("Широта  т.2(в градусах): ")))
g2 = math.radians(float(input("Довгота т.2(в градусах): ")))
distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
print("Відстань",round(distance,2),"км")

printTimeStamp("Віталій Дудник")


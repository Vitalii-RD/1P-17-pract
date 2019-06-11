import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

import math
def dist(t1,g1,t2,g2):
    distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
    return distance

lviv_t = math.radians(49.83826)
lviv_g = math.radians(24.02324)

harkiv_t = math.radians(49.98081)
harkiv_g = math.radians(36.25272)

odesa_t = math.radians(46.47747)
odesa_g = math.radians(30.73262)

dist1 = dist(lviv_t,   lviv_g,   harkiv_t, harkiv_g)
dist2 = dist(harkiv_t, harkiv_g, odesa_t,  odesa_g)
dist3 = dist(lviv_t,   lviv_g,   odesa_t,  odesa_g)

p = (dist1 + dist2 + dist3)/2

area = math.sqrt(p*(p-dist1)*(p-dist2)*(p-dist3))
print("Площа трикутника між Одесою, Харківом та Львівом:",round(area, 2),"км")
printTimeStamp("Віталій Дудник")
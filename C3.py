import re, datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

coordinates = []
while True:
    coord = input("Координати: ")
    pattern = "[0-9]+\.?[0-9]*,[0-9]+\.?[0-9]*"
    if re.match(pattern, coord):
        coordinates.append((float(coord[:coord.index(",")]),float(coord[coord.index(",")+1:])))
    elif coord == "":
        break
    else:
        print("Неправильні кординати!")
print(coordinates)
x   = []; y   = []
x2  = []; xy  = []
n = len(coordinates)
for item in coordinates:
    x.append(item[0])
    y.append(item[1])
    xy.append(item[0]*item[1])
    x2.append(item[0]**2)

m = (sum(xy) - (sum(x)*sum(y)) / n) / (sum(x2) - (sum(x)**2) / n)
b = sum(y)/n - m*sum(x)/n
print("y = {:.2f}x + {:.1f}".format(m, b))
printTimeStamp("Віталій Дудник")
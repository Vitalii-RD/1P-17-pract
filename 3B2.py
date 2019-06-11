import datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
def distance(s, t):
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        if s[-1] == t[-1]:
            return distance(s[:-1], t[:-1])
        d1 = distance( s[:-1], t)+1
        d2 = distance( s, t[:-1])+1
        d3 = distance( s[:-1], t[:-1] )+1
        return min(d1, d2, d3)
s = input("1: ")
t = input("2: ")
print(distance(s, t))
printTimeStamp("Коробов Даніїл, Дудник Віталій")

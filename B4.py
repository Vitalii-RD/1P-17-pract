import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

n = int(input("Введіть число n: "))
listok = [i for i in range(n+1) if i > 1]
p = 2
while p < n:
    for i in listok:
        if p == i:
            continue
        elif i % p == 0:
            listok.remove(i)
    try:
        p = listok[listok.index(p)+1]
    except IndexError:
        break
print(listok)
printTimeStamp("Віталій Дудник")
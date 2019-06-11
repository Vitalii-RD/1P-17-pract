import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

n =[1,2,3,4,5,6,7,8,9,10]
print(n)
delete = int(input("Введіть число для видалення: "))
n.remove(delete)
if len(n) > 5:
    for i in range(3):
        n.remove(max(n))
        n.remove(min(n))
else:
    print("В списку недостатньо елементів")
print(n)
printTimeStamp("Віталій Дудник")
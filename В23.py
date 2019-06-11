import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

n = int(input("Спожито води: "))

first  = lambda n: n *  9.86 / 30
second = lambda n: n * 11.22 / 20
third  = lambda n: n * 13.06 / 10
fourth = lambda n: n *  17.89

if n <= 30:
    print("%.2f" % first(n), "грн") + 20
elif 30 < n <= 50:
    price = second(n - 30) + first(30) + 20
    print("%.2f" % price, "грн")
elif 50 < n <= 60:
    price = third(n - 50) + second(20) + first(30)+ 20
    print("%.2f" % price, "грн")
else:
    price = fourth(n-60) + third(10) + second(20) + first(30) + 20
    print("%.2f" % price, "грн")

printTimeStamp("Віталій Дудник")
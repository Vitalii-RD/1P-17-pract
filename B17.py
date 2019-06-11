import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

m = float(input("Маса води(г/мл): "))
T = float(input("Зміна температури:"))
C = 4.186
q = m*T*C

print("Кількість необхідної енергії:", q)

elect = 1.33
kBt_hour = q / (3.6 * 10**6)
price = elect * kBt_hour

print("%.2f" % price)

printTimeStamp("Віталій Дудник")
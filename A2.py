import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

kPa = int(input("Тиск(кПа): "))
psi = kPa * 145.038 * 10**(-3)
mmrt = kPa * 7.5
tex_atm = kPa * 0.102 * 10**(-1)
phis_atm = kPa * 0.987 * 10**(-2)
print(
"Міліметри ртутного стовпчика -",mmrt,"\n"+
"Фунти на квадратний дюйм -",psi,"\n"+
"Технічна атмосфера -",tex_atm,"\n"+
"Фізична атмосфера -",phis_atm)

printTimeStamp("Віталій Дудник")

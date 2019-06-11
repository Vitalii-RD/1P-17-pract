import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

print("Для зупинення введіть \"end\"")
gen = 0
while True:
    name = input("Назва страви: ")
    amount = int(input("Кількість страви: "))
    price = int(input("Ціна страви: "))
    gen += amount*price
    dali = input("Ще страава:")
    if dali == "end":
        break
chayovi = gen*0.14
podatok = gen * 0.18
sum_price = gen + podatok + chayovi
print("Ціна: ",gen,"\n"+
"Чайоі: %.2f" % chayovi,"\n"+
"Податок: %.2f" % podatok,"\n"+
"Всього: ", sum_price)

printTimeStamp("Віталій Дудник")

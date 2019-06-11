import datetime

def printTimeStamp(name):
    print('\nАвтор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

veight = int(input("Маса: "))
height = int(input("Зріст: "))
yes = str(input("Поставте \"+\",якщо вага в кг, а ріст в м, інакше поставте \"-\": "))
if yes == "+":
    imt = veight / height ** 2
elif yes == "-":
    imt = 703 *  veight / height ** 2
else:
    print("Неправильнй символ!")
print(imt)

printTimeStamp("Віталій Дудник")

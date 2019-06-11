import datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
suma = 0
while True:
    num = input("Число:")
    try:
        float(num)
    except ValueError:
        try:
            eval(num)
        except SyntaxError:
            print("Введено не число!")
        except NameError:
            print("Введено не число!")
        else:
            suma += eval(num)
            print(suma)
    else:
        suma += float(num)
        print(suma)
    if num == "":
        break
print(suma)
printTimeStamp("Коробов Даніїл, Дудник Віталій")
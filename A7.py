import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

while True:
    years = int(input("Людських років: "))
    if years >= 0:
        if years <= 1:
            print("Собачих років:",years*7)
        elif 1 < years <= 2:
            print("Собачих років:", 7 + 1.75*years)
        else:
            print("Собачих років:", 10.5 + (years-2)*4)
        break
    else:
        print("Число не може бути від'ємним")
        
printTimeStamp("Віталій Дудник")

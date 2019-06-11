import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

mark = input("Введіть буквену оцінку: ")
if mark == "A+":
    print(5.0)
elif mark == "A":
    print(4.0)
elif mark == "A-":
    print(3.7)
elif mark == "B+":
    print(3.3)
elif mark == "B":
    print(3.0)
elif mark == "B-":
    print(2.7)
elif mark == "C+":
    print(2.3)
elif mark == "C":
    print(2.0)
elif mark == "C-":
    print(1.7)
elif mark == "D+":
    print(1.3)
elif mark == "D":
    print(1.0)
elif mark == "F":
    print(0)
else:
    print("Немає такої оцінки")
printTimeStamp("Віталій Дудник")



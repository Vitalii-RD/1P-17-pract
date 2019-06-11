import datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
while True:
    num = input("Введіть число для градової послідавності: ")
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Це не додатнє число!")
def Hansone_seq(n):
    if n == 1:
        return "КІНЕЦЬ!"
    else:
        if num == n:
            print("ПОЧАТОК:"+"\n"+str(n))
        if n % 2 == 0:
            print(n / 2)
            return Hansone_seq(n / 2)
        else:
            print(3* n + 1)
            return Hansone_seq(3* n + 1)
print(Hansone_seq(num))
printTimeStamp("Коробов Даніїл, Дудник Віталій")
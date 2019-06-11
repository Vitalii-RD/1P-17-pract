import datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
parol = "Abc123#@"
user = "Vitaliy"
while True:
    username  = input("Ведіть логін: ")
    passsword = input("Ведіть пароль: ")
    if parol == passsword and user == username:
        with open("A9.txt", "r") as file:
            print(file.read())
            break
    else:
        print("Неправильний пароль або логін!")
printTimeStamp("Коробов Даніїл, Дудник Віталій")

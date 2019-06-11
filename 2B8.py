import  datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
oper = input("Введіть оператор: ")
def precedence(operator):
    if operator in ["-","+"]:
        return 1
    if operator in ["*","/"]:
        return 2
    if operator == "^":
        return 3
    else:
        return -1

if precedence(oper) >= 1:
    print("Пріорітет операції:",precedence(oper))
elif precedence(oper)== -1:
    print("Невірні дані!")
printTimeStamp("Коробов Даніїл, Дудник Віталій")

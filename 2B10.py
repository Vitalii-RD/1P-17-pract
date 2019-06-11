import re, datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
ip = input("Введіть свою IPv4 адресу: ")
val= re.split("\.", ip)
proverka=0
if len(val) != 4:
    print("IPv4 адреса неправильна!")
else:
    for i in val:
        if int(i) >255 or int(i)<0:
            print("IPv4 адреса неправильна!")
            proverka+=1
            break
    if proverka==0:
        print("Адреса валідна")
printTimeStamp("Коробов Даніїл, Дудник Віталій")

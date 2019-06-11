import sys
import  datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
if len(sys.argv)<1:
    print("Має бути 2 аргумента!")
else:
    a = sys.argv[1]
    b = sys.argv[2]
    with open(a) as file:
        text1 = file.read()
    with open(b) as file:
        text2 = file.read()
    text3 = text1 +"\n"+ text2
    print(text3)
printTimeStamp("Коробов Даніїл, Дудник Віталій")
# A17.py A17(1).txt A17(2).txt

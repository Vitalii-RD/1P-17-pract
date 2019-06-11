import re
import  datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
points =[]
file = open("3B3.txt")
text = file.read().lower()
print(text)
for i in "abcdefghijklmnopqrstuvwxyz":
     print("The letter {} is found {} times".format(i.upper(),len(re.findall(i, text))))
printTimeStamp("Коробов Даніїл, Дудник Віталій")

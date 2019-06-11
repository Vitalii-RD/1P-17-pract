import datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
with open("A7.txt","a+") as file:
    file.seek(0)
    print("До:\n"+file.read())
    file.write("\n"+"Дудник Віталій Романович")
    file.seek(0)
    print("Після:\n"+file.read())
printTimeStamp("Коробов Даніїл, Дудник Віталій")

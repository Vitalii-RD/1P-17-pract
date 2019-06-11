import datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

with open("A8.txt", "r") as file:
    text = file.read()
    print("До:\n" +text)
with open("A8.txt", "w") as file:
    text = text.replace("\n"," ")
    file.write(text)
with open("A8.txt", "r") as file:
    print("Після:\n" + file.read())
printTimeStamp("Коробов Даніїл, Дудник Віталій")

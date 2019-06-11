import  datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
with open("B11(dict).txt") as file:
    text = file.read().split(", ")
    print(text)
    dictionary = {i : 0 for i in text}
with open("B11(text).txt") as file:
    text = file.read().lower().replace(",","").split(" ")
    print(text)
print("Непрвильні слова:")
for word in text:
    if word not in dictionary:
        print(word)
printTimeStamp("Коробов Даніїл, Дудник Віталій")
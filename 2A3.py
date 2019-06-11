import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

words = set()
while True:
    word = input("Введіть слово:")
    if word == "":
        break
        
    else:
        words.add(word)
for i in words:
    print(i)

printTimeStamp("Віталій Дудник")
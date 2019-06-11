import datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
dictionary = {1: ["A", "E", "I", "L", "N", "O", "R", "S", "T", "U"],
              2: ["D", "G"], 3:["B", "C", "M", "P"], 5: ["K"],
              4: ["F", "H", "V", "W", "Y"], 8: ["J", "X"], 10:["Q", "Z"]}
words = input("Word(s): ")
words = words.split(" ")
for word in words:
    result = 0
    for letter in word:
        for key, values in dictionary.items():
            for value in values:
                if value == letter.upper():
                   result += key
    print(word,"-",result)
printTimeStamp("Коробов Даніїл, Дудник Віталій")
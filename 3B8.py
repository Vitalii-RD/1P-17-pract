import datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
dictionary = {"A" : ".-",   "B" : "-...", "C" : "-.-." , "D" : "-..", "E" : ".",
              "F" : "..-.", "G" : "--.",  "H" : "....",  "I" : "..",
              "J" : ".---", "K" : "-.-",  "L" : ".-..",  "M" : "--",
              "N" : "-.",   "O" : "---",  "P" : ".--.",  "Q" : "--.-",
              "R" : ".-.",  "S" : "...",  "T" : "-",     "U" : "..-",
              "V" : "...-", "W" : ".--",  "X" : "-..-",  "Y" : "-.--",
              "Z" : "--..", "0" : "-----","1" : ".----", "2" : "..---",
              "3" : "...--","4" : "....-","5" : ".....", "6" : "-....",
              "7" : "--...","8" : "---..","9" : "----."}
text = input("Введіть текст: ").upper()
for letter in text:
    if  letter not in dictionary:
        text = text.replace(letter,"")
for key, value in dictionary.items():
    text = text.replace(key,value)
print(text)
printTimeStamp("Коробов Даніїл, Дудник Віталій")

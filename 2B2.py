import datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
dictionary = {1: [".", ",", "?", "!", ":"], 2: ["A", "B", "C"],
              3: ["D", "E", "F"],           4: ["G", "H", "I"],
              5: ["J", "K", "L"],           6: ["M", "N", "O"],
              7: ["P", "Q", "R", "S"],      8: ["T", "U", "V"],
              9: ["W", "X", "Y", "Z"],     10: [" "]}
text = (input("Text:")).upper()
for i in text:
    for key, values in dictionary.items():
        for value in values:
            if value == i:
                print(str(key)*(values.index(i)+1), end="")
printTimeStamp("Коробов Даніїл, Дудник Віталій")

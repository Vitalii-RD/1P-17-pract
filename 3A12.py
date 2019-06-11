import datetime,os
from collections import Counter
def printTimeStamp(name):
    print('\nАвтор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
while True:
    infile = input("Введіть назву вхідного файлу: ")
    if os.path.exists("{}.txt".format(infile)):
        break

with open("{}.txt".format(infile), "r") as file:
    text = file.read().lower()
    punctuation = [".", ",", "!", "?", "«","»"]
    for i in punctuation:
        text = text.replace(i, "")
    text = text.split(" ")
    count  = Counter(text)
    for i in count.most_common(3):
        print(i[0], " - ",i[1])
printTimeStamp("Коробов Даніїл, Дудник Віталій")

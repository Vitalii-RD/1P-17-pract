import datetime, os
def printTimeStamp(name):
    print('\nАвтор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
while True:
    infile = input("Введіть назву вхідного файлу: ")
    if os.path.exists("{}.txt".format(infile)):
        break
outfile = input("Введіть назву вихідного файлу: ")
with open("{}.txt".format(infile), "r") as file:
    text = file.read().split("\n")
    print(text)
    for item in text:
        if item.isspace() or item == "":

            text.remove(item)
        else:
            text[text.index(item)] = str(text.index(item)+1) + ". " + item
    print(text)
with open("{}.txt".format(outfile),"w") as file:
    file.write("\n".join(text))
printTimeStamp("Коробов Даніїл, Дудник Віталій")
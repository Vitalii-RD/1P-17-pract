import re, datetime, os
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
while True:
    infile = input("Назва вхідного файла: ")
    if os.path.exists("%s.py"%infile):
        break
outfile= input("Введіть нову назву: ")
new_text = []
with open("%s.py"%infile, "r+") as file:
    text = file.read().split("\n")
    for row in text:
        amount = re.findall("#", row)
        if len(amount) >= 1:
            new_text.append(row[:row.index("#")])
        else:
            new_text.append(row)
    for i in new_text:
        if i.isspace():
            new_text.remove(i)
    file.truncate(0)
    file.write("\n".join(new_text))
os.rename("%s.py"%infile, "%s.py"%outfile)
printTimeStamp("Коробов Даніїл, Дудник Віталій")
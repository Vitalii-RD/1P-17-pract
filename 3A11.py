import datetime
def printTimeStamp(name):
    print('\nАвтор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
with open("A11.txt","r") as file:
    text = file.read().replace("\n", " ").split(" ")
    maks = 0
    listok = []
    for item in text:
        if len(item) > maks:
            maks = len(item)
            listok.clear()
            listok.append(item)
        elif len(item) == maks:
            listok.append(item)
print("Довжина найдовшого слова:", maks)
print("Слова:", ", ".join(listok))
printTimeStamp("Коробов Даніїл, Дудник Віталій")
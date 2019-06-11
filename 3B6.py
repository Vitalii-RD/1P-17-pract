import  datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
file = open("3B6.txt")
text = file.read()
print(text)
symbol= []
colich=0
start=0
finish = 1
while finish != len(text):
    symbol.append(text[start])
    while len(set(text[start:finish]))==1:
        colich+=1
        finish+=1
    symbol.append(colich)
    colich=0
    start= finish-1
print("Текст був зжатий на {} %".format(100-(100*len(symbol)/len(text))))
with open("compressed.txt","w")as file_comp:
    for i in symbol:
        file_comp.write(str(i))
with open("decompressed.txt","w")as file_decomp:
    for i in symbol:
        if symbol.index(i)%2==0:
            t= i*(symbol[symbol.index(i)+1])
            file_decomp.write(t)
printTimeStamp("Коробов Даніїл, Дудник Віталій")
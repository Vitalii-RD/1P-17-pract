import datetime, re
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

expression = input("Введіть вираз для токенізації: ")
tokens = [i for i in expression.replace(" ","")]
tokens1 = []
for i in range(len(tokens)-1):
    try :
        while True:
            if tokens[i].isdigit() and tokens[i+1].isdigit():
                tokens[i] = tokens[i] + tokens[i+1]
                tokens.remove(tokens[i+1])
            else:
                break
    except IndexError:
        pass
i = 0
while i != len(tokens):
    item = tokens[i]
    if item in "*/^()":
        tokens1.append(item)
    elif item in "+-":
        if tokens[i-1] not in "/*^()" and re.match("[0-9]",tokens[i+1][0]):
            tokens1.append(item)
        else:
            tokens1.append(item)
            tokens1.append(tokens[tokens.index(item) + 1] + tokens[tokens.index(item) + 2])
            i += 2
    elif item.isdigit():
        tokens1.append(item)
    i += 1
for i in  tokens1:
    if i.isdigit():
        print(i, "-  число" )
    elif i in "/*^+-":
        print(i, "-  оператор")
    elif i == "()":
        print(i, "-  дужка")
    elif i[0] in "+-" and i[1].isdigit():
        print(i, "-  число з опційним знаком")
printTimeStamp("Дудник Віталій, Коробов Даніїл")

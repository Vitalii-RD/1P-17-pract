import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

expression = input("Математичний вираз: ")
tokens = [i for i in expression.replace(" ","")]
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
for i in tokens:
    if i.isdigit():
        print(i, "- число")
    elif i in "()":
        print(i, "- дужка")
    else:
        print(i, "- оператр")
printTimeStamp("Віталій Дудник")
import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

values = []
expression = input("Інфіксований вираз: ")
tokens = [i for i in expression]
for i in range(len(tokens)-1):
    try :
        if tokens[i] == " ":
            tokens.remove(" ")
        while True:
            if tokens[i].isdigit() and tokens[i+1].isdigit():
                tokens[i] = tokens[i] + tokens[i+1]
                tokens.remove(tokens[i+1])
            else:
                break
    except IndexError:
        pass
print(tokens)
for token in tokens:
    if token.isdigit():
        values.append(int(token))
    else:
        right = values[-1]
        values.remove(values[-1])
        left = values[-1]
        values.remove(values[-1])
        result = eval("{} {} {}".format(right, token ,left))
        values.append(result)
print(values)

printTimeStamp("Віталій Дудник")

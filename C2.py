import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

values = []
expression = input("Постфіксований вираз: ")
tokens = [i for i in expression]
for i in range(len(tokens)-1):
    try :
        if tokens[i] == " ":
            tokens.remove(" ")
        while True:
            if tokens[i].isdigit() and tokens[i+1].isdigit():
                tokens[i] = tokens[i] + tokens[i+1]
                tokens.remove(tokens[i+1])
            if tokens[i] in "+-" and tokens[i+1].isdigit():
                tokens[i] = tokens[i] + tokens[i + 1]
                tokens.remove(tokens[i + 1])
            else:
                break
    except IndexError:
        pass

for token in tokens:
    if is_number(token):
        values.append(int(token))
    else:
        right = values[-1]
        values.remove(values[-1])
        left = values[-1]
        values.remove(values[-1])
        result = eval("{} {} {}".format(left, token ,right))
        values.append(result)
print(values[0])
printTimeStamp("Віталій Дудник")

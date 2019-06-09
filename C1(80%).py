import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

operators = []
postfixs =[]
expression = input("Інфіксований вираз: ")

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
print(tokens)
for token in tokens:
    if token.isdigit():
        postfixs.append(token)
    if token in "*/+-()":
        while operators != [] and operators[-1] != "(" and precedence(token) < precedence(operators[-1]):
            print("add",operators[-1], token)
            postfixs.append(operators[-1])
            operators.remove(operators[-1])
        operators.append(token)
    if token == "(":
        operators.append(token)
    if token == "(":
        while operators[-1] != "(":
            postfixs.append(operators[-1])
            operators.remove(operators[-1])
        operators.remove("(")

while operators != []:
    postfixs.append(operators[-1])
    operators.remove(operators[-1])

print(postfixs)
printTimeStamp("Віталій Дудник")
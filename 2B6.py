import datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
one = ["одна", "дві", "три", "чотири", "п'ять", "шість", "сім", "вісім", "дев'ять"]
two_one = ["одинадцять", "дванадцять", "тринадцять", "чотирнадцять", "п'ятнадцять",
       "шістнадцять", "сімнадцять", "вісімнадцять", "дев'ятнадять"]
two = ["","двадцять", "тридцять", "сорок", "п'ятдесят", "шістдесят", "сімдесят", "вісімдесят", "д'евяносто"]
# в списку two перший елемент пустий для правильного індексу
three = ["сто", "двісті", "триста", "чотириста", "п'ятсот", "шістсот", "сімсот","вісімсот", "дев'ятсот"]
four = ["одна тисяча", "дві тисячі", "три тисячі","чотири тисячі", "п'ять тисяч",
        "шість тисяч", "сім тисяч", "вісім тисяч", "дев'ять тисяч"]
five = ["десять тисяч"]
dictionary = {0:one, 1:two, 2:three, 3:four, 4:five}
while True:
    n = input("Число для конвертації: ")
    if n.isdigit():
        if 0 < int(n) <= 10000:
            break
        else:
            print("Число не в діапазоні від 0 до 10 000")
    else:
        print("Це не число")
n = str(n)
grn = []
for i in range(len(n)):
    if int(n[-1-i]) != 0:
        if i == 0 and n[-2] == 1:
            word = two_one[int(n[-1])-1]
            grn.append(word)
            print(i, word)
        elif i == 1 and n[-2] == 1:
            continue
        else:
            word = dictionary.get(i)[int(n[-1-i])-1]
            grn.append(word)
            print(i, word)
    else:
        continue
grn.reverse()
print(grn, "грн")
printTimeStamp("Коробов Даніїл, Дудник Віталій")
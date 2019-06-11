import random, datetime

def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

points = 0
attempt =1 # Попытка, добавлеться если три пары или шесть одинаковых
while attempt == 1:
    attempt -= 1
    bone= [random.randint(1,6) for i in range(6)]
    print(bone)
    break_group = 0 #Ввел для того что бы если уже нашло 3 или больше одинаковых костей (1*), то не стработали условие "с тремя парми" (2*)
    for i in range(1,7):
        if bone.count(i) >= 3:
            print("{} однакові кості '{}' +{}".format(bone.count(i), i,(bone.count(i) - 2) * 100 *(10 if i == 1 else i)))
            points += (bone.count(i) - 2) * 100 *(10 if i == 1 else i)
            break_group +=1     #(1*)

    if len(set(bone))==3 and break_group == 0: # (2*) Тут считаеться когда у тебя три пары костей(сет убирает все одинаковые элементы, а потом считает количество), но может быть [1,1,1,1,2,3] и он посчитает что там 3 пары, для этго и ввел break_group = 0
        print("Три пари +750 та ще одна спроба")
        points += 750
        attempt += 1
    elif break_group==0:
        points += bone.count(1) * 100
        points += bone.count(5) * 50

    if len(set(bone)) == 6:
        print("Три пари +1500 та ще одна спроба")
        points += 1500
        attempt += 1
print("Ваші очки:", points)

printTimeStamp("Даніїл Коробов")
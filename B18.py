bukva= {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
poza= input("Введіть позіцію на дощці: ")
try:
    if 0>=int(poza[0]) or int(poza[0])>=9:
         print("Некоректний ввід!")
    elif (int(poza[0])%2== 1 and bukva[poza[1]]%2==1) or (int(poza[0])%2== 0 and bukva[poza[1]]%2==0):
        print("Квадрат чорний!")
    else:
        print("Квадрат білий!")
except KeyError:
    print("Некоректний ввід!")
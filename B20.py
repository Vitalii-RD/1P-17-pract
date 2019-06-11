import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

def ABCDF(mark):
    if 4 < mark <= 5:
        return "A+"
    elif 3.7 < mark <=4:
        return "A"
    elif 3.3 < mark <= 3.7 :
        return "A-"
    elif 3.0 < mark <= 3.3:
        return "B+"
    elif 2.7< mark <= 3.0:
        return "B"
    elif 2.3< mark < 2.7:
        return "B-"
    elif 2.0 < mark <= 2.3:
        return "C+"
    elif 1.7 < mark <2.0:
        return "C"
    elif 1.3 < mark <= 1.7:
        return "C-"
    elif 1.0 < mark <= 1.3:
        return "D+"
    elif 0 < mark <= 1.0:
        return "D"
    elif mark == 0:
        return "F"
    else:
        return"Немає такої оцінки"
marks = []
while True:
    mark = int(input("Оцінка: "))
    if mark == -1:
        break
    marks.append(mark)
    print("Буквений варіант:",ABCDF(mark))

average = sum(marks)/len(marks)
print("Середній бал по групі:",str(average)+". Буквений варіант:",ABCDF(average))

printTimeStamp("Віталій Дудник")
import datetime,random

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

red = ["1","3","5","7","9","12","14","16","18","19","21","23','25",'27','30',"32","34","36"]
random_numb = random.randint(0,37)
if random_numb == 37:
    random_numb = "00"
print("На рулетці випало",random_numb,"\n"+"Виплатити",random_numb)

if str(random_numb) in "00":
    print("Виплатити зелене")
elif str(random_numb) in red:
    print("Виплатити красне")
else:
    print("Виплатити чорне")

if str(random_numb) == "0" and "00":
    pass
elif int(random_numb) % 2 == 0:
    print("Виплатити парні")
else:
    print("Виплатити непарні")

if 0 < random_numb < 19:
    print("Виплатити від 1 до 18")
elif 18 < random_numb < 37:
    print("Виплатити від 19 до 36")
else:
    pass
printTimeStamp("Віталій Дудник")
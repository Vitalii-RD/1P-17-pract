import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

n = int(input("Enter number: "))
noise = {130: "Jackhammer", 106: "Gasvlawnmover", 70: "Alarm clock", 40: "Quiet room"}
if n in noise:
    print("Noise type: ",noise.get(n))
elif n > 130 :
    print("Шум вищий за табличний")
elif n < 40:
    print("Шум нижчий за табличний")

else:
    maks = n
    min = n
    while maks not in noise:
        maks += 1
    while min not in noise:
        min  -= 1
    print("Noise type between",noise.get(maks),"and",noise.get(min))

printTimeStamp("Віталій Дудник")
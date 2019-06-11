import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

frequency = int(input("Enter frequency:"))
if  0 < frequency < 3 * 10**9:
    print("Radio waves")
elif 3 * 10**9 < frequency < 3 * 10**12:
    print("Microwaves")
elif 3 * 10**12< frequency < 4.3 * 10**14:
    print("Infrared light")
elif 4.3 * 10**14 < frequency < 7.5 * 10**14:
    print("Visiable light")
elif 7.5 * 10**14 < frequency < 3 * 10 **17:
    print("Ultraviolet light")
elif 3 * 10**17 < frequency < 3 *10**19:
    print("X-rays")
else:
    print("Gamma rays")

printTimeStamp("Віталій Дудник")
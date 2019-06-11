import winsound, datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

arrey = [(659,250), (659,250), (659,300), (523,250), (659,250), (784,300),
         (392,300), (523,275), (392,275), (330,275), (440,250), (494,250),
         (466,275), (440,275), (392,275), (659,250), (784,250), (880,275),
         (698,275), (784,225), (659,250), (523,250), (587,225), (494,225)]
frequency = [i[0] for i in arrey]
duration = [i[1] for i in arrey]
i = 0
while i != len(arrey):
    winsound.Beep(frequency[i], duration[i])
    i += 1

printTimeStamp("Віталій Дудник")
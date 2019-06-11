import datetime

def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))


fourth_octave= {"C": 261.63, "D": 293.66, "E": 329.63, "F": 349.23, "G": 392.00, "A": 440.00, "B": 493.88}
x= input("Ведіть ноту, щоб узнати її частоту, або частоту, щоб знайти ноту: ")
try:
    note = x[0]
    octave = int(x[1])
    note_hz = fourth_octave[note] / 2**(4-octave)
    print("Частота ноти {}: {} Гц".format(x, note_hz))
except KeyError:
  x= float(x)
  stop=0
  start_octaves = 4
  iter= 0
  while -1< start_octaves < 9:
    if stop == -1:
      break
    if iter > 56:
      print("Нота поза діапазону")
      break
    if x > 493.88:
      x=x/2
      start_octaves += 1
    if x < 261.63:
      x = x * 2
      start_octaves -= 1
    for i in fourth_octave:
      if  x == fourth_octave[i]:
        print("Це частота ноти:", i+str(start_octaves))
        stop= -1
    iter+=1
  else:
    print("Нота поза діапазону")

printTimeStamp("Даніїл Коробов")
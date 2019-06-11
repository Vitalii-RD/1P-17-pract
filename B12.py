import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

year = int(input("Введіть рік: "))
animals = {
    2000:"Dragon", 2001:"Snake", 2002:"Horse", 2003:"Sheep", 2004:"Monkey", 2005:"Rooster",
    2006:"Dog",    2007:"Pig",   2008:"Rat",   2009:"Ox",    2010:"Tiger",  2011:"Hare"}
if year in animals:
    print(animals.get(year))
else:
    if year < 2000:
        while year not in animals:
            year += 12
        print(animals.get(year))
    else:
        while year not in animals:
            year -= 12
        print(animals.get(year))

printTimeStamp("Віталій Дудник")
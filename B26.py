import datetime
def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

factor = 2
try:
    n = int(input("Enter the integer(2 or greater): "))
except n < 2:
    print("Error (n < 2)!")
else:
    print("The prime factors of",str(n),"are:")
    while factor <= n:
        if n % factor == 0:
            n /= factor
            print(factor)
        else:
            factor += 1

printTimeStamp("Віталій Дудник")
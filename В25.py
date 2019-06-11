import datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

for row in range(11):
    if row == 0:
        print("  ",end = "")
        for column in range(1, 11):
            print(str(column).rjust(4), end="")
    else:
        print(str(row).rjust(2), end = "")
        for column in range(1,11):
            print(str(column*row).rjust(4), end="")
    print("")

printTimeStamp("Віталій Дудник")
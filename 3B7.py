import datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
k = int(input("Key: "))
plaintext = input("plaintext: ")
print("ciphertext: ", end="")
for i in plaintext:
    if 64 < ord(i) < 91:
        ciphertext = chr(((((ord(i) + k) - 65) % 26) + 65))
        print(ciphertext, end="")
    elif 96 < ord(i) < 123:
        ciphertext = chr(((((ord(i) + k) - 97) % 26) + 97))
        print(ciphertext, end="")
    else:
        print(i, end="")
print("\n")
printTimeStamp("Коробов Даніїл, Дудник Віталій")
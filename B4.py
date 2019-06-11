num=[]
isbn= input("Введіть номер ISBN: ")
while len(isbn) != 13:
    print("У номері повинно бути 13 цифр!")
    isbn = int(input("Введіть номер ISBN: "))
for i in range(12):
    if i%2==0:
        num.append(int(isbn[i]))
    else:
        num.append(int(isbn[i])*3)
if 10-(sum(num)%10)== int(isbn[12]):
    print("Номер валідний!")
else:
    print("Номер не валідний!")



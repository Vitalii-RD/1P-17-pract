import math
koordinaty=[]
dlina=[]
for a in range(3):
    x= int(input("Enter the x part of the coordinate:"))
    y= int(input("Enter the y part of the coordinate:"))
    koordinaty.append((x,y))
try:
    while x!= " ":
        x = input("Enter the x part of the coordinate(blank to quit): ")
        y = input("Enter the y part of the coordinate(blank to quit): ")
        koordinaty.append((int(x),int(y)))
except ValueError:
    for i in koordinaty:
        try:
            dlina.append(math.sqrt((koordinaty[koordinaty.index(i)+1][0]-i[0])**2+(koordinaty[koordinaty.index(i)+1][1]-i[1])**2))
        except IndexError:
            dlina.append(math.sqrt((koordinaty[0][0] - i[0]) ** 2 + (koordinaty[0][1] - i[1]) ** 2))

print("Периметер:",sum(dlina))
propuski=[7,4,2,1,0]
c = 3
for x in range(5):
    print(propuski[x]*" "+"x"*c)
    c+= (propuski[x]- propuski[x+(1 if x<4 else 0)])*2
for x in range(1,6):
    print(propuski[-x]*" "+"x"*c)
    c-= ((propuski[-x-1] if x<5 else 10) - propuski[-x])*2

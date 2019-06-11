import  datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
reserv = {1:True, 2:True, 3:True, 4:True, 5:True, 6:True, 7:True, 8:True, 9:True, 10:True, 11:True, 12:True}
place= 0
def business():
    global place
    for i in range(1, 7):
        if reserv[i] == True:
            print("Ваше посадкове місце {}. Бізнес-клас".format(i))
            reserv[i] = False
            place += 1
            break
    else:
        print("Місця бызнес-класу закінчились!")
        pic= int(input("Натисніть '1' якщо хочете зарезервувати місця в економ-класі/ Натисніть '2' для відміни: "))
        if pic == 1:
            economy()
        else:
            print("Наступний виліт через 3 години")
            place=12
def economy():
    global place
    for i in range(7,13):
        if reserv[i]== True:
            print("Ваше посадкове місце {}. Економ-клас".format(i))
            reserv[i] = False
            place += 1
            break
    else:
        print("Місця економ-класу закінчились!")
        pic = int(input("Натисніть '1' якщо хочете зарезервувати місця в бізнес-класі/ Натисніть '2' для відміни: "))
        if pic == 1:
            business()
        else:
            print("Наступний виліт через 3 години")
            place = 12
while place != 12:
    num = int(input("Натисніть '1' для першого класу/ Натисніть '2' для економного класу/ Натисніть '3' для виходу: "))
    if num== 1:
        business()
    if num == 2:
        economy()
    if num==3:
        print("Наступний виліт через 3 години")
        place = 12
printTimeStamp("Коробов Даніїл, Дудник Віталій")





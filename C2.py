neadekvat=1
while  neadekvat ==1:
    neadekvat-=1
    year = int(input("Введіть рік: "))
    month = int(input("Введіть місяць: "))
    day = int(input("Введіть день: "))
    feva= int(str(year)[-2:])
    if (month or year or day) <= 0 or (month==2 and year%4==0 and day>=29):
        print("Ти неaдаекват!!!")
        neadekvat+=1
        break
    if (day == 31 and (month == 1 or 3 or 5 or 7 or 8 or 10 or 12)) or (day== 30 and (month == 2 or 4 or 6 or 9 or 11)) or (day==28 and month== 2 and feva%4 !=0) or (day==29 and month== 2 and feva%4 ==0):
        day= 1
        year =year if month != 12 else year+1
        month=1 if month==12 else month+1
    else:
        day+=1
    print("Наступний день: {}-{}-{}".format(year, (month if month>9 else "0"+str(month)), (day if day>9 else "0"+str(day))))
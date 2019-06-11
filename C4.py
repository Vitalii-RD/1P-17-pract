tariff = input("Введіть цифру тарифу яким користуєтесь:")
megabytes = int(input("Введіть скільки мегабайтів використали:"))
if tariff == "1000":
        print("Сейчас вы платите {} за {}  Мб, а с Тарифом 2000 - {}, а с Тарифом 5000 - {}".format(((((megabytes- 1000) * 0.05)if megabytes>=1000 else 0)+20),
            megabytes, ((((megabytes- 2000) * 0.04)+35) if megabytes> 2000 else 35),((((megabytes- 5000) * 0.02)+85) if megabytes> 5000 else 85) ))
elif tariff == "2000":
        print("Сейчас вы платите {} за {}  Мб, а с Тарифом 5000 - {} ".format((((((megabytes- 2000) * 0.04)if megabytes>=2000 else 0)+35)), megabytes,((((megabytes- 5000) * 0.02)+85) if megabytes> 5000 else 85)))
elif tariff == "5000":
        print("Сейчас вы платите {} за {}  Мб".format(((((megabytes- 5000)if megabytes>=5000 else 0) * 0.02)+85), megabytes))
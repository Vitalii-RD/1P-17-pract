s_temperature= int(input("Введіть температуру на вулиці: "))
r_temperature= int(input("Введіть температуру в кімнаті: "))
chasiki=0
k=0
termostat=True
while chasiki!= 24:
    if  5<=chasiki<=15:
        s_temperature+=1
    else:
        s_temperature-=1
    if 22<=r_temperature<=24 and termostat==True:
        termostat= False
        k=0
        for i in range(8):
            print("Температура в кімнаті - {:.2f}`C. Година - {}:00. Термостат працює.".format(r_temperature,chasiki if chasiki> 9 else "0"+str(chasiki)))
            r_temperature= r_temperature+k*abs((r_temperature-s_temperature))
            if 5 <= chasiki <= 15:
                s_temperature += 1
            else:
                s_temperature -= 1
            chasiki+=1
    elif 22<=r_temperature<=24 and termostat==False:
        k=-0.02
        r_temperature = r_temperature + k * abs((r_temperature - s_temperature))
        chasiki+=1
        print("Температура в кімнаті - {:.2f}`C. Година - {}:00. Всі прилади вимкнені.".format(r_temperature,chasiki if chasiki > 9 else "0" + str(chasiki)))

    elif r_temperature<22:
        k=0.11
        r_temperature = r_temperature + k * abs((r_temperature - s_temperature))
        chasiki+=1
        print("Температура в кімнаті - {:.2f}`C. Година - {}:00. Обігрівач працює.".format(r_temperature,chasiki if chasiki > 9 else "0" + str(chasiki)))

    elif r_temperature>24:
        k=-0.09
        r_temperature = r_temperature + k * abs((r_temperature - s_temperature))
        chasiki+=1
        print("Температура в кімнаті - {:.2f}`C. Година - {}:00. Кондіціонер працює.".format(r_temperature,chasiki if chasiki > 9 else "0" + str(chasiki)))
        chasiki+=1



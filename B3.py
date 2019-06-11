min= int(input("Введіть кіл-сть витрачених хвилин: "))
mes= int(input("Введіть кіл-сть написаних повідомлень: "))
rakhunok=35
if min> 200:
    rakhunok+= (min - 200) * 0.17
if mes > 50:
    rakhunok+= (mes - 50) * 0.15
print("Рахунок з податками: {:.2f}".format(rakhunok))
print("Чистий рахунок: {:.2f}".format(rakhunok-0.44-(rakhunok*0.05)))


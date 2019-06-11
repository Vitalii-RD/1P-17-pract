import re, datetime

def printTimeStamp(name):

  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

province = {"A": "Newfoundland", "B": "Nove Scotia", "C": "Prince Edward Island",
            "S": "Saskatchewan", "T": "Albera",      "V": "British Columbia",
            "X": "Nunavut or Northwest Territories", "Y": "Yukon","R":"Manitoba",
            "E": "New Brunswick", "G":"Quebec", "H":"Quebec", "J":"Quebec",
            "K":"Ontario", "L":"Ontario", "M":"Ontario", "N":"Ontario", "P":"Ontario"}
code = input("Enter mail-code: ")
print(code)
pattern = "([A-Z][0-9]){3}"
if re.match(pattern, code):
    if code[0] in province:
        print("Province:", province.get(code[0]))
    else:
        print("Uncorrect mail-code. D, F, I, O, Q, U, W and Z can not be first letter")
    if code[1] == 0:
        print("Type: Village")
    else:
        print("Type: City")
else:
    print("Uncorrect mail-code")
printTimeStamp("Коробов Даніїл, Дудник Віталій")
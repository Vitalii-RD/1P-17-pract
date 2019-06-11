import re, datetime
def printTimeStamp(name):
  print('\nАвтор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
points =[]
text = input("Enter text: ")
words = re.split(" ", text)
vowels= re.findall("e|i|u|o|a", text.lower())
consonants =re.findall("B|C|D|F|G|J|K|L|M|N|P|Q|R|S|T|V|W|X|Y|Z", text.upper())
big =re.findall("[A-Z]", text)
small =re.findall("[a-z]", text)
space =re.findall(" ", text)
letters =re.findall("[A-Za-z]", text)
numbers =re.findall("\d", text)
print(words)
print("Words: {} Letters: {} Number: {} Space: {} Big letters: {} Small letters: {} Vowels: {} Consonants: {}".format
      (len(words),len(letters),len(numbers), len(space), len(big), len(small), len(vowels), len(consonants)))
printTimeStamp("Коробов Даніїл, Дудник Віталій")
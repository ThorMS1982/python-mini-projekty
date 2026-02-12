import random, string

chars = string.punctuation + string.digits + string.ascii_letters + " "

chars = list(chars)
key = chars.copy()

random.shuffle(key)


czysty_tekst = input('Podaj tekst do zakodowania: ')
zakodowany_tekst = ""

for i in czysty_tekst:
    index = chars.index(i)
    zakodowany_tekst += key[index]

print(f'Czysty tekst: {czysty_tekst}')
print(f'Zakodowany tekst: {zakodowany_tekst}')

#Dla porownania znaki :
#print(chars)
#print(key)


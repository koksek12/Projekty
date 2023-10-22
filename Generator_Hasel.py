import random

#Litery do hasła
words = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

#Długość hasła
pass_lenght = int(input("ile liter ma mieć hasło?"))

#Hasło
password = ""

#Pisanie hasła
for i in range(pass_lenght):
    password += random.choice(words)

#Wypisywanie hasła
print(password)

# ASCII art Spēle "Karātavas"

import random

# Iespējamie vārdi
words = ["Cikls", "Galds", "Blokshēma", "Algoritms", "Skaitītājs", "Dators", ]

# Izvēlās vārdu pēc nejaušības principa
word = random.choice(words)

# Pārveido vārdu uz CAPS (lielajiem burtiem)
word = word.upper()

# Izveido tukšu sarakstu, lai saglabātu spēlētāja uzminētos burtus
guessed_letters = []

# Ievietot mēģinājumu / dzīvību daudzumu: 5
num_guesses = 5

# Atkārto tikmēr spēlētājs ir izmantojis visas dzīvības vai pareizi uzminējis vārdu
while num_guesses > 0:
    # Izprintē ASCII art
    print("    _______")
    print("   |/      |")
    print("   |      ({})".format(" " if num_guesses < 6 else ""))
    print("   |      \\|/")
    print("   |       |")
    print("   |      / \\")
    print("___|___")
    print()

    # Izprintē vārdu ar apakšsvītrām priekš neuzminētiem burtiem
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)

    # Spēlētājam tiek prasīts ievadīt burtu
    guess = input("Ievadi Burtu: ").upper()

    # Pārbauda vai burts jau ir izmantots iepriekš
    if guess in guessed_letters:
        print("Jūs jau minējāt šo burtu!")
    # Pārbauda vai burts ietilpst vārdā
    elif guess in word:
        print("Pareizi!")
        guessed_letters.append(guess)
    # Ja burts vārdā ir nepareizs, izdod šādu frāzi: "Nepareizi"
    else:
        print("Nepareizi!")
        num_guesses -= 1

    # Pārbauda vai spēlētājs ir vārdu uzminējis pareizi
    if all(letter in guessed_letters for letter in word):
        print("Apsveicam Uzvarētājus!")
        break

# Ja spēlētājs ir izmantojis visas savas dzīvības neuzminot vārdu, tas parāda ASCII art priekš Zaudējuma
if num_guesses == 5:
    print("    _______")
    print("   |/      |")
    print("   |      (_)")
    print("   |      \|/")
    print("   |       |")
    print("   |      / \\")
    print("___|___")
    print()
    print("Jums Beidzās dzīvības, vārds bija: {}.".format(word))
from random import randint


print("*** Jeu du nombre mystère ***")
nb_mystère = randint(0,100)
essai = 5

while essai > 0:
    print(f"il te reste {essai} essais")
    nb_user = input("Devine le nombre : ")
    if nb_user.isdigit() != True:
        print("Entre un nombre valide")
        continue
    else:
        nb_mystère = int(nb_mystère)
        nb_user = int(nb_user)
        if nb_user > nb_mystère:
            print(f"Le nombre mystère est plus petit que {nb_user}")
        elif nb_user < nb_mystère:
            print(f"le nombre mystère est plus grand que {nb_user}")
        else:
            break
        
    essai -= 1
if essai == 0:
    print(f"Perdu le nombre mystère est {nb_mystère}")
else:
    print(f"Tu as trouvé le nombre en {6 - essai} essai ")
    print(f"Bravo ! Le nombre mystère est {nb_user}")
        
        
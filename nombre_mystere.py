from random import randint


def verification(valeur):
    valid = False

    while not valid:
        try:
            valeur = int(valeur)
            assert 1 <= valeur <= 100
            valid = True
        except ValueError:
            valeur = input("Veuillez entrer un nombre entier compris entre 1 et 100")
        except AssertionError:
            valeur = input("Veuillez entrer un nombre entier compris entre 1 et 100")

    return valeur


nombre = randint(1, 100)
element = input("Quel est le nombre ?")
element = verification(element)
compteur = 1


while element != nombre:
    compteur += 1
    if element > nombre:
        print("C'est trop grand")
        element = input("Quel est le nombre ?")
        element = verification(element)
    else:
        print("C'est trop petit")
        element = input("Quel est le nombre ?")
        element = verification(element)

print("Félicitations, vous avez trouvé le nombre mystere en", compteur, "coups")

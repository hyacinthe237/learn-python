#coding:utf-8

"""
Nommer une variable : doit commencer par une lettre ou un uderscore
                      ne doit pas contenir de caractères spéciaux
                      ne pas contenir d'espaces
                      utiliser des underscores (_)

Types standards     : entier numérique (int)
                    nombre floattant (float)
                    chaine de caractères (str)
                    booléen (bool) True ou False

Fonctions vues : print() -> afficher à l'écran
                input() -> lire au clavier
                type() -> retourne le type d'une donnée, variable etc...
                str.format() -> formater une chaîne
                int(), float(), str(), bool() -> "caster" une donnée, la convertir sans lui changer son type

agePersonne = 34
prixHt = 120.3456
agePersonne2 = "34"
continuerPartie = True
nePasContinuer = False

texte = "L'age de la personne est {} et le prix HT est de {} XAF"
print(texte.format(agePersonne, prixHt))

nomJoueur = input("Saisissez un nom de joueur : ")
print("Bienvenue, ", nomJoueur)

prixHT = input("Saisissez un un prix HT : ")
prixHT = int(prixHT)
prixTTC = prixHT + (prixHT * 20/100)
print("Prix TTC =", prixTTC)
"""


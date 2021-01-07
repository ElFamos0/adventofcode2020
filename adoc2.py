'''
ELFAMOSO
Donner seulement les mots de passes valides
'''
with open("adoc2.txt") as file:
    data = [line for line in file]

#Partie1
ok = 0
for entry in data:
    entry = entry.split() #WTf ça supprime le /n on est béni des dieux
    numbers = entry[0].split(sep="-")
    lettre = entry[1][0] #On prend le premier élément de la liste b: par exemple
    minimum = int(numbers[0])
    maximum = int(numbers[1])
    motdepasse = entry[2]

    if minimum <= motdepasse.count(lettre) <= maximum:
        ok += 1
print(ok)
# Très largement inspiré de 0xVector (Merci monsieur pour les connaissances)
'''
Mtn les mots de passes valides sont ceux qui possèdent uniquement la lettre indiqué à une seule des deux positions c'est à dire que si la lettre est sur les deux positions c'est faux
'''
#Partie2 on se ressert du mapping vu avant (et non parce que la position est décalé de 1 super giga cool)
ok = 0
for entry in data:
    entry = entry.split() #WTf ça supprime le /n on est béni des dieux
    numbers = entry[0].split(sep="-")
    lettre = entry[1][0] #On prend le premier élément de la liste b: par exemple
    pos1 = int(numbers[0])-1
    pos2 = int(numbers[1])-1
    motdepasse = entry[2]
    if ((motdepasse[pos1] == lettre) ^ (motdepasse[pos2] == lettre)):
        ok+=1
print(ok)

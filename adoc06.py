"""
ELFAMOSO
"""

with open("inputs/adoc6.txt") as file:
	data = [ligne.strip() for ligne in file]
groupe = []
groupes = []
somme = 0

for element in data: #première boucle de traitement des données
	if element == "":
		groupes.append(groupe)
		groupe = []
	else:
		groupe.append(element)
#Partie1
for groupe in groupes:
	reponseoui = []
	for mot in groupe:
		for i in range(len(mot)):
			if mot[i] not in reponseoui:
				reponseoui.append(mot[i])
	somme += len(reponseoui)	
print(somme)

#Partie2

for groupe in groupes:
	for mot in groupe:
		reponseoui = [mot[0][i] for i in range (len mot[0])]
		for i in range(len(mot)):
			if mot[i] not in reponseoui:



part1 = sum(len(set.union(*map(set, groupe))) for groupe in groupes)
part2 = sum(len(set.intersection(*map(set, groupe))) for groupe in groupes)
print(part1, part2)
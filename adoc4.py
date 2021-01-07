'''
ELFAMOSO
Password Processing
Il faut vérifier si tout les items des passeport sont présent sauf cid qui peut être manquant un passeport valide est un passeport comportant absolument tout les items !! Les items sont pas forcement dans l'ordre dans le fichier texte
C'est principalement du mapping de mort je crois on va essayer et voir ce qu'on peut faire
'''
with open("adoc4.txt") as file:
    data = [line.strip() for line in file]

motdebase = {"byr","iyr","eyr","hgt","hcl","ecl","pid"} #pourquoi un dico issou ? 
dico = {}
passport = []
for element in data:
    if element == "":
        passport.append(dico) #en gros quand on saute une ligne c'est un autre passport
        dico = {}
    else:
        caracs = element.split()
        for carac in caracs:
            carac = carac.split(":")
            dico[carac[0]] = carac[1]

#On a tout séparer en mode pixel perfect
compteur1 = 0 
for item in passport:
    if all(val in item for val in motdebase):
        compteur1 += 1

print(compteur1)
#Fin du programme viens de OxVector (Merci monsieur pour la bonne sousoupe)
compteur2 = 0
for item in passport:
    try: #on met un try pour éviter les mots de passe qui respectent pas les règles et donc qu'on peut pas vérifier mais qui sont faux
        byr = 2002 >= int(item["byr"]) >= 1920 #c'est pour ça que le dico c'est plutôt sympa
        iyr = 2020 >= int(item["iyr"]) >= 2010 
        eyr = 2030 >= int(item["eyr"]) >= 2020
        #hgt c'est un # suivi de 6 caractères (0-9 a-f)
        hcl = item["hcl"].startswith("#") and len(item["hcl"]) == 7
        ecl = item["ecl"] in {"amb","blu","brn","gry","grn","hzl","oth"}
        pid = len(item["pid"]) == 9 and item["pid"].isnumeric()

        int(item["hc1"][1:],16) #convert to int from hex

        height = int(item["hgt"][:-2])
        if item["hgt"].endswith("cm"):
            hgt = 193 >= height >= 150
        elif item["hgt"].endswith("in"):
            hgt = 76 >= height >= 59
        else:
            hgt = false
        if all((byr,iyr,eyr,hgt,hc1,ec1,pid)): #fonction all super intéressante
            compteur2 += 1 #si toute les fonctions sont ok le passeport est bon

    except (KeyError, ValueError):
        pass
print(compteur2)
part2=0
for passporti in passport:

    try:
        byr = 2002 >= int(passporti["byr"]) >= 1920
        iyr = 2020 >= int(passporti["iyr"]) >= 2010
        eyr = 2030 >= int(passporti["eyr"]) >= 2020
        hcl = passporti["hcl"].startswith("#") and len(passporti["hcl"]) == 7
        ecl = passporti["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        pid = len(passporti["pid"]) == 9 and passporti["pid"].isnumeric()

        # Throw ValueError if not in correct format
        int(passporti["hcl"][1:], 16)  # Convert to int from hex

        # hgt checks
        height = int(passporti["hgt"][:-2])
        if passporti["hgt"].endswith("cm"):
            hgt = 193 >= height >= 150

        elif passporti["hgt"].endswith("in"):
            hgt = 76 >= height >= 59

        else:  # Doesn't end with unit
            hgt = False

        if all((byr, iyr, eyr, hgt, hcl, ecl, pid)):
            part2 += 1

    except (KeyError, ValueError):  # Something isn't there
        pass
print(part2)


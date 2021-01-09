'''
ELFAMOSO
'''
filin = open("inputs/adoc01.txt","r") #on ouvre le fichier en lecture
nombres = filin.readlines()
for i in range(len(nombres)):
    nombres[i]= nombres[i].strip("\n")
    nombres[i]=int(nombres[i])

def trouver2020(liste):
    for i in range(len(liste)):
        for j in range(1+i,len(liste)):
            if liste[i]+liste[j]==2020:
                print(liste[i]*liste[j])        

#trouver2020(nombres)

def trouver2020bis(liste):
    for i in range(len(liste)):
        for j in range(1+i,len(liste)):
            for k in range(1+j,len(liste)):
                if liste[i]+liste[j]+liste[k]==2020:
                    print(liste[i]*liste[j]*liste[k])
trouver2020bis(nombres)

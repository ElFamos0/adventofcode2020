'''
ElFamoso Script Code Advend 2020 

Je suis la reine de salopes si je cherche sur internet c'est dis mtn
je n'ai pas été une salope c'est beau
For example, consider just the first seven characters of FBFBBFFRLR:

    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.

For example, consider just the last 3 characters of FBFBBFFRLR:

    Start by considering the whole range, columns 0 through 7.
    R means to take the upper half, keeping columns 4 through 7.
    L means to take the lower half, keeping columns 4 through 5.
    The final R keeps the upper of the two, column 5.
'''

with open("adoc5.txt") as file:
    data = [line[0:-1] for line in file]#je suis vrm supercool  

maxdefou = 0 
for ligne in data:
    mini, maxi = 0, 127
    mini2, maxi2 = 0, 7
    intervalle = [mini,maxi]
    intervalle2 = [mini2,maxi2]
    for i in range(7):
        if ligne[i] == "F":
            maxi = (maxi+mini)//2
            intervalle = [mini,maxi]
        elif ligne[i] == "B":
            mini = (maxi+mini)//2+1
            intervalle = [mini,maxi]
            '''
            if i == 6:
                intervalle[0] +=
                '''
    for j in range(7,10):
        if ligne[j] == "L":
            maxi2 = (maxi2+mini2)//2
            intervalle2 = [mini2,maxi2]
        elif ligne[j] == "R":
            mini2 = (maxi2+mini2)//2+1
            intervalle2 = [mini2,maxi2]
            '''if i == 9:
                intervalle[0] += 1
                '''
    print(intervalle[0],intervalle2[0])
    if intervalle[0]*8+intervalle2[0] > maxdefou:
        maxdefou = intervalle[0]*8+intervalle2[0]
print(maxdefou)
print("--------------------------------------------------------------------------------------------")

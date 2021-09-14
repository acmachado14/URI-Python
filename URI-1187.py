M = [[0 for j in range(12)]for i in range(12)]

O = input()

for i in range (len(M)):
    for j in range (len(M[0])):
        M[i][j] = float(input())

soma = 0
inf = 1
sup = 11
cont = 0
for i in range(0,5):
    for j in range(inf,sup):
        soma += M[i][j]
        cont += 1
    inf += 1
    sup -= 1

   

med = soma / cont

if O == "S":      
    print("%.1f"%soma)      
elif O == "M":
    print("%.1f"%med)
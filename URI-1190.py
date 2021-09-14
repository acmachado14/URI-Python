M = [[0 for j in range(12)]for i in range(12)]

O = input()

for i in range (len(M)):
    for j in range (len(M[0])):
        M[i][j] = float(input())

cont = 0
col = 11
soma = 0.0
for i in range(1,11):
    for j in range(col,12):
        soma += M[i][j]
      
        cont += 1
    if i < 5:
        col -= 1
    if i > 5:
        col += 1
  
   

med = soma / cont

if O == "S":      
    print("%.1f"%soma)      
elif O == "M":
    print("%.1f"%(soma/12))
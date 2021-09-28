while (True):
    N = int(input())    
    if N < 2 or N > 10000:
        break
    
    botas = [0 for k in range(N)]
    cont = 0
    for i in range(N):
        X = input()
        botas.append(X)
        for j in range(len(botas))

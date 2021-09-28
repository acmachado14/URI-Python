def a(mat,i,j):
    p = 0
    l = len(mat) -1
    c = len(mat[i]) -1

    if (i > 0 and mat[i - 1][j] == 1): 
        p +=1
    if (i < l and mat[i + 1][j] == 1):
        p +=1
    if (j > 0 and mat[i][j - 1] == 1): 
        p +=1
    if (j < c and mat[i][j + 1] == 1): 
        p +=1

    return p

while True:    
    try:
        N, M = input().split(" ")
        N = int(N)
        M = int(M)

        if N < 1 or N > 100:
            break

        if M < 1 or M > 100:
            break

        mat = [[0 for b in range(M)] for x in range(N)]

        for i in range(N):
            s = input().split(" ")
            for j in range(M):
                mat[i][j] = int(s[j])
            

        for i in range(N):
            for j in range(M):
                if (mat[i][j] == 1): 
                    print("9", end="")
                else: 
                    print(a(mat, i, j), end="")
            
            print()
    except EOFError:
        break

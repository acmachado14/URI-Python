X = [0 for i in range(10)]
for i in range(10):
    x = int(input())
    if (x <= 0):
        x = 1
    X[i] = x
    
for i in range(10):
    print('X[{}] = {}'.format(i,X[i]))


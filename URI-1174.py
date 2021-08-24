A = [0 for i in range(100)]

for i in range(100):
    A[i] = float(input())

for i in range(100):
    if A[i] <= 10:
        print('A[{}] = {}'.format(i,A[i]))

N = int(input())

while N < 0 and N > 46:
    N = int(input())

cont = 0
fibo = 0
a=1
b=1
if N==1:
    print(f'0', end=' ')
elif N==2:
    print(f'0 1', end=' ')
else:
    print(f'0 1 1', end=' ')
    for i in range(N-3):
        total = a + b
        b=a
        a= total
        print(f'{total}', end=' ')

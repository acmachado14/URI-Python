N = int(input())
if N < 0 or N > 1000000:
    print("numero invalido")
else:
    print(N)
    num100 = N // 100
    resto100 = N % 100
    N = num100
    print(N, "nota(s) de R$ 100,00")
    num50 = resto100 // 50
    resto50 = resto100 % 50
    N = num50
    print(N, "nota(s) de R$ 50,00")
    num20 = resto50 // 20
    resto20 = resto50 % 20
    N = num20
    print(N, "nota(s) de R$ 20,00")
    num10 = resto20 // 10
    resto10 = resto20 % 10
    N = num10
    print(N, "nota(s) de R$ 10,00")
    num5 = resto10 // 5
    resto5 = resto10 % 5
    N = num5
    print(N, "nota(s) de R$ 5,00")
    num2 = resto5 // 2
    resto2 = resto5 % 2
    N = num2
    print(N, "nota(s) de R$ 2,00")
    num1 = resto2 // 1
    resto1 = resto2% 1
    N = num1
    print(N, "nota(s) de R$ 1,00")
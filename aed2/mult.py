op1 = [0, 9, 8, 1]
op2 = [1, 2, 3, 4]
produto = [0, 0, 0, 0, 0, 0, 0, 0]
aux = 0
a = 0

while a <= 3:
    pp = -1 + (a * -1)
    resto = [0, 0, 0, 0]
    for i in range(len(op1) - 1, -1, -1):
        aux = op2[i] * op1[i]
        if resto[i] != 0:
            aux += resto[i]
        if aux >= 10:
            resto[i - 1] = (aux % 100) // 10
        produto[pp] += aux % 10
        if produto[pp] >= 10:
            resto[i - 2] = (aux % 100) // 10
            produto[pp] = produto[pp] % 10
        pp += - 1
    a += 1

print(produto)
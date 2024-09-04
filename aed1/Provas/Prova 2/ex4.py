# PROVA DE SEXTA
# 4. Crie um programa que leia um númeiro inteiro e escreva todos os divisores desse número. EXEMPLO: 14 --> 1, 2, 7, 14; 17 --> 1, 17; 24 --> 1, 2, 3, 4, 6, 8, 12, 24. 

n = int(input('Digite um número: '))
c = 2
divisores = '1'

while c <= n:
    if n % c == 0:
        divisor = str(c)
        divisores = divisores + ', ' + divisor
    c += 1

print(f'O número {n} tem como divisores: {divisores}')
#22. Faça um programa em python que leia um valor inteiro X. Em seguida apresente os 6 valores ÍMPARES consecutivos a partir de X, 
# inclusive o X se for o caso. Por exemplo, para o número 8, a saída será “9,11,13,15,17,19”.

n = int(input('Digite um valor inteiro: '))
c = 0

while c < 6:
    if n % 2 != 0:
        if c == 0:
            print(n, end='')
        else:
            print(f', {n}', end='')
        c += 1
    n += 1

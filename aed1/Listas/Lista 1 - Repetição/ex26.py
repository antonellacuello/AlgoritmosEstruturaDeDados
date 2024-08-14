# 26. Construa um programa em Python que escreva uma contagem de 10 (dez) minutos, ou seja, mostre 0:00, e então 0:01, 0:02, ..., 0:58, 0:59, 1:00, 1:01, ..., até 10:00.

s = 0
m = 0

while m != 10:
    while s <= 59:
        if s < 10:
            print(f'{m}:0{s}')
            s += 1
        if s > 9:
            print(f'{m}:{s}')
            s += 1
    m += 1
    s = 0

print(f'{m}:0{s}')
    

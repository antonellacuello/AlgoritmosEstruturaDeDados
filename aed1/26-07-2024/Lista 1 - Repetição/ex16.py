#16. Escreva um programa que receba um número inteiro positivo do usuário e verifique se ele é primo.

n = int(input('Digite um número inteiro e positivo: '))

while n < 0:
  n = int(input('Digite um número INTEIRO e POSITIVO: '))

if n <= 1:
    print(f'{n} não é um número primo.')
else:
    primo = True
    divisor = 2
    
    while divisor * divisor <= n:
        if n % divisor == 0:
            primo = False
            break
        divisor += 1
    

    if primo == True:
        print(f'{n} é um número primo.')
    else:
        print(f'{n} não é um número primo.')

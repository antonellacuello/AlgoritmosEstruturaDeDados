#15. Escreva um programa que calcule e mostre a soma dos números de 1 a N. Não utilize as equações de progressão aritmética.

n = int(input('Digite um número inteiro positivo: '))
soma = 0
c = 1

while n <= 0:
  n = int(input('Digite um número INTEIRO e POSITIVO: '))

while c <= n:
  soma += c
  c += 1
    
print(f'A soma dos números de 1 a {n} é {soma}.')

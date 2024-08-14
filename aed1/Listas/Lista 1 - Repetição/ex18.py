# 18. Escreva um programa que calcule o fatorial de um número fornecido pelo usuário. O fatorial de um número n é o produto de todos os números inteiros de 1 a n.

n = int(input('Digite um número: '))
c = 1
f = 1

while c <= n:
	f *= c
	print(f, c)
	c += 1
	
print(f'O fatorial de {n} é {f}')

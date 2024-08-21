# 17. Escreva um programa que mostre a sequência de Fibonacci até o enésimo termo (n deve ser informado pelo usuário). A sequência de Fibonacci é aquela em que cada termo é a soma dos dois termos anteriores. Por exemplo, para n=8 escreva 0, 1, 1, 2, 3, 5, 8 e 13.
'''
n = 1 -> 0; n = 2 -> 1; n = 3 -> 1; n = 4 -> 2; n = 6 -> 5; n = 10 -> 34
'''
n = 10 #int(input('Digite um número: '))
c = 3
f = 0
f1 = 1
f2 = 0

print(f'A sequência Fibonacci de {n} é:')
print(f'0 -> {f2}')
print(f'1 -> {f1}')
 
while c <= n:
	f = f1 + f2
	print(f'{c} -> {f}')
	c += 1
	f2 = f1
	f1 = f
	print(c)

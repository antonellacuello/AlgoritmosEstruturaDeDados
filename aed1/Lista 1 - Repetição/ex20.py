# 20. Escreva um programa que leia diversos funcionários e seu respectivo salario, ate que o nome de um funcionário seja “fim”. Em seguida escreva:
''' a) O nome do funcionário com maior salário
    b) O nome do funcionário com menor salário
    c) A média dos salários digitados'''
    
f = input('Digite o nome do funcionário: ')
s = float(input('Digite o respectivo salário: '))
c = 1
soma = s
smax = s
smin = s
fRico = f
fPobre = f

while f != 'fim':
	f = input('Digite o nome do funcionário: ')
	if f == 'fim':
		print('tchau.')
	else:
		s = float(input('Digite o respectivo salário: '))
		if s > smax:
			smax = s
			fRico = f
		if s < smin:
			smin = s
			fPobre = f
		c += 1
		soma += s
	
media = (soma / c)
print(soma, c)
print(f'O funcionário com maior salário é {fRico}. \nO funcionário com menor salário é o {fPobre}. \nA média dos salários é {media}')

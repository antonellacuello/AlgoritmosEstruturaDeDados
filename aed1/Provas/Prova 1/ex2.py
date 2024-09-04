# PROVA DE QUARTA
# 2. Leia uma data inicial e um número de dias. Calcule e escreva a data correspondente ao número de dias. EX: 01/01/2024; 55; 25/02/2024

'''dia_inicial = int(input('Insira o dia inicial: '))
mes_inicial = int(input('Insira o mes inicial: '))
ano_inicial = int(input('Insira o ano inicial: '))
num_dias = int(input('Digite o número de dias que deseja percorrer: '))'''

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
num_dias = int(input('Digite o número de dias que deseja percorrer: '))
# data = True
c = 0

# funciona para alguns casos 
while c < num_dias:
	if dia == 31 and mes == 12:
		print('zzz')
		dia = 1
		mes = 1
		ano += 1
	elif ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia == 30) or ((mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8) and dia == 31) or (mes == 2 and dia == 28):
		dia = 1
		mes += 1
	else:
		dia += 1
	c += 1

print(f'{dia}/{mes}/{ano}')

# teste 98734983490
'''while c < num_dias:
	if mes == 2:
		while dia < 28:
			dia += 1
			c += 1
	elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
		while dia < 30:
			dia += 1
			c += 1
	elif mes == 12 and dia == 31:
		print('zzz')
		mes = 1
		dia = 1
		ano += 1
	else:
		while dia < 31:
			dia += 1
			c += 1
	mes += 1
		#ano += 1
		#mes = 1	
print(f'{dia}/{mes}/{ano}')'''

# validação 
'''if dia > 31 or mes > 12:
	print('Data inválida!')
else:
	if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
		print('Data inválida!')
	else:
		if mes == 2 and dia > 28:
			print('Data inválida!')
		else: 
			print('Data válida!')'''
		

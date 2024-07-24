# 1. Leia uma data DD, MM, AAAA e diga se ela é válida. 
# b) Considere ano bissexto. 
# Ano bissexto tem que ser divisivel por 4 ou por 400 mas nao pode ser divisivel por 100

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
b = ''

if (ano % 4 == 0 or ano % 400 == 0) and ano % 100 != 0:
	b = ' Ano bissexto!'
	if (dia > 31 or mes > 12):
		print('Data inválida!')
	else:
		if mes == 2 and dia == 29:
			print('Data válida!' + b)
		else:
			if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
				print('Data inválida!')
			else:
				print('Data válida!' + b)
else: 
	b = ' Ano não bissexto!'
	if dia > 31 or mes > 12:
		print('Data inválida!')
	else:
		if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
			print('Data inválida!')
		else:
			if mes == 2 and dia > 28:
				print('Data inválida!')
			else:
				print('Data válida!' + b)

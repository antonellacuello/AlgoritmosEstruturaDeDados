# 1. Leia uma data DD, MM, AAAA e diga se ela é válida. 
# a) Desconsidere ano bissexto;

'''dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if dia > 31 or mes > 12:
	print('Data inválida!')
else:
	if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
		print('Data inválida!')
	else:
		if mes == 2 and dia > 28:
			print('Data inválida!')
		else: 
			print('Data válida!')'''

# 7. b) Crie um programa em Pyhon que leia uma data (DD/MM/AAAA) e diga se a data é válida. Considere anos bissextos.

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
c = 0

if ano % 100 != 0 and (ano % 4 == 0 or ano % 400 == 0):
	b = True
else: 
	b = False

print(b)

if dia > 31 or dia < 0 or mes > 12 or mes < 1 or (mes == 2 and dia > 29):
	print('Data inválida!')
else:
	if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
		print('Data inválida!')
	else:
		if mes == 2 and dia == 29:
			if b != True:
				print('Data inválida!')
			else:
				print('Data válida!')

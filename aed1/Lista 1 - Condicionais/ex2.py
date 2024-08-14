#2. Faça um programa em python que pergunte ao usuário o seguinte:
#		- A viagem custará menos de R$ 30?
#    	- Terá Wifi?
#    	- Terá piscina?
#    	- Terá churrasqueira?
# O programa deverá mostrar se a viagem ocorrerá de acordo com as seguintes regras:
#    	- Deverá custar menos de R$ 30
#    	- Tem que ter wifi e piscina
#    	- Se não tiver wifi ou piscina, tem que ter churrasqueira

custo = input('A viagem custará menos de R$ 30? ')
wifi = input('Terá Wifi? ')
piscina = input('Terá piscina? ')
churrasqueira = input('Terá churrasqueira? ')

if custo == 's' and (wifi == 's' and piscina == 's'):
	print('Ocorrerá viagem.')
else:
	if wifi == 'n' or piscina == 'n':
		if churrasqueira == 's':
			print('Ocorrerá viagem.')
		else: 
			print('Não ocorrerá viagem.')

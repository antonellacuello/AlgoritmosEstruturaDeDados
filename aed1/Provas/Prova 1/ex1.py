# 1. Leia os lados de um retângulo e imprima sua área. Verifique para que o usuário insira apenas números positivos.
l1 = float(input('Digite o primeiro lado do retângulo: '))

while l1 < 0: 
	print('Digite apenas valores POSITIVOS!')
	l1 = float(input('Digite o primeiro lado do retângulo: '))
	
l2 = float(input('Digite o segundo, e último, lado do retângulo: '))
	
while l2 < 0:
	print('Digite apenas valores POSITIVOS!')
	l2 = float(input('Digite o segundo, e último, lado do retângulo: '))

area = l1 * l2
print(area)

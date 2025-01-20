# 1. Faça um programa que, ao receber os valores da largura e do comprimento de uma figura geométrica, mostre se esta é um quadrado ou apenas um retângulo. 
# Caso um valor seja menor ou igual a zero, deve-se mostrar um erro.

l = int(input('Insira a largura da figura: '))
c = int(input('Insira o comprimento da figura: '))

if l <= 0 or c <= 0:
	print('Error 404')
else:
	if l == c:
		print('A figura geométrica é um QUADRADO!')
	else:
		print('A figura geométrica é um RETÂNGULO!')

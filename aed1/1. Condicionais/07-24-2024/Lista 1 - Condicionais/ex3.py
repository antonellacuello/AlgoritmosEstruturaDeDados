# 3. Construa um programa em python que, informadas três medidas a, b e c pelo usuário, verifique se elas podem ser lados de um triângulo. Se não puderem ser, primeiramente o algoritmo deve informar isso. Se for possível serem lados de triângulo, deve dizer qual tipo de triângulo pode ser construído com essas medidas (isósceles, escaleno ou equilátero). A condição para formar um triângulo: comprimento do maior segmento seja inferior à soma dos comprimentos dos dois menores.

a = int(input('Insira o primeiro lado do triângulo: '))
b = int(input('Insira o segundo lado do triângulo: '))
c = int(input('Insira o terceiro, e último, lado do triângulo: '))

if a > b and a > c:
	M = a
	m = b + c
elif b > a and b > c:
	M = b
	m = a + c
else:
	M = c
	m = a + b

if M <= m:
	if a == b and a == c and b == c:
		print('O triângulo é EQUILÁTERO!')
	elif a != b and a != c and b != c:
		print('O triângulo é ESCALENO!')
	else:
		print('O triângulo é ISÓSCELES!')
else:
	print('Não é um triângulo.')		

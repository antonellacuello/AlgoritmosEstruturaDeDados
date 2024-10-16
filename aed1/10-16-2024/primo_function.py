def verificarPrimo(valor):
	if valor <= 1:
		return False
	else:
		primo = True
		divisor = 2
		
		while divisor * divisor <= valor:
		    if valor % divisor == 0:
		        primo = False
		        break
		    divisor += 1

		if primo == True:
			return True
		else:
			return False

n = int(input('Digite um valor: '))
if verificarPrimo(n):
	print('É primo.')
else:
	print('Não é primo.')

# Prisco
def eh_primo(num):
	cont = 2
	while cont < num:
		if num % cont == 0:
			return False
		cont = cont + 1
	return True

for i in range(100, 200):
	if eh_primo(i):
		print(i)

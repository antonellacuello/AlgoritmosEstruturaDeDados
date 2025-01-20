# Aula do dia 16/10/2024 - FUNÇÕES

def dobro(num):
	saida = num * 2
	return saida

numero = int(input('num: '))
duplo = dobro(numero)
print(duplo + 1)

def verificarPar(valor):
	if valor % 2 == 0:
		return True       #só retorna um return, dps dele nada mais acontece
	return False

def teste():
	print('Volta ás aulas!')
	return 2
	print('Amamos grama sendo cortadakkkkk')

teste()

print(verificarPar(numero))
if verificarPar(numero):
	print('Par!')
else:
	print('Ímpar!')

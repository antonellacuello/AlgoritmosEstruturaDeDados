# 19. Escreva um programa que leia diversos números até que o usuário digite zero. Em seguida escreva a média dos números digitados.

n = int(input('Digite alguns números: '))
c = 0
n1 = 0

while n > 0:
	n = int(input('Digite alguns números: '))
	n1 += n
	c += 1
	
print(n1 / (c - 1))

# 3. Leia um número inteiro entre 1000 e 9999 e escreve a sequência invertida. EX: 1000 -> 1 ou 1412 -> 2141

n = int(input('Digite um número entre 1000 e 9999: '))

while n > 9999 or n < 1000:
	n = int(input('Digite um número entre 1000 e 9999: '))

c = 1
m = n // 1000
c = ((n % 1000) // 100) * 10
d = ((n % 100) // 10) * 100
u = (n % 10) * 1000

print(u + d + c + m)



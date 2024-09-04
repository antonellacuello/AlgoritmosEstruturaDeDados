# PROVA DE SEXTA
# 3. Leia um número inteiro e escreva a soma dos números correspondentes a cada dígito do número. EXEMPLOS: 1412 -> 8; 4341220 -> 16; 101 -> 2.

n = int(input('Digite um número: '))
while n < 0:
    n = int(input('Digite um número: '))

soma_digitos = 0

while n > 0:
    digito = n % 10
    soma_digitos += digito
    n = n // 10

print(f'A soma dos dígitos desse número é: {soma_digitos}')

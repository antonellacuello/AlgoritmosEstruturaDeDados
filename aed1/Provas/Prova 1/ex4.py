# 4. Solicite ao usuário um número inteiro e positivo. O programa deve dividir o número sucessivamente por 2 até que o resultado seja MENOR QUE 1. Em cada divisão, deve-se exibir o seu resultado. Quando o resultado for menor que 1, exiba "Chegou a zero!".

n = int(input('Digite um número inteiro e positivo: '))

while n < 0:
	int(input('Digite um número inteiro e POSITIVO: '))
	
while n > 1:
    n = n / 2
    if n >= 1:
        print(n)
print("Chegou a zero!")

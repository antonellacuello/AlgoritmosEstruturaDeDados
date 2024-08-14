# 25. Considere uma sequência de números que atende a todos critérios abaixo: 
#   a - Possui sempre 2 dígitos , nem mais , nem menos . 
#   b - A representação do número possui pelo menos um dígito 1 ou um dígito 2. 
#   c - O número é múltiplo de 3. 
# Faça um programa que implemente e mostre essa sequência. obs: tem que usar repetição para mostrar a sequência. Não pode mostrar os números “na mão”.

c = 10

while c <= 99:
    if c % 3 == 0:
        dezena = c // 10
        unidade = c % 10
        if dezena == 1 or dezena == 2 or unidade == 1 or unidade == 2:
            print(c)
    c += 1

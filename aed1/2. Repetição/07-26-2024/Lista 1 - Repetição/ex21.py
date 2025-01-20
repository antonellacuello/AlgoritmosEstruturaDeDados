#21. Escreva um programa de adivinhação de número. O programa deve conter um número secreto entre 1 e 1.000.000. O usuário deve chutar um número e o programa deve 
# dizer se o número chutado é MAIOR ou MENOR que o número secreto. O usuário deve tentar até acertar o número secreto. O código abaixo mostrar como sortear um 
# número aleatório entre 0 e 10 em python: import random sorteado = random.randint(0,10)

import random
sorteado = random.randint(0,10)
chute = int(input('Digite um número: '))

while chute != sorteado:
  if chute > sorteado:
    print('O número é menor!')
  elif chute < sorteado:
    print('O número é maior!')
  chute = int(input('Digite um número: '))

print('Correto!')

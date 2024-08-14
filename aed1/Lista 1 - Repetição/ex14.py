# Escreva um programa que mostre a seguinte sequência de números para um valor N informado pelo usuário:
'''

   1
   2 2
   3 3 3
   4 4 4 4
   5 5 5 5 5
   …
   N N N N N N N …
   
'''
n = int(input('Digite um número: ')) 
c1 = '' 
c = 0
while c < n:
  c += 1
  c1 = str(c) + ' '
  print(c1 * c)
  
'''N = int(input("Informe o valor de N: "))
i = 1
while i <= N:
    j = 1
    while j <= i:
        print(i, end=" ")
        j += 1
    print()
    i += 1'''

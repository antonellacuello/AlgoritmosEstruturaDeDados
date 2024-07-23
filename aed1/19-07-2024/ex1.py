# Leia um número e escreva seu absoluto

n = int(input('Digite um número:'))
if n >= 0:
  print(f'O absoluto de {n} é {n}!')
else:
  a = n * (-1)
  print(f'O absoluto de {n} é {a}!')

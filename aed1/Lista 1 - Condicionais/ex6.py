# 6. Faça um programa em python que leia 3 números e os mostre em ordem crescente.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))
n3 = int(input('E, por, digite o último número: '))
p = 0
s = 0
t = 0

if n1 > n2 and n1 > n3:
	p = n1
elif n2 > n1 and n2 > n3:
   p = n2
else:
   p = n3
   
if p == n1:
  if n2 > n3:
    s = n2
    t = n3
  else:
    s = n3
    t = n2
elif p == n2:
  if n1 > n3:
    s = n1
    t = n3
  else:
    s = n3
    t = n1
else:
  if n1 > n2:
    s = n1
    t = n2
  else:
    s = n2
    t = n1

print(f'{t}, {s}, {p}')

# Escreva um programa que leia dois valores x e y. Em seguida escreva quais são os números primos contidos neste intervalo. Por exemplo, para x=3 
# e y=14 escreva: 3,5,7,11,13. Verifique se o usuário digitou x e y de modo que x<y.

inicio = 3
fim = 14
num = inicio

while num <= fim:
  teste = 2
  primo = True
  while teste < num and primo:
    resto = num % teste
    if resto == 0:
      primo = False
    teste += 1
  if primo:
    print(num)
  num += 1

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

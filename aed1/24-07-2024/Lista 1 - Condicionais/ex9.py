#9. Crie um programa em Python que leia o rendimento mensal do usuário, qual o modelo de imposto (sem correção/com correção das perdas no governo Bolsonaro) 
# e retorne o quanto ele deve pagar de imposto.

r = float(input('Insira seu rendimento mensal: '))
m = input('Insira o modelo de imposto: ')

if m == 'sem correção':
  if r <= 1903.98:
    print('Isento de imposto.')
  elif r <= 2826.65:
    print('O valor a ser pago referente ao imposto é R$142,80')
  elif r <= 3751.05:
    print('O valor a ser pago referente ao imposto é R$354,80')
  elif r <= 4664.68:
    print('O valor a ser pago referente ao imposto é R$636,13')
  else:
    print('O valor a ser pago referente ao imposto é R$869,36')
elif m == 'com correção integral':
  if r <= 4710.49:
    print('Isento de imposto.')
  elif r <= 6993.20:
    print('O valor a ser pago referente ao imposto é R$353,29')
  elif r <= 9280.19:
    print('O valor a ser pago referente ao imposto é R$877,78')
  elif r <= 11540.53:
    print('O valor a ser pago referente ao imposto é R$1573,80')
  else:
    print('O valor a ser pago referente ao imposto é R$2.150,82')
else:
  if r <= 2500.44:
    print('Isento de imposto.')
  elif r <= 3712.16:
    print('O valor a ser pago referente ao imposto é R$187,54')
  elif r <= 4926.14:
    print('O valor a ser pago referente ao imposto é R$465,95')
  elif r <= 6125.99:
    print('O valor a ser pago referente ao imposto é R$835.41')
  else:
    print('O valor a ser pago referente ao imposto é R$1.141,71')

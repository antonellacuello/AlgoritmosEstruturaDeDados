# Peça para o usuário informar seu nome e a hora do dia. Escreva uma mensagem conforme a hora
nome = input('Digite seu nome: ')
hora = int(input('Atualmente, que horas são? Limite-se apenas aos dois primeiros números: '))

if  hora >= 5 and hora <= 12:
  print(f'Bom dia, {nome}')
if hora >= 13 and hora <= 18:
  print(f'Boa tarde, {nome}')
if hora >= 14 and hora <= 23 or hora == 00:
  print(f'Boa noite, {nome}')
else:
  print(f'Boa madrugada, {nome}!')

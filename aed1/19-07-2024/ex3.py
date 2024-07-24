# Leia o ano que nasceu e escreva se o voto é facultativo ou obrigatório.

ano_nasc = int(input('Insira o ano de nascimento: '))
from datetime import date
ano_atual = date.today().year

idade = ano_atual - ano_nasc

if idade < 16:
  print("Não pode votar")
elif 18 <= idade <= 70:
  print("Voto obrigatório")
else:
  print("Voto facultativo")

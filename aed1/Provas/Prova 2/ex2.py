# PROVA DE SEXTA
# 2. Crie um programa em python que leia uma data de 2024 ou de 2025 e escreva qual o dia da semana correspondete à data. Observe que 2024 é um ano bissexto e que o ano começou 
# em uma segunda-feira. EXEMPLOS: 12/01/2024 -> Sexta; 03/04/2024 -> quarta; 31/03/2025 -> segunda;

ano = int(input('Digite o ano (2024 ou 2025): '))
while ano != 2024 and ano != 2025:
    print('Ano inválido.')
    ano = int(input('Digite o ano (2024 ou 2025): '))

mes = int(input('Digite o mês: '))
while mes < 1 or mes > 12:
    print('Mês inválido.')
    mes = int(input('Digite o mês: '))

dia = int(input('Digite o dia: '))
while dia < 1 or dia > 31:
    print(f'Dia inválido para o mês {mes}.')
    dia = int(input('Digite o dia: '))
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    while dia < 1 or dia > 30:
        print(f'Dia inválido para o mês {mes}.')
        dia = int(input('Digite o dia: '))
if mes == 2 and ano == 2025:
    while dia < 1 or dia > 28:
        print(f'Dia inválido para o mês {mes}.')
        dia = int(input('Digite o dia: '))
else:
    while dia < 1 or dia > 29:
        print(f'Dia inválido para o mês {mes}.')
        dia = int(input('Digite o dia: '))

dias_ate_mes = 0
mes_atual = 1
while mes_atual < mes:
    if mes_atual == 1 or mes_atual == 3 or mes_atual == 5 or mes_atual == 7 or mes_atual == 8 or mes_atual == 10 or mes_atual == 12:
        dias_ate_mes += 31
    elif mes_atual == 2:
        if ano == 2024:
            dias_ate_mes += 29
        else:
            dias_ate_mes += 28
    elif mes_atual == 4 or mes_atual == 6 or mes_atual == 9 or mes_atual == 11:
        dias_ate_mes += 30
    mes_atual += 1

dia_do_ano = dias_ate_mes + dia
if ano == 2024:
    dias_passados = dia_do_ano - 1
else:
    dias_passados = 366 + dia_do_ano - 1 


dia_semana = dias_passados % 7
if dia_semana == 0:
    print(f'O dia da semana correspondente á data {dia:02d}/{mes:02d}/{ano} é: Segunda-feira!')
elif dia_semana == 1:
    print(f'O dia da semana correspondente á data {dia:02d}/{mes:02d}/{ano} é: Terça-feira!')
elif dia_semana == 2:
    print(f'O dia da semana correspondente á data {dia:02d}/{mes:02d}/{ano} é: Quarta-feira!')
elif dia_semana == 3:
    print(f'O dia da semana correspondente á data {dia:02d}/{mes:02d}/{ano} é: Quinta-feira!')
elif dia_semana == 4:
    print(f'O dia da semana correspondente á data {dia:02d}/{mes:02d}/{ano} é: Sexta-feira!')
elif dia_semana == 5:
    print(f'O dia da semana correspondente á data {dia:02d}/{mes:02d}/{ano} é: Sábado!')
else:
    print(f'O dia da semana correspondente á data {dia:02d}/{mes:02d}/{ano} é: Domingo!')

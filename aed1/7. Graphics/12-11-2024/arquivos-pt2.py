with open('nome', 'w') as arq:      # mais usado e não precisa usar o close, var arq fica inacessível fora da estrutura
    arq.write('Hi')
    arq.seek(offset, local)         # move cursor para a posição offset a partir do Local
    arq.seek(local)                 # move cursor para local designado
    arq.seek(0)                     # move o cursor para o ínicio do arquivo
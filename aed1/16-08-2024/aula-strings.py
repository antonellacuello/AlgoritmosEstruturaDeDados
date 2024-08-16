# Aula de Strings, Listas e Dicionários
#1. Strings -> São listas, a ordem importa e o testo pode ser dividido em caracteres.

x = 'Andre Prisco'
y = 'Erdna Rpicos'   
  
x[0]  # 'A'
x[2]  # 'D'
x[-1] # 'O'

len(x) # 12 (número de caracteres)

z = 'Davi'
z[1] = 'u'    # Não funciona, a string é imutável
f = x[0] + 'u' + x[2] + x[3]    # Concatena

nome = x + ' ' + 'Viera'  # 'Davi Vieira'



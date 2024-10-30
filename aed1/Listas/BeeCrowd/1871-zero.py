def zero(soma):
    soma = str(soma)
    saida = ''
    for p in soma:
        if p != '0':
            saida += p
    return saida

entrada = input().split(' ')
n1 = int(entrada[0])
n2 = int(entrada[1])
soma = n1 + n2
print(zero(soma))

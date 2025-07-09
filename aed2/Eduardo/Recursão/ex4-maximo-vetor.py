def maximo(vetor, pos = 0):
    if pos == len(vetor) - 1:
        return vetor[pos]
    max_resto = maximo(vetor, pos + 1)

    if vetor[pos] > max_resto:
        return vetor[pos]
    else:
        return max_resto
    
lista = [4, 7, 1, 9, 3]
print(maximo(lista))
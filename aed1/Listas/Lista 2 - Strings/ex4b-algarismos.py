#printa os elementos unicos
# retorna o indice que esra o elemento, se for -1 é pq não tem na lista
def ondeEsta(item, lista):
    i = 0
    while i < len(lista):
        if item == lista[i]:
            return i
        i += 1
    return (-1)

def qtsUnicos(lista):
    elementos = []
    quantidade = []

    for item in lista:
        if item in elementos:
            indice = ondeEsta(item, elementos) 
            quantidade[indice] += 1
        else:
            elementos.append(item)
            quantidade.append(1)
    #print(elementos, quantidade)
    qts_unicos = 0
    for item in quantidade:
        if item == 1:
            qts_unicos += 1
    return qts_unicos

numeros = [5, 3, 7, 9, 5, 3, 1, 1, 3, 1, 2, 3, 4, 2,4, 6, 3, 7, 9, 5, 3, 6, 6, 7, 1978, 2024, 1000, 2024, 2025]
print(numeros)
print(qtsUnicos(numeros))

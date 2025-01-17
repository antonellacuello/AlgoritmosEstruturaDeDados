# 6 lista de revisão
def somaListas(l1, l2):
    l3 = []
    soma_l1 = 0
    soma_l2 = 0
    soma_l3 = 0
    for numero in l1:
        l3.append(numero)
        soma_l1 += numero 

    for numero in l2:
        l3.append(numero)
        soma_l2 += numero

    for numero in l3:
        soma_l3 += numero
    l3.sort()
    
    ltotal = [l1, l2, l3]
    listas = {"Lista 1": l1, "Soma lista 1": soma_l1, "Lista 2": l2, "Soma lista 2": soma_l2, "Lista 3": l3, "Soma lista 3": soma_l3}
    return listas

r = somaListas([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
print(r)
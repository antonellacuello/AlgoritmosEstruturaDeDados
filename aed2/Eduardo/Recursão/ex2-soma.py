def soma(vetor, indice = 0):
    if indice >= len(vetor):
        return 0
    return (vetor[indice] + soma(vetor, indice + 1))

r =  soma([1, -2, 3, 4])
print(r)

''''
return 0
return (4 + soma(vetor, 4)) = 4 + 0 = 4
return (3 + soma(vetor, 3)) = 3 + 4 = 7
return (-2 + soma(vetor, 2)) = -2 + 7 = 5
return (1 + soma(vetor, 1)) = 1 + 5 = 6
'''
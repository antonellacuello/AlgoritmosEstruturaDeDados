# Implemente uma função recursiva para buscar determinado valor em um vetor ordenado. Se o valor existir no vetor, retorne seu indice. Caso não esteja no vetor, retorne -1.

def buscaBinaria(vetor, valor, inicio, fim):
    if inicio > fim:
        return -1
    
    meio = inicio + (fim - inicio) //2:
    if vetor[meio] == valor:
        return meio
    elif vetor[meio] > valor:
        return buscaBinaria(vetor, valor, inicio, meio - 1)
    else:
        return buscaBinaria(vetor, valor, meio + 1, fim)

# Exemplo de uso:   
v = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
buscaBinaria(v, 21, 0, len(v) - 1)
    
# Tempo de Execução:
'''
T(n) = ⌈        θ(1)            ; n < 1
       |           
       ⌊    θ(1) + T(n / 2)     ; n > 1
'''
# PSEUDO-CÓDIGO 
'''
somaVetor(vetor, tamanho)
se tamanho <- 0:
    retorne 0;
então:
    retorne vetor[tamanho - 1] + somaVetor(vetor, tamanho - 1);

'''
# CÓDIGO EM PYTHON
def somaVetor(vetor):
    if len(vetor) == 0:
        return 0
    return vetor[0] + somaVetor(vetor[1:])

# Exemplo de uso:
numeros = [1, 2, 4] 
resultado = somaVetor(numeros)                                               
print("Soma do vetor: ", resultado)

# Tempo de Execução
'''
T(n) = ⌈ θ(1)           ; n = 0 (caso base) 
       | 
       ⌊ θ(1) + T(n - 1); n >= 1
'''
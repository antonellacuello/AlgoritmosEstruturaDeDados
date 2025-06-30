# Implemente uma função recursiva para calcular o n-ésimo elemento da sequência de fibonacci.
# A seq. fib começa com 0 e 1, e cada número subsequente é a soma dos dois anteriores: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

def fibonacci(enesimo):
    if enesimo == 1:
        return 0
    if enesimo == 2:
        return 1
    return fibonacci(enesimo - 1) + fibonacci(enesimo - 2)

# Exemplo de uso:
enesimo = 10
print(f"O {enesimo}° termo da sequência fibonacci é {fibonacci(enesimo)}.")

# Tempo de Execução:
'''
T(n) = ⌈           θ(1)            ; n = 1 (caso base 1) 
       |           θ(1)            ; n = 2 (caso base 1) 
       ⌊ θ(1) + T(n - 1) + T(n - 2); n > 1
'''
# Exemplo 2 - Fibonnaci é a sucessão de números inteiros que começa com 0 e 1, e onde cada número seguinte é a soma dos dois anteriores. 0, 1, 1, 2, 3, 5, 8, 13

def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2) 

print(fibonnaci(5))
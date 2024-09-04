# PROVA DE SEXTA
# 1. Cada carro tem um desempenho, que é geralmente medido por quantos quilômetros ele pode percorrer com 1 litro de gasolina. Por exemmplo, os carros mais econômicos 
# podem fazer 16 km/l. Escreva um programa em python que leia o desempenho de um carro e um trajeto percorrido em um mês. Escreva o quanto foi gasto em reais, 
# considerando a gasolina R$5,85. EXEMPLOS: desempenho -> 12km/l; trajeto -> 1000km; gasto -> R$487,50.

d = float(input('Digite o desempenho do seu carro em KM/L: '))
t = float(input('Digite o trajeto percorrido no mês: '))
g = 5.85

gasto = (t / d) * g

print(f'O valor total gasto, em reais, neste mês foi R${gasto:.2f}')

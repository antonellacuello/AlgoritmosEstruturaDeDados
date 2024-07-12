# Exercícios da aula 12/07/2024

# 4. Leia a temperatura em graus Celsius e converta para Fahrenheit.

cf = input('Você deseja converter a temperatura de C para F? Responda com SIM ou NAO ')
if cf.lower() in 'sim':
	c = float(input('Insira a temperatura em °C: '))
	f = (c * 9/5) + 32
	print(f'A temperatura em Fahrenheit é {f}°F!')
else:
	f = float(input('Insira a temperatura em °F: '))
	c = (f - 32) * 5 / 9
	print(f'A temperatura em Celsius é {c}°C!')

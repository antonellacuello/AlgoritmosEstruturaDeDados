#8. Faça um programa em python que leia o nome de 4 times de futebol que estão em uma semifinal. Após, leia os gols das duas partidas: time 1 x time 2 e time 3 x time 4. 
# Os times vencedores devem ir para a final. Caso haja empate, deve-se perguntar ao usuário qual time se classificou. Por fim, deve-se ler os gols da final e mostrar 
# qual time foi campeão (se empatar, perguntar quem foi campeão).

t1 = (input('Digite um dos times presentes na semifinal: ')).upper()
t2 = (input('Digite um outro time presente na semifinal: ')).upper()
t3 = (input('Digite um outro time presente na semifinal: ')).upper()
t4 = (input('Digite o último time presente na semifinal: ')).upper()

gt1 = int(input(f'Insira o número de gols realizado pelo {t1}: '))
gt2 = int(input(f'Insira o número de gols realizado pelo {t2}: '))
gt3 = int(input(f'Insira o número de gols realizado pelo {t3}: '))
gt4 = int(input(f'Insira o número de gols realizado pelo {t4}: '))

v1 = ''
v2 = ''
if gt1 == gt2:
  qc = (input('Quem venceu a primeira disputa? ')).upper()
  if qc == t1:
    v1 = t1
  else:
      v1 = t2
elif gt1 > gt2:
  v1 = t1
else:
  v1 = t2

if gt3 == gt4:
  qc = (input('Quem venceu a segunda disputa? ')).upper()
  if t3 == qc:
    v2 = t3
  else:
    v2 = t4
elif gt3 > gt4:
  v2 = t3
else:
  v2 = t4
  
f1 = int(input(f'Insira o número de gols realizado pelo {v1} na final: '))
f2 = int(input(f'Insira o número de gols realizado pelo {v2} na final: '))
vf = ''

if f1 > f2:
  print(f'{v1} foi o campeão!')
else:
  print(f'{v2} foi o campeão!')

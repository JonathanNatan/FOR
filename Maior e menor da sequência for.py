#EXERCICIO 55
peso = 0
menor = float('inf')
for c in range(1, 5):
    player = float(input(f'Digite um peso da {c} pessoa: '))

    if player > peso:
        peso = player

    if player < menor:
        menor = player

print(f'O maior peso é {peso} e o menor é {menor}')

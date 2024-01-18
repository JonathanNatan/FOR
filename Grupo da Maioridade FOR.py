#EXERCICIO 54
maior = 0
menor = 0
for c in range(1, 8):
    player = int(input(f'Digite o ano do nascimento da {c} pessoa: '))
    idade = 2023 - player
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'Existem {maior} pessoas de maior e {menor} pessoas de menor.')

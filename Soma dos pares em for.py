#EXERCICIO 50
soma = 0
for c in range(0, 6):
    player = int(input('Digite um numero: '))
    if player % 2 == 0:
        soma = soma + player
print(soma)
print('fim')
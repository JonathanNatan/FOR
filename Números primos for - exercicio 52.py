#EXERCICIO 52
cont = 0
numero = int(input('Digite um numero: '))
for c in range(1, numero + 1):
    if numero % c == 0:
        cont = cont + 1
        print(f'{c}', end=', ')
print(f'\n O numero {numero} foi divisivel {cont} vezes')
cont = 0
soma = 0
A = 0
B = 0
for c in range(0,501):
    if c % 2 == 1 and c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'todos o numeros {cont}')
print(f'soma = {soma}')
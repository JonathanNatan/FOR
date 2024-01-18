#EXERCICIO 56
soma_idade = 0
maior = 0
mais_velho = ''
mulher = 0
for c in range(1, 5): 
    print(f'///////// {c} PESSOA ////////')
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    soma_idade = soma_idade + idade
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    media_idade = soma_idade / 7

    if idade > maior and sexo == 'M':
        maior = idade
        mais_velho = nome
    
    if sexo == 'F' and idade < 20:
        mulher = mulher + 1

print(f'O mais velhor tem {maior}, o nome dele é {mais_velho}.')
print(f'A media de idade deles sao {media_idade:.2f}')
print(f'São {mulher} mulheres com menos de 20 anos')
player = int(input('Digite um numero para a tabuada: '))
for c in range(0, player + 1):
    multi = player * c
    print(f'{player}  x {c} = {multi}')

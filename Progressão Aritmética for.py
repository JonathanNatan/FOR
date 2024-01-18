# Solicita ao usuário o valor do primeiro termo da progressão aritmética (PA)
pt = int(input('Digite o primeiro termo: '))

# Solicita ao usuário o valor da razão da progressão aritmética (PA)
razao = int(input('Digite a razao: '))

# O loop for cria uma progressão aritmética com base no primeiro termo (pt) e na razão fornecidos.
# Ele imprimirá os primeiros 10 termos da PA.
# O range começa em pt e vai até pt + 10*razao com passos de razao.
for c in range(pt, pt + 10 * razao, razao):
    print(c)

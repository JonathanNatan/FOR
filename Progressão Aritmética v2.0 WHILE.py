#EXERCICIO 61
c = 0  # Inicializa o contador c com o valor 0.
pt = int(input('Digite o primeiro termo: '))  # Solicita ao usuário o primeiro termo da PA e armazena na variável pt.
razao = int(input('Digite a razao: '))  # Solicita ao usuário a razão da PA e armazena na variável razao.
termo = pt
# Inicia um loop while que continua enquanto o contador c for menor que 10.
while c < 10:
    resultado = termo + c * razao  # Calcula o termo atual da PA usando a fórmula.
    print(resultado)  # Imprime o termo atual da PA.
    c = c + 1  # Incrementa o contador c em 1 para a próxima iteração do loop.


# forma guanabara
pt = int(input('pt: '))
razao = int(input('razap: '))
cont = 1
termo = pt
while cont <= 10: #se chegar ate 10 para
    print(termo) # print dos termos da p.a exemplo (0,5,10,15...)
    pt = pt + razao #soma da progressao
    cont = cont + 1 #contador para parar o loop
#EXECICIO 53
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #FORMA UMA LISTA COM CADA PALAVRA DA FRASE
junto = ''.join(palavras) #JUNTAR TUDO EM UMA S
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
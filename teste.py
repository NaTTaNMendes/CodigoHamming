'''caminho = input('Primeiro txt: ')
arquivo = open(caminho, 'r').read()

caminho = input('Segundo txt: ')
arquivo2 = open(caminho, 'r').read()

if (arquivo == arquivo2):
    print('igual')
else:
    print('diferente')'''
def binarioParaInt(lista):

    # inicialize potência com o 2**8 utilizando operações bit a bit
    pot = (1<<7)
    # criar uma acumulador chamado palavra, afinal um grupo de bytes é uma
    # palavra
    word = 0
    # para cada bit da lista l
    for b in lista:
        b = int(b)
        # guarde o valor do bit vezes a sua potência
        word += b * pot
        # reduza a potência pela divisão por dois usando bit a bit
        pot = pot >> 1
    return word

print(binarioParaInt("11111111"))
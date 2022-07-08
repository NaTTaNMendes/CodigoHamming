from functools import reduce

bits = [0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0]

erro = reduce(lambda x, y: x^y, [i for i, bit in enumerate(bits) if bit])

primeiroBit = True
if ((bits[1:].count(1) % 2 == 1) and (bits[0] == 0)) or ((bits[1:].count(1) % 2 == 0) and (bits[0] == 1)):
    primeiroBit = False
    
if (erro != 0 and primeiroBit == True):
    print('Mais de dois erros encontrados')
elif (erro == 0 and primeiroBit == False):
    print('Erro na posicao 0')
else:
    if (erro != 0):
        print('Erro na posição', erro)
    else:
        print('Nenhum erro encontrado')

    
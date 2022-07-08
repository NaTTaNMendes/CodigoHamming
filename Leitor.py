from ntpath import join

def onzeParaHamming(onze):
    hamming = [0] * 16
    ndxh = 3 # indice no hamming
    pot2 = 4 # proxima potencia a ser pulada
    # percorrer o onze e colocar no hamming
    for i in range(0,11):
        if ndxh == pot2: # o indice é pot de 2
            ndxh +=1     # incrementa a posicao 
            pot2 *= 2    # avanca para a proxima potencia
        # aqui ndxh não é pot de 2
        hamming[ndxh] = onze[i]  # atribuir na posicao correta
        ndxh += 1 # avançar

    paridade = 0
    # calcular bits de paridade usando xor
    for i in range(0, 16):
        if hamming[i]: # se a posição possui um 1, então deve entrar 
            paridade = paridade ^ i   # para o xor
    print(f'paridade={paridade}')

    # ir direto para as potencias de dois
    # estrategia: ir lendo o último bit da paridade e ir deslocand
    # a paridade para esquerda
    for i in range(0,4):
        bitp = paridade & 1       # pegar o ultimo bit da paridade
        paridade = paridade >> 1  # deslocar o paridade para esquerda 
                                  # por uma posição
        hamming[2**i] = bitp      # atribuir na posição potencia de 2


    # calcular a paridade do quadro geral
    bitp = 0
    # fazer o xor de todos os 1 do quadro hamming
    for i in range(0,16):
        bitp ^= hamming[i]
    hamming[0] = bitp

    return hamming


def bla():
    from functools import reduce
    import operator as op
    binarioCompleto = []
    x = list("0100111001100001011101000111010001100001011011100000101000001010")
    while len(x) > 0:
        n = [x[0:11]]
        strComErro = bin((reduce(op.xor, [i for i, bit in enumerate(n) if bit])))
        print(strComErro)
        binarioCorreto = list(strComErro[0] + strComErro[2:])
        print(binarioCorreto)
        
        n[1].append(binarioCorreto[3])
        n[2].append(binarioCorreto[2])
        n[4].append(binarioCorreto[1])
        n[8].append(binarioCorreto[0])
        binarioCompleto.append(n)
        binarioCompleto.append("|")
        print(binarioCompleto)
        del x[0:11]
        print(len(x))


from random import randint, seed # funções para gerar valores aleatorios
seed(3) # alterar a semente do gerador
onze = [ randint(0,1) for i in range(0,11) ]
print(onze)

# chamar a função onzeParaHamming
hamming = onzeParaHamming(onze)
print(f'hamming={hamming}')
#print(len(hamming))

n = 6 & 2

  

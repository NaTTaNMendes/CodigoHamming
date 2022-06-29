
from functools import reduce
import operator as op
import numpy as np

def onzeParaHammingSa(onze):
    bitEm16 = ["*"] * 16
    potencias2 = 4
    posicao_Onze = 0
    grupo1, grupo2, grupo3, grupo4 = [], [], [], []
    pariedadeg, pariedadeg1, pariedadeg2, pariedadeg3, pariedadeg4 = 0, 0, 0, 0, 0
    for posicao, i in enumerate(bitEm16):
            if posicao == potencias2:
                potencias2 *= 2
            elif posicao > 2:
                bitEm16[posicao] = onze[posicao_Onze]
                posicao_Onze += 1    
    
    #print(bitEm16)
    for posicaoMatrix, resultado in enumerate(bitEm16):
        posicaoMatrixBin = [int(i) for i in bin(posicaoMatrix) if i != "b"]
        while len(posicaoMatrixBin) < 4:
            posicaoMatrixBin.insert(0, 0)
        if len(posicaoMatrixBin) > 4:
            posicaoMatrixBin.pop(0)
        if posicaoMatrixBin[0]:
            grupo4.append(posicaoMatrix)
        if posicaoMatrixBin[1]:
            grupo3.append(posicaoMatrix)
        if posicaoMatrixBin[2]:
            grupo2.append(posicaoMatrix)
        if posicaoMatrixBin[3]:
            grupo1.append(posicaoMatrix)
    liderG1 = grupo1.pop(0)
    #print(grupo1)
    for posicaoP in grupo1:
        pariedadeg1 = pariedadeg1 ^ int(bitEm16[posicaoP])
        #print(bitEm16[posicaoP])
    bitEm16[liderG1] = pariedadeg1
    #print()

    liderG2 = grupo2.pop(0)
    #print(grupo2)
    for posicaoP in grupo2:
        pariedadeg2 = pariedadeg2 ^ int(bitEm16[posicaoP])
        #print(bitEm16[posicaoP])
    bitEm16[liderG2] = pariedadeg2
    #print()

    liderG3 = grupo3.pop(0)
    #print(grupo3)
    for posicaoP in grupo3:
        pariedadeg3 = pariedadeg3 ^ int(bitEm16[posicaoP])
        #print(bitEm16[posicaoP])    
    bitEm16[liderG3] = pariedadeg3
    #print()

    liderG4 = grupo4.pop(0)
    #print(grupo4)
    for posicaoP in grupo4:
        pariedadeg4 = pariedadeg4 ^ int(bitEm16[posicaoP])
        #print(bitEm16[posicaoP])  
    bitEm16[liderG4] = pariedadeg4
    #print()

    for im, posicaom in enumerate(bitEm16):
        if im == 0:
            continue
        pariedadeg = pariedadeg ^ int(posicaom)
    bitEm16[0] = pariedadeg
    return(bitEm16)
            
    
    """for i, a in enumerate(bitEm16):
        if a == "1" or a == "0":
            #print(i)
            pariedade = pariedade ^ i
            #print(pariedade)
                
    else:
        print(f' Pariedade Sá -> {pariedade}')
        pariedade = bin(pariedade)
        print(f'pariedade Sá bit -> {pariedade}')
        pariedade = pariedade[0] + pariedade[2:]
        #print(pariedade)
    
    
    for i in pariedade:
        if posicaoPariedade != 0:
            bitEm16[posicaoPariedade] = i
            posicaoPariedade = int(posicaoPariedade / 2)
    
"""


def BinarioParaHamming(binarioCompleto):
    binarioCompletoTemp = [i for i in binarioCompleto]
    binarioFinal = ""
    while len(binarioCompletoTemp) >= 11:
        strSemAntErro = binarioCompletoTemp[0:11]
        strComAntErro = onzeParaHammingSa(strSemAntErro)
        #print(strComAntErro)
        strTemp = "".join(str(e) for e in strComAntErro)
        #print(f'string temp -> {strTemp}')
        binarioFinal = binarioFinal + strTemp
        #print(f'binario Final -> {binarioFinal}')
        del(binarioCompletoTemp[0:11])
    if 11 > len(binarioCompletoTemp) > 0:
        strTemp = "".join(str(e) for e in binarioCompletoTemp)
        binarioFinal = binarioFinal + strTemp
   # print(binarioFinal)
    return binarioFinal


def HammingParaBinario(bits):
    erros = []
    grupo = 0
    bitsTemp = "0000000000000000000000"
    bitsLista = [int(i) for i in bits]
    mensagemFinal = ""
    while len(bitsLista) >= 16:
        temp = ""
        grupo += 1
        bitsTemp = bitsLista[0:16]
        print(bitsTemp)
        posicao = (reduce(op.xor, [i for i, bit in enumerate(bitsTemp) if bit]))
        print(posicao)
        if int(posicao):
            bitsTemp[posicao] = int(not bitsTemp[posicao])
            erros.append([grupo, posicao])
        del(bitsTemp[8])
        del(bitsTemp[4])
        del(bitsTemp[2])
        del(bitsTemp[1])
        del(bitsTemp[0])
        temp = "".join(str(i) for i in bitsTemp)
        mensagemFinal = mensagemFinal + temp 
        del(bitsLista[0:16])
        print(bitsLista)
    if len(bitsLista) > 0:
        mensagemFinal = mensagemFinal + "".join([str(i) for i in bitsLista])


    return (mensagemFinal, erros)

x = BinarioParaHamming("01000001011100100110100101100001011001000110111001100101")
x = HammingParaBinario("100001001010101101011001100110101100110101000010100111001100001001111110101100101")

print(len(x))
print(x)

# 100001001010101101011001100110101100110101000010100111001100001001111110101100101
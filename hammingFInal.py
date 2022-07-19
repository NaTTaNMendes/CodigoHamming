""" Trabalho de recuperação de arquivo
O programa tem a finalidade de recuperar um arquivo utilizando o metodo de Hamming,
utilizando interpolação, etc. O programa não tem muita otimização, portanto, o mesmo
demora para arquivos muito grandes.

Autores:
@Celio Ludwig Slomp
@Kaio de Souza Cardoso
@Nattan Mendes Tinonin
@Vitor Gabriel Gonçalves Coelho
"""

import time
from pathlib import Path

def codCelio(caminho, arquivoSaida):
    sufixo = Path(caminho).suffix
    prefixo = Path(caminho).stem
    for i in prefixo:
        for j in bin(ord(i))[2:].zfill(8):
            bits.append(j)
    for i in sufixo:
        for j in bin(ord(i))[2:].zfill(8):
            bits.append(j)
    for i in range(0, 176-len(bits)):
        bits.append('0')
    blocos = []
    tmp = ''
    for i in range(0, 176):
        tmp += bits[i]
        if (len(tmp) == 11):
            blocos.append(tmp)
            tmp = ''
    bits = bits[176:]

    blocoHamming = []                                           # MASCARA DE HAMMING APLICADA EM CADA
    for bloco in blocos:                                        # BLOCO
        mascara = "xxx" + bloco[0] + "x" + bloco[1:4] + "x" + bloco[4:11]
        blocoHamming.append(mascara)

    for index, saida in enumerate(blocoHamming):                # APLICA HAMMING NOS BLOCOS
        lista = list(saida)
        lista[1] = str(criarQ1(saida))
        lista[2] = str(criarQ2(saida))
        lista[4] = str(criarQ3(saida))
        lista[8] = str(criarQ4(saida))
        lista[0] = str(criarQ0("".join(lista)))
        if (lista[3] == '1'):                                  # CASO O USUÁRIO DESEJE APLICAR ERROS EM CADA BLOCO
            lista[3] = '0'
        else:
            lista[3] = '1'
        saida = "".join(lista)
        blocoHamming[index] = saida
    embaralhado = ''                                            # ADICIONA TODOS OS BLOCOS EM UMA STRING
    for bloco in blocoHamming:                                  # UNICA
        embaralhado += ''.join(bloco)
    embaralhado = embaralhador(embaralhado)                     # EMBARALHA OS BITS

    tmp = ''
    for bit in embaralhado:                                     # ESCREVE TODOS OS BITS
        tmp += bit
        if (len(tmp) == 8):
            arquivoSaida.write(binarioParaInt(tmp).to_bytes(1, 'little'))
            tmp = ''

def criarQ1(binario): 
    """Cria o segundo bit de paridade

    Verifica e adiciona o segundo bit de paridade. No quadro abaixo o bit está
    representado por 'X' e os verificados por 'Y'.\n
    [[0, X, 0, Y]\n
     [0, Y, 0, Y]\n
     [0, Y, 0, Y]\n
     [0, Y, 0, Y]]

    Args:
        binario (str): uma string para poder aplicar o hamming.

    Returns:
        integer: retorna bit para colocar na paridade do hamming.
    """
    y = 1
    um = 0
    while (y < 16):
        if (binario[y] != "x"):  
            if (binario[y] == "1"):
                um += 1
        y += 2
    if (um % 2 == 1):
        return 1
    else:
        return 0

def criarQ2(binario):
    """Cria o terceiro bit de paridade

    Verifica e adiciona o terceiro bit de paridade. No quadro abaixo o bit está
    representado por 'X' e os verificados por 'Y'.\n
    [[0, 0, X, Y]\n
     [0, 0, Y, Y]\n
     [0, 0, Y, Y]\n
     [0, 0, Y, Y]]

    Args:
        binario (str): uma string para poder aplicar o hamming.

    Returns:
        integer: retorna bit para colocar na paridade do hamming.
    """
    y = 2
    um = 0
    while (y < 16): 
        if (binario[y] != "x"):  
            if (binario[y] == "1"):
                um += 1
        if (y % 2 == 0):
            y += 1
        else:
            y += 3
    if (um % 2 == 1):
        return 1
    else:
        return 0

def criarQ3(binario):
    """Cria o quarto bit de paridade

    Verifica e adiciona o quarto bit de paridade. No quadro abaixo o bit está
    representado por 'X' e os verificados por 'Y'.\n
    [[0, 0, 0, 0]\n
     [X, Y, Y, Y]\n
     [0, 0, 0, 0]\n
     [Y, Y, Y, Y]]

    Args:
        binario (str): uma string para poder aplicar o hamming.

    Returns:
        integer: retorna bit para colocar na paridade do hamming.
    """
    y = 4
    um = 0
    while (y < 16):
        if (binario[y] != "x"):  
            if (binario[y] == "1"):
                um += 1
        if (y == 7):
            y = 12
        else:
            y += 1
    if (um % 2 == 1):
        return 1
    else:
        return 0

def criarQ4(binario):
    """Cria o quinto bit de paridade

    Verifica e adiciona o quinto bit de paridade. No quadro abaixo o bit está
    representado por 'X' e os verificados por 'Y'.\n
    [[0, 0, 0, 0]\n
     [0, 0, 0, 0]\n
     [X, Y, Y, Y]\n
     [Y, Y, Y, Y]]

    Args:
        binario (str): uma string para poder aplicar o hamming.

    Returns:
        integer: retorna bit para colocar na paridade do hamming.
    """
    y = 8
    um = 0
    while (y < 16):
        if (binario[y] != "x"):
            if (binario[y] == "1"):
                um += 1
        y += 1
    if (um % 2 == 1):
        return 1
    else:
        return 0

def criarQ0(binario):
    """Cria o bit de paridade que verifica todas as linhas e colunas

    Verifica e adiciona o primeiro bit de paridade. No quadro abaixo o bit está
    representado por 'X' e os verificados por 'Y'.\n
    [[X, Y, Y, Y]\n
     [Y, Y, Y, Y]\n
     [Y, Y, Y, Y]\n
     [Y, Y, Y, Y]]

    Args:
        binario (str): uma string para poder aplicar o hamming.

    Returns:
        integer: retorna bit para colocar na paridade do hamming.
    """
    y = 1
    um = 0
    while (y < 16): 
        if (binario[y] == "1"):
            um += 1
        y += 1
    if (um % 2 == 1):
        return 1
    else:
        return 0     

def embaralhador(bits):
    """ O interpolador do código de hamming

    Essa função é responsável por interpolar 16 blocos de 16 bits
    (256 bits com hamming) para fazer com que o hamming consiga corrigir
    mais de 1 erro no codigo.

    Args:
        bits (str): String com os 256 bits.

    Returns:
        saida (str): bloco de 256 bits interpolados.
    """
    saida = ''
    for i in range(16):
        for a in range(16):
            saida = saida + bits[(a * 16) + i]
    return saida

def mensagemErro(mensagem):
    """ Mensagem de erro personalizada

    Uma mensagem simples de erro que é acionada quando o usuário insere alguma
    alternativa ou argumento cujo o código não suporta/aceita.

    Args:
        mensagem (String): A mensagem de erro.

    Returns:
        None
    """
    # Imprime a mensagem contendo o erro.
    print(mensagem)
    time.sleep(0.5)
    print('\n'*130)

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

def escrever(arquivoSaida, saida):
    escrita = []                                        # DIVIDIMOS EM BLOCOS DE 8 BITS
    for bit in saida:                                   # TRANSFORMAMOS EM BYTES
        escrita.append(bit)                             # E GRAVAMOS NO ARQUIVO            
        if (len(escrita) == 8):
            arquivoSaida.write(binarioParaInt(escrita).to_bytes(1, 'little'))
            escrita = []

def alternativaA():
    caminho = 'teste.mp4'
    arquivoEntrada = open(caminho, 'rb')
    arquivoSaida = open('arquivo.bin', 'wb')
    totalBytes = Path(caminho).stat().st_size
    bits = []
    bitsTemp = []

    st = caminho
    binary_converted = ''.join(format(c, 'b').zfill(8) for c in bytearray(st, "utf-8"))
    binary_converted = binary_converted.zfill(176)

    for bit in binary_converted:
        bitsTemp.append(bit)

    binary_converted = ''
    st = str(totalBytes)
    binary_converted = ''.join(format(c, 'b').zfill(8) for c in bytearray(st, "utf-8"))
    binary_converted = binary_converted.zfill(176)

    for bit in binary_converted:
        bitsTemp.append(bit)
    
                                                                        # Coleta o total de bytes do arquivo
    resto = (totalBytes * 8) % 176                                      # e coloca os 0 a esquerda necessários
    if (resto != 0):
        bits.append('1')
        for i in range(175-resto):
            bits.append('0')
        bits = list(reversed(bits))
    else:
        for i in range(175):
            bits.append('0')
        bits.append('1')
    bitsTemp.extend(bits)
    bits = bitsTemp
    while True:
        byte = arquivoEntrada.read(1)

        if (byte == b''):
            break

        for i in byte:                                                  # TRANSFORMA EM BIT
            for j in bin(i)[2:].zfill(8):
                bits.append(j)
        
        if (len(bits) >= 176):                                          # DIVIDE EM BLOCOS DE 11 BITS
            blocos = []
            tmp = ''
            for i in range(0, 176):
                tmp += bits[i]
                if (len(tmp) == 11):
                    blocos.append(tmp)
                    tmp = ''
            bits = bits[176:]

            blocoHamming = []                                           # MASCARA DE HAMMING APLICADA EM CADA
            for bloco in blocos:                                        # BLOCO
                mascara = "xxx" + bloco[0] + "x" + bloco[1:4] + "x" + bloco[4:11]
                blocoHamming.append(mascara)

            for index, saida in enumerate(blocoHamming):                # APLICA HAMMING NOS BLOCOS
                lista = list(saida)
                lista[1] = str(criarQ1(saida))
                lista[2] = str(criarQ2(saida))
                lista[4] = str(criarQ3(saida))
                lista[8] = str(criarQ4(saida))
                lista[0] = str(criarQ0("".join(lista)))
                if (lista[3] == '1'):                                  # CASO O USUÁRIO DESEJE APLICAR ERROS EM CADA BLOCO
                    lista[3] = '0'
                else:
                    lista[3] = '1'
                saida = "".join(lista)
                blocoHamming[index] = saida
            
            embaralhado = ''                                            # ADICIONA TODOS OS BLOCOS EM UMA STRING
            for bloco in blocoHamming:                                  # UNICA
                embaralhado += ''.join(bloco)

            embaralhado = embaralhador(embaralhado)                     # EMBARALHA OS BITS

            tmp = ''
            for bit in embaralhado:                                     # ESCREVE TODOS OS BITS
                tmp += bit
                if (len(tmp) == 8):
                    arquivoSaida.write(binarioParaInt(tmp).to_bytes(1, 'little'))
                    tmp = ''

    arquivoSaida.close()
    arquivoEntrada.close() 

def alternativaB():
    arquivoEntrada = open('arquivo.bin', 'rb')
    arquivoSaida = ""
    totalEsperado = 0
    totalColetado = 0
    caminho = ''
    
    bits = []
    pos = 0
    qtdErro = 0
    qtdCorrigido = 0
    variavelM = True
    pokemon = True
    while True:
        byte = arquivoEntrada.read(1)                           # LE UM BYTE
        if (byte == b''):                                       # SE ACABAR SAI
            break

        for i in byte:                                          # TRANSFORMA EM BIT
            for j in bin(i)[2:].zfill(8):
                bits.append(j)

        if (len(bits) >= 256):                                  # COLETA UM GRUPO E DESEMBARALHA
            desembaralhado = "".join(bits)
            desembaralhado = embaralhador(desembaralhado)
            bits = []
            pos += 1

            blocos = []                                         # DIVIDE O GRUPO EM BLOCOS
            temp = ''
            for i in desembaralhado:
                temp += i
                if (len(temp) == 16):
                    blocos.append(temp)
                    temp = ''

            decodificados = []
            for bloco in blocos:                                # VERIFICA CADA BLOCO        
                posUm = []
                qtdUm = 0

                for posicao, numero in enumerate(bloco):        # COLETA A QTD DE 1 E AS POSICOES DELES                                              
                    if (numero == '1'):
                        posUm.append(posicao)
                    if (numero == '1' and posicao > 0):
                        qtdUm += 1
                
                checkQ0 = True                                  # VERIFICA O BIT DE PARIDADE 0
                if (qtdUm % 2 == 0):
                    if (bloco[0] == '1'):
                        checkQ0 = False
                else:
                    if (bloco[0] == '0'):
                        checkQ0 = False
                
                xor = 0                                         # FAZ O XOR DE TODAS AS POSIÇÕES COM 1
                if (len(posUm) != 0):
                    for item in posUm:
                        xor = xor^item                          
                    
                    if (xor != 0) and (checkQ0 == False):       # VERIFICA E CORRIGE UM ERRO COMUM
                        a = ""
                        for i in range(0, len(bloco)):
                            if i == xor:
                                if bloco[i] == "1":
                                    a += "0"
                                else:
                                    a += "1"
                            else:
                                a += bloco[i]
                        bloco = a
                        qtdErro += 1
                        qtdCorrigido += 1

                    elif (xor != 0) and (checkQ0 == True):      # VERIFICA SE TEM MAIS DE DOIS ERROS
                        qtdErro += 2
                        print('Quantidade de erros:', qtdErro)
                        print('NÃO FOI POSSÍVEL CORRIGIR OS ERROS: 2 OU MAIS BITS CORROMPIDOS EM UM BLOCO OU FORAM ADICIONADOS/REMOVIDOS BYTES')
                        exit()
                  
                    elif not((xor == 0) and checkQ0):           # VERIFICA SE O BIT 0 ESTÁ ERRADO
                        if (bloco[0] == '0'):
                            bloco = bloco[1:]
                            bloco = '1' + bloco
                        else:
                            bloco = bloco[1:]
                            bloco = '0' + bloco
                        qtdErro += 1
                        qtdCorrigido += 1
                
                decodificados.append(bloco)                     # GUARDA O BINÁRIO DECODIFICADO

            saida = ''
            for bloco in decodificados:                         # REMOVE OS BITS DE PARIDADE
                bloco = list(bloco)
                bloco[0] = ''
                bloco[1] = ''
                bloco[2] = ''
                bloco[4] = ''
                bloco[8] = ''
                saida = saida + ''.join(bloco)
            
            if (pos == 1) and (pokemon):
                saida = saida[saida.index('1'):]
                if (len(saida) % 8 != 0):
                    for i in range(8 - (len(saida) % 8)):
                        saida = '0' + saida
                print(saida)

                for i in range(0, len(saida), 8):   
                    temp_data = saida[i:i + 8] 
                    decimal_data = binarioParaInt(temp_data)
                    caminho = caminho + chr(decimal_data)
                print(caminho)
                 
                arquivoSaida = open('c' + caminho, 'wb')
                pokemon = False
            
            if (pos == 2):
                saida = saida[saida.index('1'):]
                if (len(saida) % 8 != 0):
                    for i in range(8 - (len(saida) % 8)):
                        saida = '0' + saida

                str_data =''
                for i in range(0, len(saida), 8):   
                    temp_data = saida[i:i + 8] 
                    decimal_data = binarioParaInt(temp_data)
                    str_data = str_data + chr(decimal_data)

                totalEsperado = int(str_data)

            if (pos == 3) and variavelM:                        # CASO TENHAMOS COLOCADO 0 A ESQUERDA,
                saida = saida[saida.index('1') + 1:]            # ELE REMOVE E COLOCA O SUFICIENTE PARA
                if (len(saida) % 8 != 0):                       # QUE SEJAM MULTIPLOS DE 8
                    saida.zfill(8 - (len(saida) % 8))
                    variavelM = False
            
            escrever(arquivoSaida, saida)
            
    totalColetado = Path(caminho).stat().st_size

    if (totalColetado > totalEsperado):
        print('Arquivo decodifcado, porém foram adicionados bytes')
    elif (totalColetado < totalEsperado):
        print('Arquivo decodifcado, porém foram removidos bytes')

    arquivoEntrada.close()
    arquivoSaida.close()
    print('Quantidade de erros:', qtdErro)
    print('Erros corrigidos:', qtdCorrigido)
    
def main():
    """Função principal do programa

    Essa é a função principal do código, ela pede ao usuário o que
    o mesmo deseja fazer.

    Args:
        None

    Returns:
        None
    """

    alternatives = ['A', 'B']
    # Aqui está as alternativas que o usuário poderá escolher
    while True:                                                                                     
        print('BEM VINDO AO CODIFICADOR E DECODIFICADOR DE HAMMING')
        print('\n'*2)
        print('A - Codificar um arquivo em Hamming')
        print('B - Decodificar um arquivo codificado em Hamming')
        print('\n'*2)
        choice = input('Sua alternativa: ').upper()

        # Aqui verifica se a alternativa que o usuário escolheu existe
        # Caso não exista, será exibido uma mensagem de erro.
        if (choice in alternatives):
            break
        else:
            mensagemErro('Opção inválida')
    
        # Caso o usuario escolha a alternativa 'A', ele vai para o primeiro
        # if, caso ele escolha a alternativa 'B', ele vai para o segundo.
    if (choice == 'A'):
        # Caso o usuario digite 'A', será chamada a função 'alternativaA()'
        alternativaA()

    if (choice == 'B'):
        # Caso o usuario digite 'B', será chamada a função 'alternativaB()'
        alternativaB()

# Método main padrão do Python.
if __name__ == '__main__':
    main()
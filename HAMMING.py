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

def binarioParaInt(lista):
    """Pega um binario e o transforma em inteiro.

    Args:
        lista (list): Lista de numeros.

    Returns:
        word (integer): Valor referente ao binário.
    """
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
    """Escreve um binario no arquivo.

    Args:
        arquivoSaida (file): O arquivo que será escrito.
        saida (str): o binário que será escrito.
    Returns:
        None.
    """
    
    escrita = []
    for bit in saida:
        # É dividido em blocos de 8 bits
        escrita.append(bit)            
        if (len(escrita) == 8):
            # Logo em seguida é escrito dentro do arquivo.
            arquivoSaida.write(binarioParaInt(escrita).to_bytes(1, 'little'))
            escrita = []

def criarCabecalho(string):
    """Cria o cabeçalho do arquivo binario

    Essa função cria o arquivo.bin, coloca coloca o arquivo selecionado
    em binário e o codifica em hamming

    Args:
        string (string): possui o nome, extensão, etc do arquivo.

    Returns:
        bitsTempo (list): os bits do cabeçalho.
    """
    
    bitsTemp = []
    st = string
    binarioConvertido = ''.join(format(c, 'b').zfill(8) for c in bytearray(st, "utf-8"))
    binarioConvertido = '1' + binarioConvertido
    # Caso não preencha os 256 bits, adiciona 0 à esquerda
    binarioConvertido = binarioConvertido.zfill(176)

    # Coloca os bits em uma lista
    for bit in binarioConvertido:
        bitsTemp.append(bit)

    return bitsTemp

def alternativaA():
    """É a parte que codifica o arquivo e passa para arquivo binario

    Args:
        None.
    
    Returns:
        None.
    """
    # Pega o arquivo que será codificado e também passa o arquivo que conterá
    # o binário codificado.
    caminho = 'teste.mp4'
    arquivoEntrada = open(caminho, 'rb')
    arquivoSaida = open('arquivo.bin', 'wb')
    totalBytes = Path(caminho).stat().st_size
    bits = []
    
    # Cria o cabeçalho do arquivo.
    cabecalho = criarCabecalho(caminho)
    cabecalho.extend(criarCabecalho(str(totalBytes)))

    # Verifica quandos bits tem no arquivo, caso nao seja divisivel por 176
    # fica adicionando 0 à esquerda até que o arquivo seja divisivel.
    resto = (totalBytes * 8) % 176
    if (resto != 0):       
        for i in range(175-resto):
            bits.append('0')
        bits.append('1')
    else:
        for i in range(175):
            bits.append('0')
        bits.append('1')

    # Coloca o cabeçalho nos bits
    cabecalho.extend(bits)
    bits = cabecalho

    # Lê cada byte do arquivo
    while True:
        byte = arquivoEntrada.read(1)

        # Para o laço quando acabar os bytes
        if (byte == b''):
            break

        for i in byte:
            # Transforma cada byte em bits com 0 a esquerda caso necessário
            for j in bin(i)[2:].zfill(8):
                bits.append(j)
        
        # separa em blocos de 11 bits
        if (len(bits) >= 176):
            blocos = []
            tmp = ''
            for i in range(0, 176):
                tmp += bits[i]
                if (len(tmp) == 11):
                    blocos.append(tmp)
                    tmp = ''
            bits = bits[176:]

            # Cria uma mascara nos blocos de 11 bits, colocando x onde vai os
            # bits de paridade do hamming
            blocoHamming = []
            for bloco in blocos:
                mascara = "xxx" + bloco[0] + "x" + bloco[1:4] + "x" + bloco[4:11]
                blocoHamming.append(mascara)

            # Coloca o hamming em cada um dos x colocados anteriormente
            for index, saida in enumerate(blocoHamming):
                lista = list(saida)
                lista[1] = str(criarQ1(saida))
                lista[2] = str(criarQ2(saida))
                lista[4] = str(criarQ3(saida))
                lista[8] = str(criarQ4(saida))
                lista[0] = str(criarQ0("".join(lista)))
                #if (lista[3] == '1'):
                #    lista[3] = '0'
                #else:
                #    lista[3] = '1'
                saida = "".join(lista)
                blocoHamming[index] = saida
            
            # Coloca todos os bits em uma string e manda para o embaralhador
            embaralhado = ''
            for bloco in blocoHamming:
                embaralhado += ''.join(bloco)
            embaralhado = embaralhador(embaralhado)

            tmp = ''
            # Escreve todos os bits dentro do arquivo
            for bit in embaralhado:
                tmp += bit
                if (len(tmp) == 8):
                    arquivoSaida.write(binarioParaInt(tmp).to_bytes(1, 'little'))
                    tmp = ''

    # Fecha ps arqiovos
    arquivoSaida.close()
    arquivoEntrada.close() 

def leCabecalho(binario):
    """Le o cabeçalho para o transformar no nome do arquivo

    Args:
        binario (str): A string que está o cabeçalho

    Returns:
        saida (str): O nome do arquivo com a extensão.
    """
    binario = binario[binario.index('1') + 1:]
    saida = ''

    # Pega de byte em byte para conseguir ler o cabeçalho
    for i in range(0, len(binario), 8):
        temp = binario[i:i + 8]
        decimal = binarioParaInt(temp)
        saida = saida + chr(decimal)
    
    return saida

def alternativaB():
    """É a parte que decodifica o arquivo binario e cria o arquivo original

    Args:
        None.
    
    Returns:
        None.
    """
    # Arquivos que serão abertos
    arquivoEntrada = open('arquivo.bin', 'rb')
    arquivoSaida = None
    # Quantidade de bits do arquivo
    totalEsperado = 0
    # Quantidade de bits no cabeçalho
    totalColetado = 0
    
    bits = []
    pos = 0
    qtdErro = 0  
    qtdCorrigido = 0
    abrirSaida = True
    caminho = ''
    
    # Pega byte por byte do arquivo
    while True:
        byte = arquivoEntrada.read(1)
        # Caso acabe os bytes do arquivo, ele para.
        if (byte == b''):
            break
        
        # transforma em bytes
        for i in byte:
            for j in bin(i)[2:].zfill(8):
                bits.append(j)

        # Desembaralha os bits
        if (len(bits) >= 256):
            desembaralhado = "".join(bits)
            desembaralhado = embaralhador(desembaralhado)
            bits = []
            pos += 1

            # Divide em blocos
            blocos = []
            temp = ''
            for i in desembaralhado:
                temp += i
                if (len(temp) == 16):
                    blocos.append(temp)
                    temp = ''

            decodificados = []
            # Verifica cada bloco do arquivo
            for bloco in blocos:   
                posUm = []
                qtdUm = 0

                # Ve quantos 1 que tem no byte
                for posicao, numero in enumerate(bloco):
                    if (numero == '1'):
                        posUm.append(posicao)
                    if (numero == '1' and posicao > 0):
                        qtdUm += 1
                
                # Verifica o bit de paridade 0
                checkQ0 = True
                if (qtdUm % 2 == 0):
                    if (bloco[0] == '1'):
                        checkQ0 = False
                else:
                    if (bloco[0] == '0'):
                        checkQ0 = False
                
                xor = 0
                # Faz o xor nos bytes
                if (len(posUm) != 0):
                    for item in posUm:
                        xor = xor^item                          
                    
                    # Verifica e corrige apenas um erro por bloco
                    if (xor != 0) and (checkQ0 == False):
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

                    # Verifica se o bloco possui mais de dois erros
                    elif (xor != 0) and (checkQ0 == True):
                        qtdErro += 2
                        print('Quantidade de erros:', qtdErro)
                        print('NÃO FOI POSSÍVEL CORRIGIR OS ERROS: 2 OU MAIS BITS CORROMPIDOS EM UM BLOCO OU FORAM ADICIONADOS/REMOVIDOS BYTES')
                        exit()

                    # Verifica se o bit 0 está de acordo com os outros bits e a corrige
                    elif not((xor == 0) and checkQ0):
                        if (bloco[0] == '0'):
                            bloco = bloco[1:]
                            bloco = '1' + bloco
                        else:
                            bloco = bloco[1:]
                            bloco = '0' + bloco
                        qtdErro += 1
                        qtdCorrigido += 1
                
                decodificados.append(bloco)

            saida = ''
            # Tira os bits de paridade
            for bloco in decodificados:
                bloco = list(bloco)
                bloco[0] = ''
                bloco[1] = ''
                bloco[2] = ''
                bloco[4] = ''
                bloco[8] = ''
                saida = saida + ''.join(bloco)

            # pega o primeiro cabeçalho para colocar o nome no arquivo
            if (pos == 1) and (abrirSaida):
                caminho = leCabecalho(saida)
                arquivoSaida = open('c' + caminho, 'wb')
                abrirSaida = False
                saida = ''

            # Pega o segundo cabeçalho para verificar o tamanho do arquivo
            if (pos == 2):
                totalEsperado = leCabecalho(saida)
                totalEsperado = int(totalEsperado)
                saida = ''

            if (pos == 3):
                saida = saida[saida.index('1') + 1:]

            # Escreve no arquivo novo.
            if (saida != ''):                      
                escrever(arquivoSaida, saida)

    # Fecha os arquivos e imprime quantos erros foram achados
    arquivoEntrada.close()
    arquivoSaida.close()
    print('Quantidade de erros:', qtdErro)
    print('Erros corrigidos:', qtdCorrigido)

    totalColetado = Path('c' + caminho).stat().st_size

    # Caso tenha sido adicionado ou removido bits
    if (totalColetado > totalEsperado):
        print('Arquivo decodifcado, porém foram adicionados bytes')
    elif (totalColetado < totalEsperado):
        print('Arquivo decodifcado, porém foram removidos bytes')
    
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
            print("Opção invalida")
            time.sleep(0.5)
            print('\n'*130)
    
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
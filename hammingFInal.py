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
    

def main():
    """Função principal do programa

    Essa é a função principal do código, ela faz tudo.

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
    
    if (choice == 'A'):
        # Caso o usuario escolha a alternativa 'A', ele vem para este 'if'
        # Essa alternativa pega o primeiro arquivo que o usuario digitar
        # e escreve em binario no segundo arquivo que o usuario digitar.
        
        while True:
            # Este while pede o arquivo que será convertido para binario.
            # Caso o usuario digite um arquivo inexistente, será exibido 
            # a mensagem de erro.
            try:
                '''caminho = input('Informe o caminho do arquivo: ')'''      
                # Lê o arquivo em binário                             
                arquivoEntrada = open('teste.py', 'rb')
                break
            except:
                mensagemErro('Arquivo não encontrado')
        
        while True:
            # Este while pede o arquivo que será convertido para binario.
            # Caso o usuario digite um arquivo inexistente, será exibido 
            # a mensagem de erro.
            try:
                '''caminho = input('Informe o caminho onde deseja guardar os binários: ')'''
                arquivoSaida = open('arquivo.bin', 'wb')
                break
            except:
                mensagemErro('Arquivo não encontrado')
        
        bits = []
        embaralhado = ""
        while True:
            # Lê 2 bytes por vez
            bytes = arquivoEntrada.read(1)


            for i in bytes:
                for j in bin(i)[2:].zfill(8):
                    bits.append(j)
            
            if (len(bits) >= 176 or (len(bits) <= 175 and bytes == b'')):
                if len(bits) <= 175:
                    for i in range(0, (176-len(bits))):
                        bits.insert(0, '0')

                blocos = []
                entrada = ''
                for index, i in enumerate(bits):
                    entrada += i
                    if (len(entrada) == 11):
                        blocos.append(entrada)
                        bits = bits[index:]
                
                blocoComHamming = []
                for i in blocos:
                    mascara = "xxx" + i[0] + "x" + i[1:4] + "x" + i[4:11]
                    blocoComHamming.append(mascara) 
            
                # Este for coloca os bits de paridade no lugar certo do codigo (onde estavam os 'x')
                for index, saida in enumerate(blocoComHamming):
                    lista = list(saida)
                    lista[1] = str(criarQ1(saida))
                    lista[2] = str(criarQ2(saida))
                    lista[4] = str(criarQ3(saida))
                    lista[8] = str(criarQ4(saida))
                    lista[0] = str(criarQ0("".join(lista)))
                    saida = "".join(lista)
                    blocoComHamming[index] = saida
                
                for i in blocoComHamming:
                    embaralhado += ''.join(i)

                    '''while True:
                        if (len(embaralhado) == 0):
                            break
                        saida = embaralhado[0:9]
                        embaralhado = embaralhado[9:]
                        saida = binarioParaInt(saida)
                        saida = saida.to_bytes(1, 'little')
                        arquivoSaida.write(saida)

        if (len(bits) > 0):
            bits = ''.join(bits)
            bits = bits.zfill(176)'''
                    if len(embaralhado) >= 256:
                        embaralhado = embaralhador(embaralhado)
                        bit_8 = ''
                        for j in range(1, 257):
                            if j%8 == 0:
                                arquivoSaida.write(binarioParaInt(bit_8).to_bytes(1, 'little'))
                                bit_8 = ''
                            bit_8 += embaralhado[j-1]
                        embaralhado = ""
            if bytes == b'':
            # Quando terminar ele para o while
                break
        arquivoEntrada.close()
        arquivoSaida.close()
        print(bits)
        print(len(bits))

if __name__=='__main__':
    main()
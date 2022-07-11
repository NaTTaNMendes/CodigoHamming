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
    time.sleep(1.5)
    print('\n'*130)

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

def main():
    """Função principal do programa

    Essa é a função principal do código, ela faz tudo.

    Args:
        None

    Returns:
        None
    """
    alternatives = ['A', 'B', 'C']
    # Aqui está as alternativas que o usuário poderá escolher
    while True:                                                                                     
        print('BEM VINDO AO CODIFICADOR E DECODIFICADOR DE HAMMING')
        print('\n'*2)
        print('A - Transformar um arquivo em binário')
        print('B - Codificar um binário em Hamming')
        print('C - Decodificar um binário em Hamming')
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
                caminho = input('Informe o caminho do arquivo: ')      
                # Lê o arquivo em binário                             
                arquivo = open(caminho, 'rb')
                break
            except:
                mensagemErro('Arquivo não encontrado')

        while True:
            # Este while pede o arquivo que será convertido para binario.
            # Caso o usuario digite um arquivo inexistente, será exibido 
            # a mensagem de erro.
            try:
                caminho = input('Informe o caminho do .txt onde deseja guardar os binários: ')
                arquivoSaida = open(caminho, 'w')
                break
            except:
                mensagemErro('Arquivo não encontrado')

        while True:
            # Lê 100 bits por vez
            byte = arquivo.read(100)
            if byte == b'':
                # Quando terminar ele para o while
                break
            inteiro = int.from_bytes(byte, 'little')
            binario = bin(inteiro)
            binario = binario[2:]
            # Escreve no arquivo .txt 
            arquivoSaida.write(binario)                               
        
        print('Arquivos salvos no caminho:', caminho)

    if (choice == 'B'):
        # Caso o usuario escolha a alternativa 'B', ele vem para este 'if'
        qtdZeros = 0
        while True:
            # Este while pede o arquivo em binário que será convertido para hamming.
            # Caso o usuario digite um arquivo inexistente, será exibido 
            # a mensagem de erro.
            try:
                caminho = input('Informe o caminho do arquivo binário a ser codificado: ')
                arquivo = open(caminho, 'r').read()
                arquivo = str(arquivo)
                break
            except:
                mensagemErro('Arquivo não encontrado')
                                                                                                                                                    
        if (len(arquivo) % 11 != 0):
            # Verifica se o binário é múltiplo de 11, caso não seja, o 
            # programa irá ficar adicionando '0' até que o binário 
            # seja multiplo de 11.
            x = 0                                                                                   
            while True:
                #coleta o primeiro multiplo de 11 acima do tamanho do binário        
                if (x > len(arquivo)):
                    break                                                                       
                x += 11
            qtdZeros = x - len(arquivo)                                         
            x = 0                                                                               
            saida = ""                                                                          
            while True:
                #adiciona os 0 para que o binário se torne multiplo de 11               
                if (x == qtdZeros):                                                                
                    break                                                                       
                saida = "0" + saida                                                             
                x += 1
            arquivo = saida + arquivo
        
        # Verifica se o binário é múltiplo de 16, caso não seja, o 
        # programa irá ficar adicionando '0' até que o binário 
        # seja multiplo de 16.    
        zeros = ''                                                              
        tamanho = ((len(arquivo) / 11) * 5) + len(arquivo)
        qtdBlocos = tamanho // 16
        if ((qtdBlocos % 16) != 0):
            resto = qtdBlocos % 16
            resto = int(resto)
            for i in range((16-resto)*11):
                zeros += '0'
            arquivo = zeros + arquivo

        # Coloca 'x' onde serão colocados os bits de paridade, criando uma 'máscara'
        # e divide os bits em blocos de 11
        conjuntos = [] 
        inicio = 0
        fim = 11
                                                                 
        while True: 
            if (fim > len(arquivo)):                                                    
                break
            divisao = arquivo[inicio : fim]
            matriz = "xxx" + divisao[0] + "x" + divisao[1:4] + "x" + divisao[4:11]
            conjuntos.append(matriz)
            inicio = fim
            fim += 11
        
        # Este for coloca os bits de paridade no lugar certo do codigo (onde estavam os 'x')
        for index, saida in enumerate(conjuntos):
            lista = list(saida)
            lista[1] = str(criarQ1(saida))
            lista[2] = str(criarQ2(saida))
            lista[4] = str(criarQ3(saida))
            lista[8] = str(criarQ4(saida))
            lista[0] = str(criarQ0("".join(lista)))
            saida = "".join(lista)
            conjuntos[index] = saida
        
        saida = ''.join(conjuntos)

        while True:
            # Este while pede o arquivo que será convertido para binario.
            # Caso o usuario digite um arquivo inexistente, será exibido 
            # a mensagem de erro.
            try:
                caminho = input('Informe o caminho do .txt onde deseja guardar os binários: ')
                arquivo = open(caminho, 'w')
                break
            except:
                mensagemErro('Arquivo não encontrado')    

        for i in range (0, len(saida), 256):
            # Este for manda para a função embaralhador 256 bits, ou 16
            # conjuntos de 16 bits.
            saidaFinal = embaralhador(saida[i:i+256]) 
            arquivo.write(saidaFinal)
        
        print('Arquivos salvos no caminho:', caminho)                
    
    if (choice == 'C'):
        # Caso o usuario escolha a alternativa 'C', ele vem para este 'if'
        while True:
            # Este while pede o arquivo que será decodificado e salvo em binario.
            # Caso o usuario digite um arquivo inexistende, será exibido 
            # a mensagem de erro.
            try:
                caminho = input('Informe o caminho do arquivo binário a ser decodificado: ')
                arquivo = open(caminho, 'r').read()
                arquivo = str(arquivo)
                break
            except:
                mensagemErro('Arquivo não encontrado')

        # Esse for irá desembaralhar os bits que foram embaralhados para
        # o armazenamento.
        arquivoDesembaralhado = ''                                                                     #Desembaralha
        for i in range (0, len(arquivo), 256):
            try:
                arquivoDesembaralhado += embaralhador(arquivo[i:i+256])
            except:
                # Caso haja adição ou remoção de bits o programa encerra.
                print('ERRO: IMPOSSÍVEL RECUPERAR O ARQUIVO, HOUVE INSERÇÃO OU REMOÇÃO DE BITS')
                exit()

        arquivo = arquivoDesembaralhado

        # Separa todos os bits em blocos de 16 para a verificação
        blocos = []
        bloco = ''
        for bit in arquivo:
            bloco = bloco + bit
            if (len(bloco) == 16):
                blocos.append(bloco)
                bloco = ''
        
        #Verifica todos os bits do arquivo
        decodificados = []
        podeRetornar = True
        for index, bloco in enumerate(blocos):                                                 
            posUm = []
            qtdUm = 0

            #Coleta a posição dos números '1' no bloco de bits
            for posicao, numero in enumerate(bloco):                                                 
                if (numero == '1'):
                    posUm.append(posicao)
                if (numero == '1' and posicao > 0):
                    qtdUm += 1
            
            # Verifica a paridade geral do bloco
            checkQ0 = True
            if (qtdUm % 2 == 0):
                if (bloco[0] == '1'):
                    checkQ0 = False
            else:
                if (bloco[0] == '0'):
                    checkQ0 = False

            xor = 0
            if (len(posUm) != 0):
                for item in posUm:
                    # Realiza o xor dos bits ligados
                    xor = xor^item
                # Esse if é responsável por corrigir o erro (caso haja) no binário
                # do arquivo .txt
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
                    print('ERRO ENCONTRADO NO BLOCO %.0d E NA POSIÇÃO %.0d CORRIGIDO!' % (index, xor))

                # Verifica se ocorreu mais de dois erros
                elif (xor != 0) and (checkQ0 == True):
                    print('MAIS DE DOIS ERROS ENCONTRADOS NO BLOCO %.0d' % (index))
                    podeRetornar = False 

                # Verifica se houve um erro no bit 0                   
                elif not((xor == 0) and checkQ0):
                    if (bloco[0] == '0'):
                        bloco = bloco[1:]
                        bloco = '1' + bloco
                    else:
                        bloco = bloco[1:]
                        bloco = '0' + bloco
                    print('ERRO ENCONTRADO NO BLOCO %.0d E NA POSIÇÃO 0 CORRIGIDO!' % (index))

            # Adiciona os blocos corrigidos em uma lista
            decodificados.append(bloco)

        # Essa parte é responsável por remover o hamming do arquivo, ele 
        # tira os bits de paridade para depois salvá-lo em um arquivo .txt.
        saida = ''
        if (podeRetornar):
            for bloco in decodificados:
                bloco = list(bloco)
                bloco[0] = ''
                bloco[1] = ''
                bloco[2] = ''
                bloco[4] = ''
                bloco[8] = ''
                saida = saida + ''.join(bloco)
            
            saida = saida[saida.index('1'):]
                
            while True:
            # Este while pede o arquivo que será convertido para binario.
            # Caso o usuario digite um arquivo inexistente, será exibido 
            # a mensagem de erro.
                try:
                    caminho = input('Informe o caminho do .txt onde deseja guardar o binário decodificado: ')
                    arquivo = open(caminho, 'w')
                    arquivo.write(saida)
                    print('Arquivos salvos no caminho:', caminho)
                    break
                except:
                    mensagemErro('Arquivo não encontrado')

# Chama a função main() do programa.
if __name__=='__main__':
    main()
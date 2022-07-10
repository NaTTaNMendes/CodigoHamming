import time

def mensagemErro(mensagem): #Informa uma mensagem de erro personalizada
    print(mensagem)
    time.sleep(1.5)
    print('\n'*130)

def criarQ1(binario): #Cria o bit necessário para as colunas 2 e 4  
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

def criarQ2(binario): #Cria o bit necessário para as colunas 3 e 4
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

def criarQ3(binario): #Cria o bit necessário para as linhas 2 e 4
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

def criarQ4(binario): #Cria o bit necessário para as linhas 3 e 4
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

def criarQ0(binario): #Cria o bit necessário para todas as linhas
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
    saida = ''
    for i in range(16):
        for a in range(16):
            saida = saida + bits[(a * 16) + i]
    return saida

def main():
    alternatives = ['A', 'B', 'C']
    
    while True:                                                                                     
        print('BEM VINDO AO CODIFICADOR DE DECODIFICADOR DE HAMMING')
        print('\n'*2)
        print('A - Transformar um arquivo em binário')
        print('B - Codificar um binário em Hamming')
        print('C - Decodificar um binário em Hamming')
        print('\n'*2)
        choice = input('Sua alternativa: ').upper()

        if (choice in alternatives):
            break
        else:
            mensagemErro('Opção inválida')

    if (choice == 'A'):                                                                             
        while True:
            try:
                caminho = input('Informe o caminho do arquivo: ')                                   
                arquivo = open(caminho, 'rb')
                break
            except:
                mensagemErro('Arquivo não encontrado')

        while True:
            try:
                caminho = input('Informe o caminho do .txt onde deseja guardar os binários: ')
                arquivoSaida = open(caminho, 'w')
                break
            except:
                mensagemErro('Arquivo não encontrado')

        while True:
            byte = arquivo.read(100)
            if byte == b'':
                break                                    
            inteiro = int.from_bytes(byte, 'little')
            binario = bin(inteiro)
            binario = binario[2:]  
            arquivoSaida.write(binario)                               
        
        print('Arquivos salvos no caminho:', caminho)

    if (choice == 'B'):
        qtdZeros = 0
        while True:
            try:
                caminho = input('Informe o caminho do arquivo binário a ser codificado: ')
                arquivo = open(caminho, 'r').read()
                arquivo = str(arquivo)
                break
            except:
                mensagemErro('Arquivo não encontrado')
                                                                                                                                                    
        if (len(arquivo) % 11 != 0):                                            #Verifica se o binário é múltiplo de 11
            x = 0                                                                                   
            while True:                                                         #coleta o primeiro multiplo de 11 acima do tamanho do binário        
                if (x > len(arquivo)):
                    break                                                                       
                x += 11
            qtdZeros = x - len(arquivo)                                         
            x = 0                                                                               
            saida = ""                                                                          
            while True:                                                         #adiciona os 0 para que o binário se torne multiplo de 11               
                if (x == qtdZeros):                                                                
                    break                                                                       
                saida = "0" + saida                                                             
                x += 1
            arquivo = saida + arquivo
        
            
        zeros = ''                                                              #Transforma o total de blocos em um múltiplo de 16
        tamanho = ((len(arquivo) / 11) * 5) + len(arquivo)
        qtdBlocos = tamanho // 16
        if ((qtdBlocos % 16) != 0):
            resto = qtdBlocos % 16
            resto = int(resto)
            for i in range((16-resto)*11):
                zeros += '0'
            arquivo = zeros + arquivo

        conjuntos = [] 
        inicio = 0
        fim = 11
                                                                 
        while True: 
            if (fim > len(arquivo)):                                                     #Cria as divisões em grupos de 11 bits e adiciona um 'X' onde deve ser adicionado um bit de paridade
                break
            divisao = arquivo[inicio : fim]
            matriz = "xxx" + divisao[0] + "x" + divisao[1:4] + "x" + divisao[4:11]
            conjuntos.append(matriz)
            inicio = fim
            fim += 11
        
        for index, saida in enumerate(conjuntos):                               # Encaixa os bits de paridade nas posições necessárias    
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
            try:
                caminho = input('Informe o caminho do .txt onde deseja guardar os binários: ')
                arquivo = open(caminho, 'w')
                break
            except:
                mensagemErro('Arquivo não encontrado')    

        for i in range (0, len(saida), 256):
            saidaFinal = embaralhador(saida[i:i+256]) 
            arquivo.write(saidaFinal)
        
        print('Arquivos salvos no caminho:', caminho)                
    
    if (choice == 'C'):
        while True:
            try:
                caminho = input('Informe o caminho do arquivo binário a ser decodificado: ')
                arquivo = open(caminho, 'r').read()
                arquivo = str(arquivo)
                break
            except:
                mensagemErro('Arquivo não encontrado')

        arquivoDesembaralhado = ''                                                                     #Desembaralha
        for i in range (0, len(arquivo), 256):
            try:
                arquivoDesembaralhado += embaralhador(arquivo[i:i+256])
            except:
                print('ERRO: IMPOSSÍVEL RECUPERAR O ARQUIVO, HOUVE INSERÇÃO OU REMOÇÃO DE BITS')
                exit()

        arquivo = arquivoDesembaralhado

        blocos = []                                                                                  #Separa todos os bits em blocos de 16 para a verificação
        bloco = ''
        for bit in arquivo:
            bloco = bloco + bit
            if (len(bloco) == 16):
                blocos.append(bloco)
                bloco = ''
        
        decodificados = []
        podeRetornar = True
        for index, bloco in enumerate(blocos):                                                       #Verifica todos os bits do arquivo
            posUm = []
            qtdUm = 0

            for posicao, numero in enumerate(bloco):                                                 #Coleta a posição dos números '1' no bloco de bits
                if (numero == '1'):
                    posUm.append(posicao)
                if (numero == '1' and posicao > 0):
                    qtdUm += 1
            
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
                    xor = xor^item                                                                  #Realiza o XOR entre os números encontrados
                
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
                elif (xor != 0) and (checkQ0 == True):
                    print('MAIS DE DOIS ERROS ENCONTRADOS NO BLOCO %.0d' % (index))
                    podeRetornar = False 
                                   
                elif not((xor == 0) and checkQ0):
                    if (bloco[0] == '0'):
                        bloco = bloco[1:]
                        bloco = '1' + bloco
                    else:
                        bloco = bloco[1:]
                        bloco = '0' + bloco
                    print('ERRO ENCONTRADO NO BLOCO %.0d E NA POSIÇÃO 0 CORRIGIDO!' % (index))

            decodificados.append(bloco)

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
                try:
                    caminho = input('Informe o caminho do .txt onde deseja guardar o binário decodificado: ')
                    arquivo = open(caminho, 'w')
                    arquivo.write(saida)
                    print('Arquivos salvos no caminho:', caminho)
                    break
                except:
                    mensagemErro('Arquivo não encontrado')
     
if __name__=='__main__':
    main()
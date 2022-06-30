import time

def mensagemErro(mensagem): #Informa uma mensagem de erro personalizada
    print(mensagem)
    time.sleep(1.5)
    print('\n'*130)

def criarQ1(binario): #verifica o bit necessário para as colunas 2 e 4
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

def criarQ2(binario): #verifica o bit necessário para as colunas 3 e 4
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

def criarQ3(binario): #verifica o bit necessário para as linhas 2 e 4
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

def criarQ4(binario): #verifica o bit necessário para as linhas 3 e 4
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

def criarQ0(binario): #verifica o bit necessário para todas as linhas
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

def main():
    alternatives = ['A', 'B', 'C', 'D']
    
    while True:                                                                                     
        print('BEM VINDO AO CODIFICADOR DE DECODIFICADOR DE HAMMING')
        print('\n'*3)
        print('A - Transformar um arquivo em binário')
        print('B - Transformar uma string em binário')
        print('C - Codificar um binário em Hamming (Corrige apenas 1 bit e detecta 2)')
        print('D - Decodificar um binário em Hamming (Corrige apenas 1 bit e detecta 2)')
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
                    arquivo = open(caminho, 'rb').read()                                          
                    arquivo = str(arquivo)                                                                                                                       
                    byteArrayEntrada = bytearray(arquivo, "utf8")                                   
                    saida = ''
                    for byte in byteArrayEntrada:                                                   
                        binario = bin(byte)
                        saida = saida + binario[2:]               
                    break
                except:
                    mensagemErro('Arquivo não encontrado')

            while True:
                try:
                    caminho = input('Informe o caminho do .txt onde deseja guardar os binários: ')
                    arquivo = open(caminho, 'w')
                    arquivo.write(saida)
                    print('Arquivos salvos no caminho:', caminho)
                    break
                except:
                    mensagemErro('Arquivo não encontrado')
                   
    if (choice == 'B'):
        entrada = input('Informe a string para ser convertida: ')
        byteArrayEntrada = bytearray(entrada, "utf8")
        saida = ''

        for byte in byteArrayEntrada:
            binario = bin(byte)
            saida = saida + binario[2:]

        print('String convertida em binário:', saida)

    if (choice == 'C'):
        while True:
            try:
                caminho = input('Informe o caminho do arquivo binário a ser codificado: ')                                   
                arquivo = open(caminho, 'r').read()                                          
                arquivo = str(arquivo)
                print(arquivo)
                break
            except:
                mensagemErro('Arquivo não encontrado')
                                                                                                                                                    
        if (len(arquivo) % 11 != 0):                                            #Verifica se o binário é múltiplo de 11
            x = 0                                                                                   
            while True:                                                         #coleta o primeiro multiplo de 11 acima da do tamanho do binário        
                if (x > len(arquivo)):                                                               
                    break                                                                       
                x += 11                                                                         
            zeros = x - len(arquivo)                                                                                                                                                         
            x = 0                                                                               
            saida = ""                                                                          
            while True:                                                         #adiciona os 0 para que o binário se torne multiplo de 11               
                if (x == zeros):                                                                
                    break                                                                       
                saida = "0" + saida                                                             
                x += 1
            arquivo = saida + arquivo
            
        inicio = 0
        fim = 11
        conjuntos = []                                                          #Cria as divisões em grupos de 11 bits e adiciona um 'X' onde deve ser adicionado um bit de paridade
        while True: 
            if (fim > len(arquivo)):
                break
            divisao = arquivo[inicio : fim]
            matriz = "xxx" + divisao[0] + "x" + divisao[1:4] + "x" + divisao[4:11]
            conjuntos.append(matriz)
            inicio = fim
            fim += 11
        
        for index, saida in enumerate(conjuntos):                               #Encaixa os bits de paridade nas posições necessárias    
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
                arquivo.write(saida)
                print('Arquivos salvos no caminho:', caminho)
                break
            except:
                mensagemErro('Arquivo não encontrado')           
    
   ## if (choice == 'D'):             
if __name__=='__main__':
    main()
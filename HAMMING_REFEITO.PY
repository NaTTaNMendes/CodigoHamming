import time
from math import ceil

def mensagemErro(mensagem):
    """ Mensagem de erro para alternativas inexistentes

    Uma mensagem simples de erro que é acionada quando o usuário insere alguma
    alternativa ou argumento cujo o código não suporta/aceita.

    Args:
        mensagem (String): A mensagem de erro.

    Returns:
        Null
    """
    print(mensagem)
    time.sleep(1.5)
    print('\n'*30)
'''
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
'''
def main():
    alternatives = ['A', 'B']
    
    while True:
        print()                                                                                    
        print('BEM VINDO AO CODIFICADOR DE DECODIFICADOR DE HAMMING')
        print()
        print('A - Codificar arquivo em Hamming')
        print('B - Decodificar Hamming em arquivo')
        print()
        choice = input('Sua alternativa: ').upper()

        if (choice in alternatives):
            break
        else:
            mensagemErro('Opção inválida')
            
    if (choice == 'A'):
        caminho = input('Informe o caminho completo do arquivo: ')              #Lê o arquivo em bytes
        caminhoSaida = input('Informe o caminho completo da saida (com o formato): ')
        arquivo = open(caminho, 'rb')
        arquivoSaida = open(caminhoSaida, 'wb')
        while True:
            byte = arquivo.read(100)
            if byte == b'':
                break
            inteiro = int.from_bytes(byte, 'little')
            binario = bin(inteiro)
            binario = str(binario)
            binario = binario[2:]

            if (len(binario) % 11 != 0):                                        #Verifica se o binário é múltiplo de 11
                x = 0                                                                                   
            while True:                                                         #coleta o primeiro multiplo de 11 acima da do tamanho do binário        
                if (x > len(binario)):
                    break 
                x += 11
            qtdZeros = x - len(binario)
            x = 0
            saida = ""
            while True:                                                         #adiciona os 0 para que o binário se torne multiplo de 11               
                if (x == qtdZeros):
                    break
                saida = "0" + saida                                                             
                x += 1
            binario = saida + binario

            inicio = 0
            fim = 11
            conjuntos = []                                                          #Cria as divisões em grupos de 11 bits e adiciona um 'X' onde deve ser adicionado um bit de paridade
            while True: 
                if (fim > len(binario)):
                    break
                divisao = binario[inicio : fim]
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
                saida = '1' + saida
                conjuntos[index] = saida
                intBinario = int(saida, 2)
                byte = intBinario.to_bytes(3, 'little')
                arquivoSaida.write(byte)   
                
        # Fechar os arquivos
        arquivo.close()
        arquivoSaida.close()

if __name__ == '__main__':
    main()        
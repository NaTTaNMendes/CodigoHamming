import time
from functools import reduce
import operator as op

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

def decodificaHamming(bits):
    erro = reduce(op.xor, [i for i, bit in enumerate(bits) if bit])
   #posicoes = []
   #for index, bit in enumerate(bits):
   #    if bit == 1:
   #        posicoes.append(index)
   #
   #if (len(posicoes) > 0):
   #    erro = posicoes[0]
   #else:
   #    erro = 0

   #for i in range(1, len(posicoes)):
   #    erro = erro ^ posicoes[i]

    primeiroBit = True
    if ((bits[1:].count(1) % 2 == 1) and (bits[0] == 0)) or ((bits[1:].count(1) % 2 == 0) and (bits[0] == 1)):
        primeiroBit = False
        
    if (erro != 0 and primeiroBit == True):
        print('Mais de dois erros encontrados')
        return False                                  # Mais de dois erros
    elif (erro == 0 and primeiroBit == False):        # Erro na posição zero
        if (bits[0] == 1):
            bits[0] = 0
        else:
            bits[0] = 1
    else:
        if (erro != 0):
            if (bits[erro] == 1):
                bits[erro] = 0
            else:
                bits[erro] = 1

    return bits

def bitParaInteiro(bits):
    BlocoHamming = []
    retorno = []
    # fatiar a lista em listas de tamanho 8
    for i in range(0, len(bits), 8):
        BlocoHamming.append(bits[i:i+8])    

    # para cada lista l da lista
    for l in BlocoHamming:
        # inicialize potência com o 2**8 utilizando operações bit a bit
        pot = (1<<7)
        # criar uma acumulador chamado palavra, afinal um grupo de bytes é uma
        # palavra
        word = 0
        # para cada bit da lista l
        for b in l:
            # guarde o valor do bit vezes a sua potência
            word += b * pot
            # reduza a potência pela divisão por dois usando bit a bit
            pot = pot >> 1
        # esse último for faz a conversão binário para decimal
        byte = word.to_bytes(1, 'little')
        retorno.append(byte)
    return retorno

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
        caminho = input('Informe o caminho completo do arquivo: ')
        caminhoSaida = input('Informe o caminho completo da saida (com o formato): ')
        
        bits = []
        arquivo = open(caminho, 'rb')                                                           #Lê o arquivo em bytes
        arquivoSaida = open(caminhoSaida, 'wb')
        
        while True:
            byte = arquivo.read(100)
            
            if byte == b'':
                break
            
            inteiro = int.from_bytes(byte, 'little')
            binario = bin(inteiro)
            binario = binario[2:]
            
            for i in binario:
                bits.append(int(i))
            
            bitComHamming = []
            
            while True:
                if (len(bits) >= 11):
                    bitComHamming.extend(onzeParaHamming(bits[0:11]))
                    bits = bits[11:]
                else:
                    break
                           
            listaBytes = bitParaInteiro(bitComHamming)
            for byte in listaBytes:
                arquivoSaida.write(byte)

        if (len(bits) != 0):
            qtdZeros = 11 - len(bits)
            zeros = [0] * qtdZeros
            bits = [*zeros, *bits]
            bits = onzeParaHamming(bits)
            byte = bitParaInteiro(bits)

            for byte in listaBytes:
                arquivoSaida.write(byte)

        # Fechar os arquivos
        arquivo.close()
        arquivoSaida.close()
    
    if (choice == 'B'):
        caminho = input('Informe o caminho completo do arquivo a ser restaurado: ')
        caminhoSaida = input('Informe o caminho completo da saida (com o formato): ')

        bits = []
        arquivo = open(caminho, 'rb')                                                           #Lê o arquivo em bytes
        arquivoSaida = open(caminhoSaida, 'wb')

        while True:
            byte = arquivo.read(100)
            
            if byte == b'':
                break
            
            inteiro = int.from_bytes(byte, 'little')
            binario = bin(inteiro)
            binario = binario[2:]
            
            for i in binario:
                bits.append(int(i))
            
            bitDecodificado = []
            
            cancelar = False
            while cancelar != True:
                if (len(bits) >= 16):
                    blocoDecodificado = decodificaHamming(bits[0:16])
                    if blocoDecodificado == False:
                        cancelar = True
                        break 
                    bitDecodificado.extend(blocoDecodificado)
                    bits = bits[16:]
                    print(bits)
                else:
                    break
            
            if (cancelar):
                break
                           
            listaBytes = bitParaInteiro(bitDecodificado)
            for byte in listaBytes:
                arquivoSaida.write(byte)

        if (len(bits) != 0):
            qtdZeros = 16 - len(bits)
            zeros = [0] * qtdZeros
            bits = [*zeros, *bits]
            bits = decodificaHamming(bits)
            byte = bitParaInteiro(bits)

            for byte in listaBytes:
                arquivoSaida.write(byte)

        # Fechar os arquivos
        arquivo.close()
        arquivoSaida.close()  

if __name__ == '__main__':
    main()        
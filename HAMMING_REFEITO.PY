import time

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
                        
            #inteiro = int.from_bytes(byte, 'little')
            #binario = bin(inteiro)
            #binario = str(binario)
            #binario = binario[2:]

            #if (len(binario) % 11 != 0):                                        #Verifica se o binário é múltiplo de 11
            #    x = 0                                                                                   
            #while True:                                                         #coleta o primeiro multiplo de 11 acima da do tamanho do binário        
            #    if (x > len(binario)):
            #        break 
            #    x += 11
            #qtdZeros = x - len(binario)
            
            #intBinario = int(saida, 2)
            #byte = intBinario.to_bytes(3, 'little')
            #arquivoSaida.write(byte) 
            break  
                
        # Fechar os arquivos
        arquivo.close()
        arquivoSaida.close()

if __name__ == '__main__':
    main()        
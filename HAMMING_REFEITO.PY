import time

def mensagemErro(mensagem): #Informa uma mensagem de erro personalizada
    print(mensagem)
    time.sleep(1.5)
    print('\n'*130)
    
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
            byte = arquivo.read(1)
            if byte == b'':
                break
            inteiro = int.from_bytes(byte, 'little')

            binario = bin(inteiro)
            binario = str(binario)
            print(binario)
            print(len(binario))
            binario = binario[2:]
            intBinario = int(binario, 2)

            byte = intBinario.to_bytes(1, 'little')
            arquivoSaida.write(byte)
        
        arquivo.close()
        arquivoSaida.close()

if __name__ == '__main__':
    main()        
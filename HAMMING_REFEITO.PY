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
        with open(caminho, 'rb') as arquivo:
            saida = []
            while True:
                byte = arquivo.read(1)
                byte = int.from_bytes(byte, byteorder='little')  
                saida.append(byte)
                if not(byte):
                    break
            print(saida)

if __name__ == '__main__':
    main()        
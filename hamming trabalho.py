import time

def main():
    alternatives = ['A', 'B', 'C', 'D']
    while True:                                                                                     
        print('BEM VINDO AO CODIFICADOR DE DECODIFICADOR DE HAMMING')
        print('\n'*3)
        print('A - Transformar um arquivo em binário')
        print('B - Transformar uma string em binário')
        print('C - Codificar um binário em Hamming')
        print('D - Decodificar um binário em Hamming')
        print('\n'*2)
        choice = input('Sua alternativa: ').upper()

        if (choice in alternatives):
            break
        else:
            print('OPÇÃO INVÁLIDA')
            time.sleep(1.5)
            print('\n'*130)

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
                    print('Arquivo não encontrado')
                    time.sleep(1.5)
                    print('\n'*130)

            while True:
                try:
                    caminho = input('Informe o caminho do .txt onde deseja guardar os binários: ')
                    arquivo = open(caminho, 'w')
                    arquivo.write(saida)
                    print('Arquivos salvos no caminho:', caminho)
                    break
                except:
                    print('Arquivo não encontrado')
                    time.sleep(1.5)
                    print('\n'*130)
                
    
    if (choice == 'B'):
        entrada = input('Informe a string para ser convertida: ')
        byteArrayEntrada = bytearray(entrada, "utf8")
        saida = ''

        for byte in byteArrayEntrada:
            binario = bin(byte)
            saida = saida + binario[2:]

        print('String convertida em binário:', saida)

if __name__=='__main__':
    main()
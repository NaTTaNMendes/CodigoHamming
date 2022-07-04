import time
import mimetypes

def mensagemErro(mensagem): #Informa uma mensagem de erro personalizada
    print(mensagem)
    time.sleep(1.5)
    print('\n'*130)


caminho = input()
arquivo = open(caminho, 'wb')


print(mimetypes.guess_type(caminho, strict=True))

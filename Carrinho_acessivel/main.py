import re
from trajetoriaPronto import trajetoria_
from reconhecimento_voz import *


macarrao = (20,9)
arroz = (38,18)
feijao = (36,28)
carne = (12,46)
ovo = (22,67)
caixa = (80,45)

intro()

def main():
        while True:
            #produtos = reconhecimento()
            #produtos = produtos.split(' ')
            produtos = ['macarrão', 'arroz', 'feijão', 'carne', 'ovo']
            stocks = {
                'macarrão' or 'Macarrão': macarrao,
                'arroz' or 'Arroz': arroz,
                'feijão' or 'Feijão': feijao,
                'carne' or 'Carne': carne,
                'ovo' or 'Ovo': ovo,

            }

            lista_produtos = []
            
            #print out all the keys
            for c in stocks:
                print(c)
            
            #print key n values
            for k, v in stocks.items():
                print("Code : {0}, Value : {1}".format(k, v))
                for i in produtos:
                    if re.search('\\b'+i+'\\b', k, re.IGNORECASE):
                        lista_produtos.append(v)
            if lista_produtos:
                print(lista_produtos)
                trajetoria_(lista_produtos)
                break
            else:
                fim = sem_produtos()
                if fim == False:
                    break
            
if __name__ == '__main__':
    main()
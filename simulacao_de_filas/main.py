'''

Modelagem e Simulação - Simulação de Filas (Menu Principal)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

from menu_tempo import *
from menu_servidor import *
from simulacao_1 import *
from simulacao_2 import *

def main():
 
    print("\nComo será o tempo entre chegadas?")

    tecParam = menuTempo()

    print("\nComo será o tempo de serviço?")

    tsParam = menuTempo()
    
    print("\nQuantos servidores estarão disponíveis para atendimento?")

    if menuServidor():
    
        simulacao1(tecParam, tsParam)

        while True:

            print("\nRealizar simulação novamente?")
            print("\nSim (1)")
            print("Não (2)\n")
    
            op = input()

            if op == '1':

                simulacao1(tecParam, tsParam)
  
            elif op == '2':

                break

            else:
            
                print("\nOpção inválida.")

    else:
    
        simulacao2(tecParam, tsParam)

        while True:

            print("\nRealizar simulação novamente?")
            print("\nSim (1)")
            print("Não (2)\n")
    
            op = input()

            if op == '1':

                simulacao2(tecParam, tsParam)
  
            elif op == '2':

                break

            else:
            
                print("\nOpção inválida.")

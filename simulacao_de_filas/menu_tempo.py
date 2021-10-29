'''

Modelagem e Simulação - Simulação de Filas (Menu dos Tempo de Serviço de Tempo Entre Chegadas)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

from menu_distribuicao import *

def menuTempo():

  param = [] 

  while True:

    print("\nDeterminístico (1)")
    print("Aleatório (2)\n")
    
    op = input()

    if op == '1':

      while True:

        try:

          t = float(input("\nInsira o tempo: "))

          if t > 0:

            break

          else:

            print("\nValor inválido.")

        except ValueError:

          print("\nValor inválido.")
        
      param.append(1)
      param.append(t)
      break
  
    elif op == '2':

      print("\nQual será a distribuição de probabilidade associada a esse tempo?")
      
      param = menuDistribuicao()
      break

    else:

      print("\nOpção inválida.")

  return param

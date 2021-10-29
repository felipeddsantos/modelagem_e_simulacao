'''

Modelagem e Simulação - Simulação de Filas (Menu do Servidor)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

def menuServidor():

  while True:

    print("\n1 Servidor (1)")
    print("2 Servidores (2)\n")
    
    op = input()

    if op == '1':

      servidor = True
      break
      
    elif op == '2':

      servidor = False
      break

    else:

      print("\nOpção inválida.")
      
  return servidor

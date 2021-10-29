'''

Modelagem e Simulação - Simulação de Filas (Menu do Simulador)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

from main import *

print("***Simulação de filas do tipo M/M/S***")
print("\nMenu principal")

while True:

  print("\nIniciar uma simulação (1)")
  print("Sair (2)\n")

  op = input()

  if op == '1':
 
    main()
  
  elif op == '2': 

    break

  else:

    print("\nOpção inválida.")

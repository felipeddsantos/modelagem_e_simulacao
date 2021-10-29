'''

Modelagem e Simulação - Simulação de Filas (Simulação com 2 Servidores)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

from chegada import *
from saida import *
from imagem_2 import *
from estatisticas_2 import *
import numpy as np

def simulacao2(tecParam, tsParam):

  TR = 0
  ES = 0
  TF = 0
  HC = 0
  HS = 999999
  n = 0
  clientes = []
  cFila = 0
  cServidos = 0
  evento = ""
  avanco = ""
  flag = 0
  
  while True:

    try:
      
      nMax = int(input("\nInsira a quantidade de entradas no sistema: "))

      if nMax > 0:
      
        eSistema = np.zeros(nMax)
        eServico = np.zeros(nMax)
        tServico = np.zeros(nMax)
        tFila = np.zeros(nMax)
        tSistema = np.zeros(nMax)

        break

      else:

        print("\nValor inválido.")
      
    except ValueError:

      print("\nValor inválido.")

  while n < nMax:

    if HC < HS:

      TR, ES, TF, HC, HS = chegada(ES, TF, HC, HS, tecParam, tsParam)

      flag += 1
      n += 1
      cAtual = n
      clientes.append(n)
      evento = "Chegada"
      
    else:

      TR, ES, TF, HS = saida(ES, TF, HS, tsParam)
      
      atual = clientes[0]
      
      if TR - eServico[atual - 1] - tServico[atual - 1] == 0:
      
        atual = clientes[0]
        clientes.pop(0)
      
      else:
      
        atual = clientes[1]
        clientes.pop(1)
      
      flag -= 1
      cAtual = atual
      cServidos += 1
      evento = "Saída"
    
    if flag == 1:

      ES = 0
    
    if flag == 2:

      ES = 1
    
    eSistema, eServico, tFila, tServico, tSistema, cFila = atualizar2(n, TR, HS, evento, clientes, cAtual, eSistema, eServico, tFila, tServico, tSistema, cFila)
    
    if flag == 2 or (evento == "Saída" and len(clientes) > 1):
      
        HS = min(eServico[clientes[0] - 1] + tServico[clientes[0] - 1], eServico[clientes[1] - 1] + tServico[clientes[1] - 1])
    
    if HS == 999999 and len(clientes) > 0:
        
        HS = eServico[clientes[0] - 1] + tServico[clientes[0] - 1]
    
    imagem2(TR, flag, TF, HC, HS, clientes, cAtual, evento, tFila, tServico, tSistema)
    
    if n == nMax:

      break

    if avanco != "p":
    
      avanco = input("\nAperte ENTER para obter a próxima imagem ou \"p\" para pular para o fim da simulação...")
   
  print("\nFim da simulação.")

  mostrar2(nMax, HS, tFila, tServico, cFila, cServidos)

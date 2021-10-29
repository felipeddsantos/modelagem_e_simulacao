'''

Modelagem e Simulação - Simulação de Filas (Simulação com 1 Servidor)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

from chegada import *
from saida import *
from imagem_1 import *
from estatisticas_1 import *

def simulacao1(tecParam, tsParam):

  TR = 0
  ES = 0
  TF = 0
  HC = 0
  HS = 999999
  n = 0
  cFila = 0
  cServidos = 0
  clientes = []
  eSistema = []
  eServico = []
  tServico = []
  tFila = []
  tSistema = []
  evento = ""
  avanco = ""
  
  while True:

    try:
      
      nMax = int(input("\nInsira a quantidade de entradas no sistema: "))

      if nMax > 0:

        break

      else:

        print("\nValor inválido.")
      
    except ValueError:

      print("\nValor inválido.")

  while n < nMax:

    if HC < HS:

      TR, ES, TF, HC, HS = chegada(ES, TF, HC, HS, tecParam, tsParam)

      n += 1
      cAtual = n
      clientes.append(n)
      evento = "Chegada"
      
    else:

      TR, ES, TF, HS = saida(ES, TF, HS, tsParam)
      
      cAtual = clientes.pop(0)
      cServidos += 1
      evento = "Saída"
    
    eSistema, eServico, tFila, tServico, tSistema, cFila = atualizar1(n, TR, HS, evento, clientes, cAtual, eSistema, eServico, tFila, tServico, tSistema, cFila)
    
    imagem1(TR, ES, TF, HC, HS, clientes, cAtual, evento, tFila, tServico, tSistema)
    
    if n == nMax:

      break

    if avanco != "p":
    
      avanco = input("\nAperte ENTER para obter a próxima imagem ou \"p\" para pular para o fim da simulação...")
   
  print("\nFim da simulação.")

  mostrar1(nMax, HS, tFila, tServico, cFila, cServidos)

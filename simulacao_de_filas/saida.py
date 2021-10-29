'''

Modelagem e Simulação - Simulação de Filas (Evento de Saída)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

from tempo import *

def saida(ES, TF, HS, tsParam):

  TR = HS

  if TF > 0:

    TF -= 1
    HS += tempo(tsParam)

  else:

    ES = 0
    HS = 999999

  return TR, ES, TF, HS

'''

Modelagem e Simulação - Simulação de Filas (Evento de Chegada)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

from tempo import *

def chegada(ES, TF, HC, HS, tecParam, tsParam):
    
  TR = HC

  if ES == 0:

    ES = 1
    HS = HC + tempo(tsParam)
    
  else:

    TF += 1
    
  HC += tempo(tecParam)

  return TR, ES, TF, HC, HS

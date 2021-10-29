'''

Modelagem e Simulação - Simulação de Filas (Obtenção de Tempos Aleatórios)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

from distribuicoes import *
from mmc import *

def tempo(param): 

  if param[0] == 1:

    return param[1]

  else:  

    if param[1] == 1: 

      return geometrica(param[2])

    elif param[1] == 2:

      return binomial(param[2], param[3])
   
    elif param[1] == 3:

      return poisson(param[2])

    elif param[1] == 4:

      return exponencial(param[2])

    elif param[1] == 5:

      return normal(param[2], param[3])
    
    elif param[1] == 6:

      return mmc(param[2])

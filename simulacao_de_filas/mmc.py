'''

Modelagem e Simulação - Simulação de Filas (Método de Monte-Carlo)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

import numpy as np

def mmc(amostra):

    amostra = amostra.split()
    nAmostra = len(amostra)
 
    for i in range(nAmostra):
    
        amostra[i] = float(amostra[i])

    limites = []
    classes = []

    nClasses = int(round(np.sqrt(nAmostra)))
    intervalo = (max(amostra) - min(amostra)) / nClasses
    prob = np.zeros(nClasses)

    for i in range(nClasses + 1):

        limites.append(min(amostra) + i * intervalo)

    for i in range(nClasses):
    
        classes.append((limites[i] + limites[i + 1]) / 2)

    for i in range(nAmostra):

        aux = []

        for j in range(nClasses):

            aux.append(abs(classes[j] - amostra[i])) 

        prob[aux.index(min(aux))] += 1

    prob = prob / nAmostra
    rand = np.random.choice(classes, 1, p = prob)
    
    return rand[0]

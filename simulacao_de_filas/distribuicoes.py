'''

Modelagem e Simulação - Simulação de Filas (Variáveis Aleatórias)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

from random import random
import numpy as np

def geometrica(p): 

    u = random()
    
    num = np.log(u)
    den = np.log(1 - p)
    
    return int(num / den) + 1

def binomial(n, p):
    
    u = random()
    
    k = 0
    c = p / (1 - p)
    pr = (1 - p) ** n
    f = pr
    
    while True:
    
        if u >= f:
            
            pr *= c * (n - k) / (k + 1)
            f += pr
            k += 1
        
        else:
            
            break
    
    return k

def poisson(lam):
    
    u = random()
    
    k = 0
    p = np.exp(-lam)
    f = p
    
    while True:
    
        if u >= f:
            
            p *= lam / (k + 1)
            f += p
            k += 1
        
        else:
            
            break
    
    return k

def exponencial(lam):

    u = random()

    return -np.log(1 - u) / lam

def normal(mi, sigma):

    u1 = random()
    u2 = random()
    
    x = np.sqrt(-2 * np.log(u1))
    y = np.cos(2 * u2 * np.pi)
    
    return mi + np.sqrt(sigma) * (x * y)

'''

Modelagem e Simulação - Simulação de Filas (Estatísticas com 2 Servidores)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

def atualizar2(n, TR, HS, evento, clientes, cAtual, eSistema, eServico, tFila, tServico, tSistema, cFila):
     
    if evento == "Chegada" and n == 1:  

        eSistema[0] = 0
        eServico[0] = 0
        tFila[0] = 0
        tServico[0] = HS - TR
    
    if evento == "Chegada" and n > 1:

        if len(clientes) == 1 or len(clientes) == 2:

            tServico[cAtual - 1] = HS - TR
            tFila[cAtual - 1] = 0
            eServico[cAtual-1] = TR
        
        else:

            cFila += 1

        eSistema[cAtual - 1] = TR

    if evento == "Saída" and len(clientes) > 1:

        eServico[clientes[1] - 1] = TR
        tFila[clientes[1] - 1]= eServico[clientes[1] - 1] - eSistema[clientes[1] - 1]
        tServico[clientes[1] - 1]= HS - TR
        tSistema[cAtual - 1] = tFila[cAtual - 1] + tServico[cAtual - 1]
    
    if evento == "Saída" and (len(clientes) == 0 or len(clientes) == 1):

        tSistema[cAtual - 1] = tFila[cAtual - 1] + tServico[cAtual - 1]

    return eSistema, eServico, tFila, tServico, tSistema, cFila

def mostrar2(nMax, HS, tFila, tServico, cFila, cServidos):

    tMedioFila = sum(tFila) / len(tFila)
    tMedioServico = sum(tServico) / len(tServico)   

    print("\n***Estatísticas da simulação***")
    print("\nTempo médio de espera na fila:", tMedioFila)    
    print("Tempo médio de serviço:", tMedioServico)    
    print("Tempo médio despendido no sistema:", tMedioFila + tMedioServico)   
    print("Tempo máximo da fila:", max(tFila)) 
    print("Probabilidade de esperar na fila:", cFila / nMax)
    print("Quantidade de entidades servidas:", cServidos)
    print("Quantidade de entidades sem serviço:", nMax - cServidos)

'''

Modelagem e Simulação - Simulação de Filas (Estatísticas com 1 Servidor)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

def atualizar1(n, TR, HS, evento, clientes, cAtual, eSistema, eServico, tFila, tServico, tSistema, cFila):
     
    if evento == "Chegada" and n == 1:  

        eSistema.append(0)
        eServico.append(0)
        tFila.append(0)
        tServico.append(HS - TR)
    
    if evento == "Chegada" and n > 1:

        if len(clientes) == 1:

            tServico.append(HS - TR)
            tFila.append(0)
            eServico.append(TR)
        
        else:

            cFila += 1

        eSistema.append(TR)

    if evento == "Saída" and len(clientes) > 0:

        eServico.append(TR)
        tFila.append(eServico[clientes[0] - 1] - eSistema[clientes[0] - 1])
        tServico.append(HS - TR)
        tSistema.append(tFila[cAtual - 1] + tServico[cAtual - 1])
    
    if evento == "Saída" and len(clientes) == 0:

        tSistema.append(tFila[cAtual - 1] + tServico[cAtual - 1])

    return eSistema, eServico, tFila, tServico, tSistema, cFila

def mostrar1(nMax, HS, tFila, tServico, cFila, cServidos):

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
    print("Probabilidade do servidor estar livre:", 1 - sum(tServico) / HS)

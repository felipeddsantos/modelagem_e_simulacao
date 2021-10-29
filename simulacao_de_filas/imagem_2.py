'''

Modelagem e Simulação - Simulação de Filas (Imagem com 2 Servidores)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

def imagem2(TR, ES, TF, HC, HS, clientes, cAtual, evento, tFila, tServico, tSistema):
    
    cServico = []

    if ES == 0:
 
        situacao = "Livre" 
        cServico.append("Nenhum")
        cFila = []
    
    elif ES == 1:

        situacao = "1 Servidor Ocupado"
        cServico.append(clientes[0])
        cFila = clientes[1:len(clientes)]
    
    else:
    
        situacao = "2 Servidores Ocupados"
        cServico.append(clientes[0])
        cServico.append(clientes[1])
        cFila = clientes[2:len(clientes)]
    
    if HS == 999999:

        hs = "Sem previsão"
    
    else:

        hs = HS

    print("\nTempo atual da simulação:", TR)
    print("Evento:", evento)
    print("Entidade:", cAtual)

    if evento == "Saída":

        print("Tempo despendido da entidade", cAtual, "no sistema:", tSistema[cAtual - 1])

    print("Situação do servidor:", situacao)
    print("Entidade(s) em serviço:", cServico)

    if evento == "Chegada" and (len(clientes) == 1):

        print("Tempo despendido da entidade", cServico[0], "na fila:", tFila[cAtual - 1])
        print("Tempo de serviço da entidade", cServico[0], ":", tServico[cAtual - 1])

    elif (evento == "Saída" and len(clientes) > 1) or (evento == "Chegada" and (len(clientes)==2)):

        print("Tempo despendido da entidade", cServico[1], "na fila:", tFila[clientes[1] - 1])
        print("Tempo de serviço da entidade", cServico[1], ":", tServico[clientes[1] - 1])
    
    print("Tamanho da fila:", TF)
    print("Entidades em fila:", cFila)
    print("Próxima chegada:", HC)
    print("Próxima saída:", hs)

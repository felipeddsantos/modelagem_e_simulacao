'''

Modelagem e Simulação - Simulação de Filas (Imagem com 1 Servidor)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

def imagem1(TR, ES, TF, HC, HS, clientes, cAtual, evento, tFila, tServico, tSistema):

    if ES == 0:
 
        situacao = "Livre" 
        cServico = "Nenhum"
    
    else:

        situacao = "Ocupado"
        cServico = clientes[0]
    
    if HS == 999999:

        hs = "Sem previsão"
    
    else:

        hs = HS
    
    if len(clientes) == 1:

        cFila = []
    
    else: 

        cFila = clientes[1 : len(clientes)]

    print("\nTempo atual da simulação:", TR)
    print("Evento:", evento)
    print("Entidade:", cAtual)

    if evento == "Saída":

        print("Tempo despendido da entidade", cAtual, "no sistema:", tSistema[len(tSistema) - 1])

    print("Situação do servidor:", situacao)
    print("Entidade em serviço:", cServico)

    if (evento == "Chegada" and len(clientes) == 1) or (evento == "Saída" and len(clientes) > 0):

        print("Tempo despendido da entidade", cServico, "na fila:", tFila[len(tFila) - 1])
        print("Tempo de serviço da entidade", cServico, ":", tServico[len(tServico) - 1])
    
    print("Tamanho da fila:", TF)
    print("Entidades em fila:", cFila)
    print("Próxima chegada:", HC)
    print("Próxima saída:", hs)

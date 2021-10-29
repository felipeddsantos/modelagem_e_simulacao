'''

Modelagem e Simulação - Simulação de Filas (Menu de Distribuições)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

def menuDistribuicao():

  param = []
  param.append(2)
 
  while True:

    print("\nDistribuição Geométrica (1)")
    print("Distribuição Binomial (2)")
    print("Distribuição de Poisson (3)")
    print("Distribuição Exponencial (4)")
    print("Distribuição Normal (5)")
    print("Distribuição definida por amostra (6)\n")
    
    op = input()
    
    if op == '1':

      while True:

        try:

          p = float(input("\nInsira o parâmetro p da Distribuição Geométrica: "))

          if p > 0 and p <= 1:
            
            break
          
          else:

            print("\nValor inválido.")

        except ValueError:

          print("\nValor inválido.")

      param.append(1)
      param.append(p)
      break

    elif op == '2':

      while True:

        try:

          n = int(input("\nInsira o parâmetro n da Distribuição Binomial: "))
          p = float(input("Insira o parâmetro p da Distribuição Binomial: "))

          if p >= 0 and p <= 1 and n >= 0:

            break

          else:

            print("\nValor inválido.")

        except ValueError:

          print("\nValor inválido.")

      param.append(2)
      param.append(n)
      param.append(p)
      break

    elif op == '3':

      while True:

        try:

          lam = float(input("\nInsira o parâmetro lambda da Distribuição de Poisson: "))
          
          if lam >= 0:

            break
          
          else:

            print("\nValor inválido.")

        except ValueError:

          print("\nValor inválido.")

      param.append(3)
      param.append(lam)
      break
    
    elif op == '4':

      while True:

        try:

          lam = float(input("\nInsira o parâmetro lambda da Distribuição Exponencial: "))

          if lam > 0:

            break
          
          else:

            print("\nValor inválido.")

        except ValueError:

          print("\nValor inválido.")

      param.append(4)
      param.append(lam)
      break

    elif op == '5':

      while True:

        try:

          mi = float(input("\nInsira o parâmetro mi da Distribuição Normal: "))
          sigma = float(input("Insira o parâmetro sigma da Distribuição Normal: "))

          if sigma >= 0:
            
            break
          
          else:

            print("\nValor inválido.")

        except ValueError:

          print("\nValor inválido.")

      param.append(5)
      param.append(mi)
      param.append(sigma)
      break

    elif op == '6':
      
      amostra = input("\nInsira a amostra: ")
      
      param.append(6)
      param.append(amostra)
      break

    else:

      print("\nOpção inválida.")

  return param

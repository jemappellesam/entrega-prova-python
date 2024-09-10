def calcular_soma_quadrados(Vetor): 
     soma=0
     for n in Vetor:
      soma = soma + n*n
     return soma


def main():
    vetor_A = [1,2,3,4,5,6,7,8,9,10]
    print(calcular_soma_quadrados(vetor_A))
     
main()


notas= []
i = 1
while i <5:
   notas.append(input('Digite a nota '+ str(i)+ ':' ))
   i=i+1

soma=0
for n in notas:
   soma = soma + int(n) 

media = soma/4

if media >= 7:
    print('APROVADO')

else:
     final = input("Digite a nota da prova final: ")

     novaMedia = (soma + int(final))/5
     if(novaMedia >=5):
        print("APROVADO")
     else:
       print("REPROVADO")

cpf = input('digite o cpf')
cpf= cpf.replace('-','').replace('.','')
soma =0
for char in cpf:
    soma= soma+ int(char)

if soma % 2 == 0:
    print('par')
else:
    print('impar')

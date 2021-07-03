"""
Recebendo dados do usuário

input() -> TODOH DADO RECEBIDO VIA INPUT É DO TIPO STRING 

"""
#print("Qual seu nome? ")
nome = input('Qual seu nome? \n') 
#print("Qual sua idade? ")
#tbm ja posso fazer o casting aqui, dessa forma:

#idade = input('Qual sua idade? \n')
idade = int(input('Qual sua idade? \n'))

#Input -> Entrada 
#recebe esse nome 

#saida antiga python 2.x
"""
    print('Seja bem-vindo(a) %s' % nome)
    print('A idade de %s é: %s' % (nome, idade))
"""
#colocasse em parenteses quando temos mais de um parametro


#exemplo de print moderno 
"""
    print('Seja bem-vindo(a) {0} '.format(nome))
    print('O(A) {0} tem {1} anos.'.format(nome, idade))

"""


#exemplo de print mais atual
print(f'\nSeja Bem-vindo {nome}') #esse f na frente é de formatação, como se fosse de format
print(f'O(A) {nome} tem {idade} anos de idade!')



"""
Casting => conversão de um tipo de dado para outro 
    Como estamos usando o input(), e todo dado recebido via input é uma string
    logo podemos transformar as devidas variáveis para o tipo que quisermos.

EXEMPLO:

    int(idade) 

    :  é o tipo que queremos que seja alterado e a variável dentro do
    parenteses
 
"""
print(f'O {nome} nasceu em {2021 - int(idade)}\n')




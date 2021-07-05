"""
Ultilitários Python que auxiliam na programação.

dir-> Apresenta todos os atributos/propriedades e funções/métodos disponíveis 
    para determinado tipo de dados ou variáveis.
        tipo: se eu tenho uma string "Matheus", e der um DIR, ele vai me indicar tudo que 
        eu posso ultilizar, ex: lower, sizeof, isdecimal... Coisas que eu posso fazer com
        essa determinada string.

dir(tipo de dado/variável)

help-> Apresenta a documentação/como ultilizar os atributos/propriedades e funções/métodos disponíveis 
    para determinado tipo de dado ou variável.
        ex: usando a determinada string acima, ai depois que eu escolher o tipo da propriedade que eu quero 
        ultilizar, e eu nao soube muito bem o funcionamento, ou ate mesmo nao saber nada sobre o meto-
        do, só é eu dar um HELP que ele irá me explicar como funciona...

help("Matheus".lower)

"""
print(dir('geek'))
help('Geek'.lower)


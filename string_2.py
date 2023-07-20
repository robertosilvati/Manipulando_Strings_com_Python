nome = "Roberto"
idade = 33
profissao = "programador"
linguagem = "Python"
saldo = 45.358

dados = {"nome": "Roberto", "idade": 28}

print("nome: %s idade: %d" % (nome, idade))

print("nome: {} idade: {}".format(nome, idade))

print("nome: {1} idade: {0}".format(idade, nome))
print("nome: {1} idade: {0} nome: {1} {1}".format(idade, nome))

print("nome: {nome} idade: {idade}".format(nome=nome, idade=idade))
print("nome: {nome} idade: {age} {nome} {nome} {age}".format(age=idade, nome=nome))
print("nome: {nome} idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")

print("=-=-=-=-=-=-=-=-=-=")

print("Metodo old style %")
print("Ola, me chamdo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s," % (nome, idade, profissao, linguagem))
print("metodo format")
print("Olá, me chamdo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
print("ola, me chamdo{3}. Eu tenho {2} anos de idade, trabacom com {1} e estou matriculado no curso de {0}".format(linguagem, profissao, idade, nome))
print("metodo f-string")
print(f"Ola, me chamdo {nome}. Tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}")

print("Formatar strings com f-string")
PI = 3.14159
print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")


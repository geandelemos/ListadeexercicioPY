from Lucro import lucro_liquido_evento
# Exercicio para alunos de administracao e economia
# Evento Gastronomico realizado na faculdade para arrecadar fundos para uma entidade filantrópica
#Lista dos organizadores do evento
lst_organizadores = ['bento','mariana','saulo']
# Fornecedores do evento
dict_fornecedor = {
    0: {'nome': 'Pastel Frito', 'vendas': 3000},
    1: {'nome': 'Massa da Mama', 'vendas': 5000},
    2: {'nome': 'Pizza do Tio', 'vendas': 10000},
    3: {'nome': 'Rodizio Mineiro', 'vendas': 3900},
}
# Clientes que consumiram no evento
list_cliente = ['rafael','douglas','amanda','jorge','jeffri','carol','cristian',
 'leonardo','maria','luana','vanessa','jose','maria','bento','mariana','saulo',
 'glauco','ze','maria']
# Despesas do evento
locacao = 0.10 # 10% das vendas
limpeza = 700
seguranca = 800
outras_despesas = 500

# 1 - Calcular o total de vendas usando o for loop no dict
total_vendas = 0 
for fornecedor in dict_fornecedor.values():
    total_vendas += fornecedor["vendas"]
print(f"total de vendas: {total_vendas}")
       
# Os professores doaram 5000,00, cada professor doou 1000,00
# 2 - Criar um dicionario com o nome e valor
dict_professores={ 
   'Professor 1': 1000,
    'Professor 2': 1000,
    'Professor 3': 1000,
    'Professor 4': 1000,
    'Professor 5': 1000
}  

# 3 - Criar uma lista com os nomes dos professores

lista_professores = list(dict_professores.keys())

# 4 - Adicionar essa lista dos professores na lista de clientes

list_cliente.extend(lista_professores)
print(f'Lista de clientes após adicionar professores: {list_cliente}')


# 5 - Calcular quantas pessoas estiveram e a media de gasto por pessoa

total_pessoas = len(list_cliente)
media_gasto_por_pessoa = total_vendas / total_pessoas
print(f'Número total de pessoas: {total_pessoas}')
print(f'Média de gasto por pessoa: {media_gasto_por_pessoa:.2f}')


# 6 - Encontrar quem foi o 10 consumidor e retire da lista

decimo_consumidor = list_cliente[9]
list_cliente.pop(9)
print(f'10º consumidor era: {decimo_consumidor}')
print(f'Lista de clientes após remoção do 10º consumidor: {list_cliente}')


# 7 - Encontre o nome "bola" inserido incorretamente na lista e retire da lista

if "bola" in list_cliente:
    list_cliente.remove("bola")
print(f'Lista de clientes após verificar "bola": {list_cliente}')

# 8 - Verificar se todos os organizadores estao na lista

organizadores_presentes = all(organizador in list_cliente for organizador in lst_organizadores)
print(f'Todos os organizadores estão na lista? {organizadores_presentes}')


# 9 - Tira-los da lista
for organizador in lst_organizadores:
    while organizador in list_cliente:
        list_cliente.remove(organizador) 
print(list_cliente)


# 10 - fazer uma funçao que calcule o lucro liquido do evento
# entrada dos parametros sao as vendas e as despesas
# criar um pacote e gravar o modulo com essa funcao
# importe o pacote com a funcao
# chame a funcao
# execute o programa
from Lucro import lucro_liquido_evento
total_despesas =  (limpeza + seguranca + outras_despesas) + (total_vendas * locacao)
lucro_liquido_evento(total_vendas,total_despesas)










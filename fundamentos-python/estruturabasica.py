# estruturas básicas

# listas 

list01 = []
list02 = ["hello", "hola", "olá", "hallo"]

print(list02[3])

list01.insert(0, 1)
print(list01[0])

list02.append('bye')
print(list02)

list02.remove("hallo")
print(list02)

list02.sort()
print(list02)

print("size of list2 = " + str(len(list02)))

lists = []
lists.append(list01)
lists.append(list02)
print(lists)

# tuplas - lista imutável depois de criada

x = tuple()
print(x)

y = (1, 2, 3)
y = y + (4,5,6)

print(y)

# conjuntos (set)

newSet = set()
newSet

conjunto1 = {1, 2, 1, 1, 2}
conjunto2 = {j for j in range(10)} # usando apenas o "for j ..." só é criado um laço, mas dessa forma conseguimos armazenar os valores em um conjunto
print(conjunto2)

conjunto2.add(10)
print(conjunto2)

teste = {[1, 2, 3]} # retornará erro, pois listas não podem ser inseridas em conjuntos
print(teste)

idades = [17, 19, 18, 20]
set_idades = set(idades)
print (set_idades)

tupla_conjunto1 = tuple(conjunto1)
print(tupla_conjunto1).add(3) # retornará erro, pois tuplas são imutáveis

# dicionários (dict): armazena pares de valores chave nos quais DEVEM ser objetos imutáveis.

dict = {}
dict2 = { 'a': 1, 'b': 2, 'c': 3}

dict2['b'] = 50
print(dict2['b'])

print(dict2.keys())
print(dict2.values())
print(dict2.items())
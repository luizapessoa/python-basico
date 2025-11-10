# variáveis

widht = 10

first_name = "Maria"

booleanCondition = True

numFloat = 10.4

character = 'M'

# tipos de variaveis 

type_of_widht = type(widht)
print(type_of_widht)

widht_float = float(widht)
print (widht_float)

# operações simples

adicao = widht_float + widht
print(adicao)

subtracao = widht - 3
print(subtracao)

multiplicacao = widht * 5
print(multiplicacao)

divisao = widht / 2
print(divisao)

# condições com if else

x = 10
y = 130

if x*2 == y:
    print ("y é o dobro de x")
elif x**2 == y:
    print("y é o quadrado de x")
else: print("nenhuma condição satisfeita")

# condições com switch

def switch(number):
    return {
        '1': 'janeiro',
        '2': 'fevereiro',
        '3': 'março',
        '4': 'abril',
        '5': 'maio',
        '6': 'junho',
        '7': 'julho',
        '8': 'agosto',
        '9': 'setembro',
        '10': 'outubro',
        '11': 'novembro',
        '12': 'dezembro'
    }.get(number, "mês inválido")

number = input("digite o número do mês do seu aniversário (1-12): ")
print("o mês do seu aniversário é:", switch(number))



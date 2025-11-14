# modulo 1


# crie um programa que receba a idade e diga se a pessoa é criança, adolescente, adulto ou idoso
idade = int(input("insira uma idade e descubra sua faixa etária: "))

if idade < 12:
    print("você é uma criança!")
elif idade >=12 and idade < 18:
    print("você é um adolescente!")
elif idade >= 18 and idade < 60:
    print ("você é um adulto!")
else:
    print("você é um idoso!")

# receba dois números e exiba +, -, *, /, % e ** entre eles
num1 = float(input("insira o primeiro número: "))
num2 = float(input("insira o segundo número: "))

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

def modulo(num1, num2):
    return num1 % num2

def exponenciacao(num1, num2):
    return num1 ** num2

print(
    f"soma = {soma(num1, num2)}\n"
    f"subtração = {subtracao(num1, num2)}\n"
    f"multiplicação = {multiplicacao(num1, num2)}\n"
    f"divisão = {divisao(num1, num2)}\n"
    f"módulo = {modulo(num1, num2)}\n"
    f"exponenciação = {exponenciacao(num1, num2)}"
)

# leia um número e diga se ele é par ou ímpar usando if

par_impar = int(input("insira um numero para saber se é par ou impar: "))
if par_impar % 2 == 0:
    print(par_impar, "é par!")
else: 
    print(par_impar, "é ímpar!")

# escreva um programa que peça uma nota e valide se está entre 0 e 10

nota = int(input("insira uma nota entre 0 e 10: "))
if nota >= 0 and nota <=10:
    print("nota válida!")
else: 
    print("nota inválida!")


# modulo 2

# crie uma função que receba um número e retorne a soma de 1 até esse número

def soma_ate_n(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma
    
num = int(input("insira um número para somar de 1 até ele: "))
print(f"a soma de 1 até {num} é {soma_ate_n(num)}")

# use um loop para imprimir os números de 10 até 0 (contagem regressiva)

for i in range(10, -1, -1):
    print(i)

# faça uma função que receba uma lista de números e retorne apenas os pares

def numeros_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares

lista_exemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("números pares:", numeros_pares(lista_exemplo))

# crie uma função que recebe uma string e retorna quantas vogais ela possui

def contar_vogais(string):
    vogais = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    contador = 0
    
    for letra in string:
        if letra in vogais:
            contador += 1
    
    return contador

frase = input("digite uma frase: ")
print("quantidade de vogais:", contar_vogais(frase))

# módulo 3

# numeros = [1, 2, 3, 4, 5] - crie uma nova lista contendo o dobro de cada valor

numeros = [1, 2, 3, 4, 5]
dobro_numeros = [num * 2 for num in numeros]
print("lista com números em dobro:", dobro_numeros)

# conjunto = {1, 2, 2, 3, 4, 4, 5} - remova elementos duplicados 

conjunto = {1, 2, 2, 3, 4, 4, 5}
conjunto_sem_duplicados = set(conjunto)
print("conjunto sem duplicados: ", conjunto_sem_duplicados)

# 11. crie um dicionário chamado pessoa com: nome, idade, cidade e exiba apenas o nome e idade.

dist = { "nome": "João", "idade": 22, "cidade": "Paulista"}
print(dist["nome"], "-", dist["idade"], "anos")

# crie uma tupla cores = ("vermelho", "azul", "verde") e exiba o 2 elemento

cores = ("vermelho", "azul", "verde")
print("segunda cor: ", cores[1])


# módulo 4

# criar a classe Pessoa com método apresentar() e adicionar o método aniversario() que aumenta a idade em 1

class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

    def aniversario(self):
        self.idade += 1
        print(f"Feliz aniversário, {self.nome}! Agora você tem {self.idade} anos.")


pessoa1 = Pessoa("Maria", 19)
pessoa2 = Pessoa("Jairo", 22)

pessoa1.apresentar()
pessoa2.apresentar()

pessoa1.aniversario()
pessoa2.aniversario()

# criar a classe ContaBancaria com métodos de depósito, saque e saldo

class ContaBancaria:
    def __init__ (self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para saque.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}")

    def exibir_saldo(self):
        print(f"Saldo atual de: R${self.saldo}")

    
conta = ContaBancaria("Ana", 1000)
conta.exibir_saldo()
conta.depositar(500)
conta.sacar(200)

# criar a classe Aluno herdando da classe Pessoa

class PessoaBase:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(PessoaBase):
    def __init__ (self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    
    def exibir_aluno(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}")

aluno1 = Aluno("Carlos", 20, "2023001")
aluno1.exibir_aluno()
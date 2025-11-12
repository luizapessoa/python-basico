# funções

# verificando se os lados formam um triangulo retangulo

def trianguloRetangulo (a, b, c):
    if max(a, b, c) != c:
        tmp = c
        c = max(a, b, c)

        if a == c:
            a = tmp
        else:
            b == c
            b = tmp

    if a**2 + b**2 == c**2:
        print("é um triângulo retângulo")
        return True
    print("não é um triângulo retângulo")
    return False

def main():
        a = input("digite o valor do lado a: ")
        b = input("digite o valor do lado b: ")
        c = input("digite o valor do lado c: ")

        return trianguloRetangulo(int(a), int(b), int(c))

if __name__ == "__main__":
    main()


# determinar se o input é um palindromo

import string

def palindromo (str):
    # cria um conjunto contendo todos os sinais de pontuação
    exclude = set(string.punctuation)
    # remove todos os caracteres de pontuação da string
    str = ''.join(ch for ch in str if ch not in exclude)
    # remove espaços e converte todas as letras para minúsculas
    str = str.replace(" ", "").lower()

    if str == str[::-1]: # verifica se a string é igual inversamente
        return True
    else:
        return False

def main():
  sentencaUsuario = input("insira a sentença para verificar se é um palíndromo: ")
  if palindromo(sentencaUsuario):
      print(sentencaUsuario, "é um palíndromo")
  else:
      print(sentencaUsuario, "não é um palíndromo")

if __name__ == "__main__":
    main()
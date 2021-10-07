#Brincando no meu primeiro programa em Python - Usando uma linha
"""Meu primeiro programa
em Python - Usando mais de uma linha"""

print("Hello world")

nome = input("Qual o seu nome? ") #Semelhante ao scanf em C, mas não precisa usar o print para solicitar e ler
print(f"Seu nome é: {nome}")

numero1 = eval(input("Entre com um número inteiro: "))
mumero1 = numero1 + 1
print(f"A soma é: {numero1}")


def multiplicador(numero):
     a = 4  #A variável a aqui é local
     print(f"Dentro da função, a variável vale: {a}")
     return a * numero


a = 3 #A variával a aqui é global
b = multiplicador(5)
print(f"Fora da função, a variável vale: {a}")
print(f"O valor de b é: {b}")
c = a * b
print(f"O valor de c é: {c}")

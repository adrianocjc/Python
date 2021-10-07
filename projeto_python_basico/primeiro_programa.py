#Meu primeiro programa em Python - Usando uma linha
"""Meu primeiro programa
em Python - Usando mais de uma linha"""

print("Hello world")


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

#Cálculo do IMC

print("Vamos calcular o seu IMC!")
peso = eval(input("Digite seu peso: "))
altura = eval(input("Digite a sua altura: "))
imc = peso/(altura**2)
print(f"O seu IMC é: {imc}")

#Imprimir hora, minutos e segundos
hora = 10
minutos = 20
segundos = 20
print(str(hora) + ' : ' + str(minutos) + ' : ' + str(segundos))

#Utilizando a função format()
print('{} : {} : {}'. format(hora, minutos, segundos))

#Ou
print(f'{hora} : {minutos} : {segundos}')



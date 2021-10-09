def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

numero = eval(input("Qual a posição da série de fibonacci você quer? "))
n = numero
fibonacci = fibo(n)
print(f"O número escolhido é {fibonacci}")

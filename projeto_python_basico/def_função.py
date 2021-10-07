escolha = input("Escolha uma opção de função: 1 ou 2: ")
if escolha == 1:
    def func1(x):
        return x + 1
    s = func1(10)
    print(f"O valor da função 1 é: {s}")

else:
    def func2(x):
        return x + 2
    t = func2(20)
    print(f"O valor da função 2 é: {t}")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("Escolha a operação: ")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

operacao = input("Digite o número da operação: (1/2/3/4)")

if operacao == '1':
    resultado = n1 + n2
    print(f"Soma {resultado}")
elif operacao == '2':
    resultado = n1 - n2
    print(f"Subtração: {resultado}")
elif operacao == '3':
    resultado = n1 * n2
    print(f"Multiplicação: {resultado}")
elif operacao == '4':
    if n2 != 0:
        resultado = n1 / n2
        print(f"Divisão: {resultado}")
    else:
        print("Erro, não é permitido divisão por 0")
else:
    print("Operação invalida")
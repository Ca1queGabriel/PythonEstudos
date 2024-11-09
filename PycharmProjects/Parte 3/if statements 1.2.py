print("Calculadora, bem vindo")
num1= float(input("insira o primeiro número: "))
operador = input("Insira o operador da conta(+,-,*,/): ")
num2= float(input("insira o segundo número: "))
resultado = 0.0

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    resultado = num1 / num2
else:
    print(f"{operador} não é um operador válido")

if resultado != 0:
    print(f"O resultado de sua conta é = {round(resultado,2)}")
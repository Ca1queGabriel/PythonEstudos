import math

def temperaturaconver():
    print("Conversor de temperatura")
    unidade = input("Insira a unidade Celsius ou Fahrenheit(C ou F): ")
    temp = float(input("Insira a temperatura: "))

    if unidade == "C":
        conversao = round((9 * temp)/ 5 + 32, 1)
        print(f"Sua temperatura é {conversao}F°")
    elif unidade == "F":
        conversao = round((temp - 32) * 5 / 9,1)
        print(f"Sua temperatura é {conversao}C°")
    else:
        print(f"A unidade {unidade} não é válida")


def calculadoraimc():
    print("Calculadora de IMC")
    peso = float(input("Insira seu peso: "))
    altura = float(input("Insira sua altura: "))

    IMC = peso / math.pow(altura,2)

    if IMC < 18.5:
        print(f"Seu IMC de {round(IMC,3)} é classificado em Baixo peso")
    elif IMC <= 24.99:
        print(f"Seu IMC de {round(IMC,3)} é classificado em Normal")
    elif IMC <= 29.99:
        print(f"Seu IMC de {round(IMC,3)} é classificado em Sobrepeso")
    else:
        print(f"Seu IMC de {round(IMC,3)} é classificado em Obesidade")

def conversorpeso():
    print("Conversor de peso")
    peso = float(input("Insira o peso: "))
    unidade = input("Quilogramas ou Libras?(Q ou L): ")

    if unidade == "Q":
        conversao = peso * 2.205
        print(f"O seu peso convertido para libras é de {round(conversao,3)}")
    elif unidade == "L":
        conversao = peso / 2.205
        print(f"O seu peso convertido para quilos é de {round(conversao,3)}")
    else:
        print(f"{unidade} não é uma unidade válida")

operacao = input("Insira uma operação que gostaria de executar(conversorpeso, calculadoraimc ou temperaturaconver): ")
if operacao == "conversorpeso":
    conversorpeso()
elif operacao == "calculadoraimc":
    calculadoraimc()
elif operacao == "temperaturaconver":
    temperaturaconver()
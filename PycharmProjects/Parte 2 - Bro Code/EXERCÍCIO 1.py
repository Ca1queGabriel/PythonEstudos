#objetivo, calcular circunferência de um círculo
import math
raio = float(input("Insira o raio do círculo que gostaria de calcular a circunferência: "))
circunferencia = 2 * math.pi * raio
print(f"A circunferência de um círculo com raio de {raio} é: {round(circunferencia, 2)}") #esse 2 dentro do round(resultado, 2) é arredondar o número para 2
# dígitos, então ele não bota todos os bilhares de números, e nem arredonda pra 7, mas sim trás só os primeiros 2 números

# logical operators = evaluate multiple conditions (or, and, not)

def temperatura():
    temp = 25
    is_raining = False

    if temp > 35 or temp < 0 or is_raining:
        print("the outdoor event is cancelled")
    else:
        print("the outdoor event is still scheduled")

def taquente():
    temp = 23
    is_sunny = False

    if temp >= 35 and is_sunny:
        print("Tá quente pra caraio 🥵")
        print("Tá ensolarado ☀️")
    elif temp <= 0 and is_sunny:
        print("Tá frio pra caraio 🥶")
        print("Tá ensolarado ☀️")
    elif temp < 28 and temp > 0 and is_sunny:
        print("Tá Quentinho 🙂")
        print("Tá ensolarado ☀️")
    if temp >= 35 and not is_sunny:
        print("Tá quente pra caraio 🥵")
        print("Tá nublado ☁️️")
    elif temp <= 0 and not is_sunny:
        print("Tá frio pra caraio 🥶")
        print("Tá nublado ☁️️")
    elif temp < 28 and temp > 0 and not is_sunny:
        print("Tá Quentinho 🙂")
        print("Tá nublado ☁️️")

taquente()
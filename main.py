import random

class AdivinaNumero:

    def __init__(self, limite_inferior, limite_superior):
        self.numero_a_adivinar = random.randint(limite_inferior, limite_superior)
        self.intentos = 0

    def adivinar(self, numero):
        self.intentos += 1

        if numero == self.numero_a_adivinar:
            return f"Adivinaste el número en {self.intentos} intentos."
        elif numero < self.numero_a_adivinar:
            return "El número es mayor. Intenta de nuevo."
        else:
            return "El número es menor. Intenta de nuevo."

limite_inferior = 1
limite_superior = 50
juego = AdivinaNumero(limite_inferior, limite_superior)

while True:
    try:
        intento = int(input(f"Ingresa un número entre {limite_inferior} y {limite_superior}: "))
        resultado = juego.adivinar(intento)
        print(resultado)
     
        if resultado.startswith("Adivinaste"):
            break
    except ValueError:
        print("Por favor, ingresa un número válido.")

print("Gracias por jugar Adivina el numero :D")
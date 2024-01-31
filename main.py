class adivina_numero:
    def __init__(self):
        self.numero_a_adivinar = 32     

        intento = int(input("Dame un numero del 1 al 50:   "))

        if intento > self.numero_a_adivinar:
            print("El numero es menor")

        elif intento < self.numero_a_adivinar:
            print("El numero es mayor") 

        else:
            print("ganaste")    

adivina_numero()

        
            


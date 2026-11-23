# Mayor de edad
#El programa debe pedirle al usuario su edad y responder:

#Eres mayor de edad si tiene 18 o más
#Eres menor de edad si tiene menos de 18


try:
    age = int(input("Por favor, ingresa tu edad: "))
except ValueError:
    print("Entrada inválida. Por favor, Debes ingresar un número.")
else:
    if age < 0:   
        print("La edad no puede ser negativa.")
    elif age >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")
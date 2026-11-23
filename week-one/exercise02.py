#Ejercicio 2: FizzBuzz (en ejercicio2.py)
#Imprime los números del 1 al 100, pero:

#en los múltiplos de 3 imprime Fizz
#en los múltiplos de 5 imprime Buzz
#en los múltiplos de 3 y de 5 imprime FizzBuzz

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

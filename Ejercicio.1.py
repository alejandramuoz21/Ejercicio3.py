num = int(input("Introduzca un número"))
multiplicand = 0
while num < 0:
    print("El número introducido no puede ser negativo.")
while multiplicand <= 10:
    Resultado = num * multiplicand
    print (num, "x", multiplicand, "=", Resultado)
    multiplicand += 1
num = int(input("Introduzca un número: "))
while num < 1:
    print("El número introducido no puede ser menor que 1.")
if num == 2:
    print (num)
else:
    for i in range (2 , num):
        esprimo = True
        for j in range(2, i):
             if i % j == 0:
                esprimo = False
        if esprimo is True :
            print (i)
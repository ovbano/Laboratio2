    #Mensaje de bienvenida
print("A continuación se va a convertir un valor en libras a kilos y gramos")
    #Variable de tipo flotante ingresada por teclado
numero1=float(input("Para ello deberá digitar el valor a convertir: "))
    #Procesos del programa
convercionKilos=(numero1/2.205)
convercionGramos=(numero1*454)
    #Resultados del programa
print("La cantidad en kilos es: ",convercionKilos)
print("La cantidad en gramas es: ",convercionGramos)
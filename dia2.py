#• Input de usuario,  Conversión de tipos, Validación básica (isdigit, .lower())

#Input de usuario
numero1 = input("Ingresa un numero para una suma: ")
numero2 = input("Ingresa el segundo numro: ")
nombre = input("Ingresa tu nombre: ")


#Conversión de tipo
#suma = numero1 + numero2 # esto lo que  hara es unir los dos valores, pero no sumandolos ej: numero1 + numero2 : 5 + 9 : 59

suma = int(numero1) + int(numero2)#esto convierte el lo que se ingrese a numeros reales y ya se podria sumar

print( "El total es: ", suma)

#validacion de datos basica 
#isdigit
if numero1.isdigit() and numero2.isdigit(): # valida que lo se esta ingresando por consola es texto
    print("ok, es texto")
else:
    print("no es texto")

#.lower

print(nombre.lower()) # convierte todo en minusculas para una respuesta por input y el usuario coloque: SI, Si o sI sea solo valido: si
                    # de la misma manera se usa .upper para mayuscula 
                    #y casefold para idiomas






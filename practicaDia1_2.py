#Practica de dia 1 y 2
#Ejercicio 1 : saludo personalizado
#pide el nombre personalizado al usuario y saludalo
'''
nombre = input("Escribe tu nombre para iniciar: ")
print("Saludos ",nombre,","," chevere tenerte aqui")

#Ejercicio 2 : pide la edad y muestrala en un mensaje
edad = input("dinos tu edad: ")
print("tienes", edad,"años wuao!! casi piso 3 ")

#Ejercicio 3: Dos números (sin validar aún) Pide dos números y muestra la suma

print("hagamos una suma")
numero1 = input("Ingresa el primer numero (el que quieras): ")
numero2 = input("Ingresa el segundo numero(el que quieras): ")

suma = int(numero1)+int(numero2)
print("la suma es:",suma)

#Ejercicio 4: Validar número Pide un dato y valida si es número con .isdigit()
dato = input("Ingresa numeros: ")

validacion = dato.isdigit()

if validacion == True:
    print("Es un numero")
else:
    print("no es numero")

#Ejercicio 5: Suma con validación Pide dos números y:Si ambos son válidos → suma Si no → muestra error

numero1 = input("Ingresa el primer monto a sumar: ")
numero2 = input("Ingresa el segundo monto a sumar: ")

if numero1.isdigit() and numero2.isdigit():
    suma = int(numero1) + int(numero2)
    print("El numero es valido y la suma es: ", suma)
else:
    print("ERROR, no son numeros")


#Ejercicio 6: Confirmación con .lower()
#Pregunta:
#¿Quieres continuar? (si/no)
#👉 Debe funcionar con:
#SI
#si
#Si
#sI

confirmacion = input("Deseas continuar?" \
"escribe si o no: ")
if confirmacion.lower() == "si":
    print("correcto, continuemos")
elif confirmacion.lower() == "no":
    print("hasta luego")
else:
    print("escribe si o no, nada mas")
    

#Ejercicio 7: Menú simple
#Haz un mini menú:
#1. Saludar
#2. Despedirse
#Si elige 1 → “Hola”
#Si elige 2 → “Adiós”
#Si no → “Opción inválida”

saludo = "Hola"
despedida = "Adios"
nombre = input("Ingresa tu nombre: ")

print("Elige la opcion que mas te acomode\n"
      "1. Saludar\n"
      "2. Despedir")

seleccion = int(input())
if seleccion == 1:
    print(saludo, nombre,"Gusto de tenerte aqui")
elif seleccion == 2:
    print(despedida, nombre, ",Espero tenerte aqui de nuevo")
else:
    print("opcion invalida")
'''
#Ejercicio 8: Número mayor de edad
#Pide edad y:
#Si no es número → error
#Si es número:
#=18 → “Mayor”
#<18 → “Menor”

entrada = input("Ingresa tu edad: ")

if entrada.isdigit():
    edad = int(entrada)

    if edad >= 18:
        print("Mayor")
    else:
        print("menor")
else:
    print("no es numero")

# =========================
# EJERCICIO 1 - AND
# =========================
# Crea dos variables:
# edad = 18
# tiene_licencia = True
#
# Imprime si la persona puede conducir:
# Debe tener 18 o más Y tener licencia
'''
edad = 18
tiene_licencia = False

# Escribe tu condición aquí:
# print(...)
if edad >= 18 and tiene_licencia == True:
    print("puedes conducir")
else:
    print("no puedes conducir")


# =========================
# EJERCICIO 2 - OR
# =========================
# es_fin_de_semana = False
# es_festivo = True
#
# Imprime si puedes descansar:
# Basta con que una de las dos sea True

es_fin_de_semana = True
es_festivo = True

# Escribe tu condición aquí:
# print(...)
if es_festivo or es_fin_de_semana == True:
    print("Puedes descansar")
else:
    print("Anda a trabajar pirobo")

# =========================
# EJERCICIO 3 - NOT
# =========================
# esta_lloviendo = True
#
# Imprime si NO está lloviendo

esta_lloviendo = False
# Escribe tu condición aquí:
# print(...)
if esta_lloviendo is not True:
    print("puedes salir")
else:
    print("quedate en casa")


# =========================
# EJERCICIO 4 - AND (login)
# =========================
# usuario = "admin"
# clave_correcta = True
#
# Permitir acceso solo si:
# usuario es "admin" Y clave_correcta es True

usuario = "adin"
clave_correcta = True

# Escribe tu condición aquí:
# print(...)

if usuario == "admin" and clave_correcta == True:
    print("logueado")
else:
    print("uno de los datos esta mal")

# =========================
# EJERCICIO 5 - RETO
# =========================
# edad = 20
# tiene_permiso_padres = False
#
# Puede entrar a la discoteca si:
# edad >= 18 O tiene permiso de padres

edad = 17
tiene_permiso_padres = True

# Escribe tu condición aquí:
# print(...)
if edad >= 20 or tiene_permiso_padres == True:
    print("ingresa perro")
else:
    print("no puedes, sapo")
    '''
'''

#DIA 4 BUCLE FOR
#1 imprimir los numeros del 1 al 10
for i in range(1,11):
    print(i)

    
#2 Imprimir numero pares del 1 al 20

for i in range(0, 21, 2):
    print(i)


#3 sumar numeros del 1 al 100

suma = 0

for i in range(0, 101):
    suma = i + suma
    print(suma)

# 4 tabla de multiplicar
entrada = (input("Ingresa el numero de la tabla que quieres ver: "))

for i in range(11):
    entrada = int(entrada)
    print(f"{entrada} x {i} = {i * entrada}")

#5 contar vocales en una palabra

entrada = input("Ingresa una palabra para contar las vocales por ti: ")
contador = 0

for i in entrada:
    if i.lower() in "aeiou":
        contador += 1
print(f"La palabra -{entrada}-, tiene {contador} vocales")


#6 invertir una cadena

entrada = input("ingresa un texto para invertirlo: ")
reverse=""

for i in entrada:
    reverse = i + reverse
print(f"{entrada} / {reverse}")


# 7 encontrar el numero mayor en una lista
lista = [5243,65,225,678]
mayor=0

for i in lista:
    if i > mayor:
        mayor = i
print(mayor)

# 8 contar numero negativos y positivos

lista = [-8,-9,-7,6,8,-1,5,6]

contador_negativo = 0
negativos = []

contador_positivo = 0
positivos = []

for i in lista:
    if i < 0:
        negativos.append(i)
        contador_negativo += 1
    else:
        positivos.append(i)
        contador_positivo += 1

print(f"estos son los positivos: {positivos} y hay: {contador_positivo}")
print(f"estos son los negativos {negativos} y hay: {contador_negativo}")
'''

# 9. Generar una lista de cuadrados usando for
lista = input("Ingresa los numeros que quieres hacer al cuadrado separa con una coma ',': ")
numeros = lista.split(",")

listaCuadrado = []

for i in numeros:
    num = int(i)
    listaCuadrado.append(num*num)

print(listaCuadrado)

#10. Recorrer una matriz con bucles anidados

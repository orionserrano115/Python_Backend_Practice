#bucles for y while
#control de flujo break, continue

# bucle for:
'''
#clase range

for i in range(10):
    print(i) #lo que hace el bucle aqui es que con la variable "i" muestra por consola la instruccion range que es hasta 10


se usa para algo repetitivo una n cantidad de veces una a una

for i in range(0,101): # con el for le estamos diciendo que, con la variable i entre en el rango 
    print(i)            # de 0 a 101 y con el print le decimos que lo muestre uno por uno
                        # si agregamos otra coma "," en el rango nos dara la secuncia de 2 en d2 o de 3
                        #depende de la indicacion


for i in range(0,21,2):
    print(i)

for i in range(21,0,-1):# en este caso, estamos que vaya de mayor a menor con el -1, y con -2 iria de  
    print(i)            # 2 en 2
    
texto = "Hola"

for caracter in texto:
    print(caracter)
print("fin del bucle")#en este ejemplo la variable "caracter" entra a la variable "texto" e imprime una a una lo que
                      #contiene

texto = "hola me llamo orion"
texto_invertido = ""

for invertir in texto:
    texto_invertido = invertir + texto_invertido
print(texto_invertido)# en este caso el bucle ingresa con la variable "invertir" a la variable "texto", y guarda el valor del moment
                      #en la variable "texto_invertido" en la segunda vuelta hace lo mismo pero lo concatena con el que ya estaba guardado
                      #anteriormente y al final se muestra al reves
                    

#tabla de multiplicar
entrada = int(input("Que tabla quieres ver: "))
for i in range(11):
    print(entrada , "x" , i , "=" , entrada * i)#este caso permite mostrar las tablas de multiplicar en consola mediante una entrada
                                                # la variable i entra al rango de 0 a 10 y luego ejecuta la indicacion dada en el print
                                                #y lo muestra en consola


#imprimir una lista de nombres
lista = ["Luis, Orion, Dariel"]

for i in lista:
    print("hola", i)
    
#sumar elementos de una lista
lista = [2,3,4,5,6]
suma =0
for i in lista:
    suma = i + suma
    print(suma)
    

#recorre una cadena y cuenta cuantas vocales tiene
frase = input("Ingresa una frase: ")
contador=0

for i in frase:
    if i.lower() in "aeiou":
        contador += 1
print(contador)


#generar una lista de cuadrados
cuadrados = []
for i in range(0,11):
    cuadrados.append(i**2)
print(cuadrados)
'''


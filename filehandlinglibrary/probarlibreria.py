from libreria import *

#Variables de prueba para utilizar en los métodos
matriz=[]
matriznumerica=[1,2,9,4,8,3,9]
empleados=[]
varinsercion="manolo"
sobreescribir="pepe"
file="prueba1.txt"
hombrearray=[]
mujerarray=[]
"""
Descomenta los que quieras para usarlos:


añadirAFichero(file, varinsercion)
leerContenidoFichero(file)
leerNumerodeCaracteres(file,10)
leerLineaporLinea(file)

sobreescribirEnFichero(file, sobreescribir )

leerLineaporLinea(file)

añadirAFicheroConSaltos(file,varinsercion)

leerLineasConcretas(file, 2)

leerLineasImPares(file) 
leerLineasPares(file)


contenidodeFicheroaMatriz(file, matriz)

for i in matriz:
    matriz.sort(reverse=True)
print(str(matriz))

print(algoritmoburbuja(matriznumerica))



contenidodeFicheroaMatriz(file, matriz)
print(matriz)
print(algoritmoburbuja(matriz))
"""


hombres="hombres.txt"
mujeres="mujeres.txt"
union="empleados.txt"

crearEmpleados(hombrearray, mujerarray)
insertarEmpleados(hombrearray, mujerarray)

print("---HOMBRES---")
leerLineaporLinea(hombres)
print("----------------")
print("---MUJERES---")
leerLineaporLinea(mujeres)


mergearFicheros(hombres,mujeres,union)

print("---------EMPLEADOS--------")
leerLineaporLinea(union)

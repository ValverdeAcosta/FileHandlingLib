



__author__ = "Víctor Valverde Acosta"
__copyright__ = "Copyright (C) 2019 Víctor Valverde Acosta"
__license__ = "Public Domain"
__version__ = "1.0"





#LIBRERIA FICHEROS PYTHON
    #Escrita en Python 3.8.0



#CREACION Y BORRADO

#Borra un fichero si existe

def borraSiExisteElfichero(fichero):
    import os
    if  os.path.exists(fichero):
        os.remove(fichero)
    

#Crear fichero para sobreescribir

def sobreescribirEnFichero(fichero, varinsercion):
    f=open(fichero,"w")
    f.write(varinsercion)
    f.close()

#crear fichero para añadir

def añadirAFichero(fichero, varinsercion):
    f=open(fichero, "a")
    f.write(varinsercion)
    f.close()

#añadir a un fichero datos con salto de linea

def añadirAFicheroConSaltos(fichero, varinsercion):
    f=open(fichero, "a")
    f.write(varinsercion+"\n")
    f.close()

#Añadir varios datos en un fichero

def añadirVariosDatos(fichero, datos, limite):
    f=open(fichero, "a")
    for i in range(limite):
        f.write(datos)
    f.close()

#Añadir datos a un array y luego ordenarlos
    

def contenidodeFicheroaMatriz(fichero, matriz):
    f=open(fichero,"r")
    for i in f:
        matriz.append(i)
    return matriz

def algoritmoburbuja(matriz):
    longitud=len(matriz)
    for i in range(longitud):
        for j in range(0, longitud-i-1):
            if matriz[j]>matriz[j+1]:
                matriz[j], matriz[j+1]=matriz[j+1],matriz[j]
    return matriz


#Introducción de empleados hombres y mujeres y ordenarlos alfabéticamente, separados en 2 ficheros

#Creacion de empleados
def crearEmpleados(mujeres, hombres):
    
    salida=0
    count=0
    while True:
        genero=str(input("Introduce un sexo de empleado: "))
        if genero=="mujer" or genero=="Mujer":
            
            mujeres.append(str(input("Introduce un nombre de empleado: ")))
            mujeres.append(int(input("Introduce una edad de empleado: ")))
            mujeres.append(genero)

        elif genero=="hombre" or genero=="Hombre":
            
            hombres.append(str(input("Introduce un nombre de empleado: ")))
            hombres.append(int(input("Introduce una edad de empleado: ")))
            hombres.append(genero)
        else:
            genero=str(input("Ese no es un genero valido! "))
        try:
            salida=int(input(" Introduce 1 si te cansas de introducir empleados "))
        except:
            pass
        count+=1
        if salida==1:
            print("SE HAN INTRODUCIDO "+str(count)+" EMPLEADOS EN SUS RESPECTIVOS FICHEROS. ¡Hasta pronto!")
            break
    
def insertarEmpleados(mujeres, hombres):
    fh=open("hombres.txt","a")
    fm=open("mujeres.txt","a")
    count=1
    count2=1
    for i in hombres:
        fh.write(str(i))
        if count%3==0:
            fh.write("\n")
        count+=1

    

    for j in mujeres:
        fm.write(str(j))
        if count2%3==0:
            fm.write("\n")    
        count2+=1

    fh.close()    
    fm.close()



#LECTURA


#leer fichero

def leerContenidoFichero(fichero):
    f=open(fichero, "r")
    print(f.read())

#Leer numero de caracteres concreto

def leerNumerodeCaracteres(fichero, numero):
    f=open(fichero, "r")
    print(f.read(numero))
    f.close()

#Leer fichero linea por linea
def leerLineaporLinea(fichero):
    f=open(fichero,"r")
    for x in f:
        print(x) 
    f.close()

#Leer un numero de lineas en concreto
def leerLineasConcretas(fichero, numerolineas):
    f=open(fichero,"r")
    count=0
    for x in f:
        count+=1
        print(x)
        if count>=numerolineas:
            break
    f.close()

#Leer las lineas pares

def leerLineasPares(fichero):
    f=open(fichero,"r")
    count=0
    for x in f:
        count+=1
        if count%2==0:
            print(x)
    
    f.close()


#Leer las lineas impares
def leerLineasImPares(fichero):
    f=open(fichero,"r")
    count=0
    for x in f:
        count+=1
        if count%2!=0:
            print(x)
    
    f.close()

#MERGEAR FICHEROS

def mergearFicheros(fichero1,fichero2, union): #Puedes meter tantos parametros de ficheros como quieras incluso un array de ficheros
    filenames=[fichero1,fichero2]
    with open(union, 'w') as ficherosalida:
        for fname in filenames:
            with open(fname) as infile:
                ficherosalida.write(infile.read())

    



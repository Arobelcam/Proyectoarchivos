#Programa de archivos y persistencia
#Realizado por Aaron Beltran Campos
#Fecha de realizacion: 24/04/2021


# Se importa el modulo csv para poder alterar el archivo de registros
import csv
# Se importa el modulo date time para poder trabajar con los datos en formato horario cuando se requiera
from datetime import datetime, timedelta
#Se importa el modulo para poder sacar la moda de la persona con mas registros en el archivo
from statistics import mode
#Se lee el archivo csv plantilla con los encabezado
with open('registro.csv') as f:
    data= f.readlines()
    print(data)
#Se establece una lista global donde se guardaran los datos ingresados
global lista
lista = list()
#Se establece un clase con los datos que se le solicitaran al usuario
class Usuario:
    fecha = ""
    nombre = ""
    edad = 0
    peso = 0
    altura = 0
    hinicio = 0
    hfinal = 0
    totalh= 0
    objetivo = ""
    
#Menu con las opciones de las acciones que realiza ell programa   
def menu():
    op = 0
    exit = 7
    while op != 7:
        print('.................................................................................................................')
        print("Menu")
        print("1. Ingreso de datos ")
        print('2. Hacer registro')
        print("3.Leer Archivo")
        print("4.Agregar nuevos registros")
        print('5.Mostrar elementos del archivo')
        print('6.Mostrar reporte')
        print("7.Salir")
#Dependiendo de el numero ingresado en el input este se dirigira al que cumpla condicion       
        op = int(input("Ingrese el numero de la accion que desea realizar:"))
        if op == 1:
            #En esta opcion se ingresan los datos que se guardaran en el registro del programa y es el primer registro
            def ingreso(): 
                a= Usuario()
                a.fecha = input ('Ingrese fecha que realizo la rutina: ')
                a.nombre = input('ingrese su nombre :')
                a.edad = int(input('Ingrese su edad :'))
                a.peso = float(input('Ingrese su peso (lbs): '))
                a.altura = float(input('Ingrese su altura(mts): '))
                a.hinicio = input("Ingrese la hora de inicio: ")
                a.hfinal = input("Ingrese la hora final :")
        
                #Utilizando el modulo datetime se convierten los valores ingresados a formato horario horas/minutos/segundos
                format_hora = "%H:%M" 
                hi = datetime.strptime(a.hinicio, format_hora)
                hf = datetime.strptime(a.hfinal, format_hora)
                
                a.totalh = (hf-hi)
                #Se utiliza de otra funcion de datetime llamada timedelta para convertir el valor ingresado en formato compatible
                #Con las horas de inicio y final
                tminimo= timedelta(minutes=30)
                print ("El tiempo de actividad fisica fue de: ", a.totalh)
                #Establece que si el tiempo de actividad fisica por sesion es mayor al tiempo minimo se mostrara el texto cumplido
                #Si por lo contrario, el tiempo es menor, entonces se mostrara el mensaje : 'Sin cumplir'
                if a.totalh >= tminimo:
                    a.objetivo = "Cumplido"
                    print("Cumplido")  
                else:
                    a.objetivo = "Sin cumplir"
                    print("Sin cumplir")
                    
                lista.append(a)  
            ingreso()
            menu()
            # Esta opcion permite exportar los elementos de almacenados en la lista global al archivo csv
        elif op == 2:
            def registro():
                # Ya que la funcion write solo acepta cadenas, los datos se pasan a ese formato
                for a in lista:
                    arch = str((a.fecha,a.nombre,a.edad,a.peso, a.altura,a.hinicio,a.hfinal, a.objetivo, a.totalh))
                    f = str(a.fecha)
                    n = str(a.nombre)
                    p = str(a.peso)
                    al= str(a.altura)
                    hin = str(a.hinicio)
                    hfin = str(a.hfinal)
                    o = str(a.objetivo)
                    t = str(a.totalh)
               # Se agregar al archivo en forma de append
                r= open('registro.csv', 'a')
                r.write(f)
                r.write(',')
                r.write(n)
                r.write(',')
                r.write(p)
                r.write(',')
                r.write(al)
                r.write('.')
                r.write(hin)
                r.write(',')
                r.write(hfin)
                r.write(',')
                r.write(o)
                r.write(',')
                r.write(t)
                r.write("\n")
                r.close()
            registro()
            menu()
            
          # La opcion 3 lee el archivo con los datos actualizados del registro  
        elif op == 3:
            def Leer():
                with open('registro.csv', 'r') as f:
                    datareader = csv.reader(f)
            Leer()
            menu()
            
            menu()
            #Esta opcion permite ingresar una fila de nuevos datos al archivo csv
        elif op == 4:
            def agregar():
                print('Ingresa los nuevos datos que deseas agregar al registro')
                a= Usuario()
                a.fecha = input ('Ingrese fecha que realizo la rutina: ')
                a.nombre = input('ingrese su nombre :')
                a.edad = int(input('Ingrese su edad :'))
                a.peso = float(input('Ingrese su peso (lbs): '))
                a.altura = float(input('Ingrese su altura(mts): '))
                a.hinicio = input("Ingrese la hora de inicio: ")
                a.hfinal = input("Ingrese la hora final :")
        
                
                format_hora = "%H:%M" 
                hi = datetime.strptime(a.hinicio, format_hora)
                hf = datetime.strptime(a.hfinal, format_hora)
                a.totalh = (hf-hi)
                
                tminimo= timedelta(minutes=30)
                
                if a.totalh >= tminimo:
                    a.objetivo = "Cumplido"
                    print("Cumplido")  
                else:
                    a.objetivo = "Sin cumplir"
                    print("Sin cumplir")
                    
                
                f = str(a.fecha)
                n = str(a.nombre)
                p = str(a.peso)
                al = str(a.altura)
                hin = str(a.hinicio)
                hfin = str(a.hfinal)
                o = str(a.objetivo)
                t = str(a.totalh)
   
                r= open('registro.csv', 'a')
                r.write(f)
                r.write(',')
                r.write(n)
                r.write(',')
                r.write(p)
                r.write(',')
                r.write(al)
                r.write(',')
                r.write(hin)
                r.write(',')
                r.write(hfin)
                r.write(',')
                r.write(o)
                r.write(',')
                r.write(t)
                r.write("\n")
                r.close()
                
                lista.append(a)
                
            agregar()
                # Esta opcion realiza la accion de imprimir el contenido actualizado del archivo csv
        elif op == 5:
            #Se muestra en pantalla los elementos actualizados en el archivo
            def mostrar():
                with open('registro.csv', 'r') as f:
                    datareader = csv.reader(f)
                    for row in datareader:
                        print(row)
            mostrar()
            menu()
            #En esta opcion se mostraran los reportes basicos como la persona que mas ejericio hizo , y la persona que mas entradas tiene en el registro
        elif op == 6:
            def reporte():
                '''
                #muestra los datos guardados en la lista global
                for a in lista:
                    arch= (a.fecha,a.nombre,a.edad,a.peso, a.altura,a.hinicio,a.hfinal, a.objetivo, a.totalh)
                    print(arch)
                    # devuelve la mayor cantidad de tiempo realizado en una misma sesion de ejericio
                for a in lista:
                    tact = str(a.totalh)
                    tiempo_de_actividad = float(tact)
                    print("El mayo tiempo actividad durante solo una sesion de ejericio fue de: ", max(tiempo_de_actividad))
                    # Devuelve la persona que mas entradas tiene en el registro
                for a in lista:
                    moda = (a.nombre)
                    print(mode(moda))
                '''
            reporte()
            menu()
          #Es la opcion de salida del programa  
        elif op == 7:
           def salir():
               print('GRACIAS POR UTILIZAR EL PROGRAMA')
               
           salir()
    
            
menu()  
            
        
    
        

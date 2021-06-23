#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys, json
from entidades.ETL import ETL

def main():
   menu()

def menu():
    objetos = None
    servicios = None
    with open('./ObjetosGeograficos.json', 'r', encoding="utf-8") as file1:
        objetos = json.load(file1)

    with open('./Servicios.json', 'r', encoding="utf-8") as file2:
        servicios = json.load(file2)

    os.system('cls||clear')
    print("     █████████████████████████████████████████████████████████")
    print("     ██████████████████████ ETL MIDAGRI ██████████████████████")
    print("     █████████████████████████████████████████████████████████")
    opcion = input("""
            0: Salir
            1: Listar Driver GDAL
            2: ETL PostgreSQL (SDE) --> ShapeFile
            3: ETL PostgreSQL (SDE) --> Oracle (SDE)
            4: ETL PostgreSQL (PostGIS) --> ShapeFile
            5: ETL PostgreSQL (PostGIS) --> Oracle (SDE)
            6: ETL OGC:WFS --> ShapeFile
            7: ETL OGC:WFS --> Oracle (SDE)
            8: ETL ArcGIS:Rest --> ShapeFile
            9: ETL ArcGIS:Rest --> Oracle (SDE)
            10. ETL ShapeFile --> Oracle (SDE)

            Por favor ingrese su elección: """)
    etl = ETL()

    if opcion == "0":
        print("Finalizado")
        sys.exit        
    elif opcion == "1":
        etl.ListarDrivers()
        print("Finalizado")
    elif opcion == "2":
        print("\n     ██████████████████████ ETL PostgreSQL --> ShapeFile ██████████████████████")
        mensaje = "\n\t\tElegir:"
        i=0
        mensaje = mensaje + "\n\t\t{0}. Salir".format(i)
        i=i+1
        for tabla in objetos:
            if tabla.find("SDE") != -1:
                mensaje = mensaje + "\n\t\t{0}. {1}".format(i, objetos[tabla]["pg_nombre"])
            i= i+1
        
        opcion_tabla = input(mensaje + "\n\n\tPor favor ingrese su elección: ")

        if isinstance(int(opcion_tabla), int):
            j=1
            for tabla in objetos:
                if int(opcion_tabla) == j:
                    etl.PostgreSQL2ShapeFile(tabla)
                j= j+1
    elif opcion == "3":
        print("\n     ██████████████████████ ETL PostgreSQL --> Oracle ██████████████████████")
        mensaje = "\n\t\tElegir:"
        i=0
        mensaje = mensaje + "\n\t\t{0}. Salir".format(i)
        i=i+1
        for tabla in objetos:
            if tabla.find("SDE") != -1:
                mensaje = mensaje + "\n\t\t{0}. {1}".format(i, objetos[tabla]["pg_nombre"])
            i= i+1

        opcion_tabla = input(mensaje + "\n\n\tPor favor ingrese su elección: ")

        if isinstance(int(opcion_tabla), int):
            j=1
            for tabla in objetos:
                if int(opcion_tabla) == j:
                    etl.PostgreSQL2Oracle(tabla)
                j= j+1
    elif opcion == "4":
        print("\n     ██████████████████████ ETL PostgreSQL (PostGIS) --> ShapeFile ██████████████████████")
        mensaje = "\n\t\tElegir:"
        i=0
        mensaje = mensaje + "\n\t\t{0}. Salir".format(i)
        i=i+1
        for tabla in objetos:
            if tabla.find("POSTGIS") != -1:
                mensaje = mensaje + "\n\t\t{0}. {1}".format(i, objetos[tabla]["pg_nombre"])
            i= i+1

        opcion_tabla = input(mensaje + "\n\n\tPor favor ingrese su elección: ")

        if isinstance(int(opcion_tabla), int):
            j=1
            for tabla in objetos:
                if int(opcion_tabla) == j:
                    etl.PostGIS2ShapeFile(tabla)
                j= j+1
    elif opcion == "5":
        print("\n     ██████████████████████ ETL PostgreSQL (PostGIS) --> Oracle ██████████████████████")
        mensaje = "\n\t\tElegir:"
        i=0
        mensaje = mensaje + "\n\t\t{0}. Salir".format(i)
        i=i+1
        for tabla in objetos:
            if tabla.find("POSTGIS") != -1:
                mensaje = mensaje + "\n\t\t{0}. {1}".format(i, objetos[tabla]["pg_nombre"])
            i= i+1

        opcion_tabla = input(mensaje + "\n\n\tPor favor ingrese su elección: ")

        if isinstance(int(opcion_tabla), int):
            j=1
            for tabla in objetos:
                if int(opcion_tabla) == j:
                    etl.PostGIS2Oracle(tabla)
                j= j+1       
    elif opcion == "6":
        print("\n     ██████████████████████ ETL OGC:WFS --> ShapeFile ██████████████████████")
        mensaje = "\n\t\tElegir:"
        i=0
        mensaje = mensaje + "\n\t\t{0}. Salir".format(i)
        i=i+1
        for tipo in servicios:
            if tipo.find("OGC:WFS") != -1:
                mensaje = mensaje + "\n\t\t{0}. {1}".format(i, servicios[tipo]["nombre"])
            i= i+1

        opcion_servicio = input(mensaje + "\n\n\tPor favor ingrese su elección: ")

        if isinstance(int(opcion_servicio), int):
            j=1
            for tipo in servicios:
                if int(opcion_servicio) == j:
                    etl.WFS2ShapeFile(tipo)
                j= j+1    
    else:
        print("Solo debe de seleccionar la opcíón [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
        print("Inténtalo de nuevo")
        menu()

main()
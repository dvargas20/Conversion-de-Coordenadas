# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 23:31:42 2024

@author: Diana Angelica
"""


class Coordenadas:
#Incluye  métodos que permiten convertir coordenadas de Grados Decimales (DD) a Grados, Minutos y Segundos (DMS), y viceversa.
   
    def dd_a_dms(dd):
        grados = int(dd)
        minutos_completos = abs((dd - grados) * 60)
        minutos = int(minutos_completos)
        segundos = (minutos_completos - minutos) * 60
        return grados, minutos, segundos

    def dms_a_dd(grados, minutos, segundos):
        dd = abs(grados) + minutos / 60 + segundos / 3600
        return dd if grados >= 0 else -dd
    
## se seleciona el tipo de conversion que el usuario quiere realizar 

def menu():
    print("Seleccione el tipo de conversión que desea realizar:")
    print("1. DD a DMS")
    print("2. DMS a DD")
    opcion = int(input(">> "))
    return opcion


## Se pide ingresar los valore numericos de las coordenadas expresadas en Grados Decimales (DD)

def obtener_coordenadas_dd():
    lat_dd = float(input("Ingrese el valor de la Latitud en DD: "))
    lon_dd = float(input("Ingrese el valor de la Longitud en DD: "))
    return lat_dd, lon_dd

## Se pide ingresar los valore numericos de las coordenadas expresadas en Grados, Minutos y Segundos (DMS)

def obtener_coordenadas_dms():
    lat_grados = int(input("Ingrese los grados de la Latitud: "))
    lat_minutos = int(input("Ingrese los minutos de la Latitud: "))
    lat_segundos = float(input("Ingrese los segundos de la Latitud: "))
    lon_grados = int(input("Ingrese los grados de la Longitud: "))
    lon_minutos = int(input("Ingrese los minutos de la Longitud: "))
    lon_segundos = float(input("Ingrese los segundos de la Longitud: "))
    return (lat_grados, lat_minutos, lat_segundos), (lon_grados, lon_minutos, lon_segundos)
## se piden las opciones que el usuario quiere elijir
def main():
    opcion = menu()

    if opcion == 1:
       
        # Conversión de DD a DMS
       
        lat_dd, lon_dd = obtener_coordenadas_dd()
        lat_grados, lat_minutos, lat_segundos = Coordenadas.dd_a_dms(lat_dd)
        lon_grados, lon_minutos, lon_segundos = Coordenadas.dd_a_dms(lon_dd)

        lat_hemisferio = 'N' if lat_dd >= 0 else 'S'
        lon_hemisferio = 'E' if lon_dd >= 0 else 'O'

        print(f"El valor de la latitud es:\n\t{abs(lat_grados)}° {lat_minutos}' {lat_segundos:.4f}'' {lat_hemisferio}")
        print(f"El valor de la longitud es:\n\t{abs(lon_grados)}° {lon_minutos}' {lon_segundos:.4f}'' {lon_hemisferio}")

    elif opcion == 2:
        
        # Conversión de DMS a DD
        
        (lat_grados, lat_minutos, lat_segundos), (lon_grados, lon_minutos, lon_segundos) = obtener_coordenadas_dms()
        lat_dd = Coordenadas.dms_a_dd(lat_grados, lat_minutos, lat_segundos)
        lon_dd = Coordenadas.dms_a_dd(lon_grados, lon_minutos, lon_segundos)

        print(f"El valor de la latitud en DD es:\n\t{lat_dd}")
        print(f"El valor de la longitud en DD es:\n\t{lon_dd}")

    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()


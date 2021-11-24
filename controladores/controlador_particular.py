from bd import obtener_conexion
from collections import Counter

def Registrar_Particular(nombreParticular,residenciaParticular,telefonoParticular,cedulaParticular):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO particulares(nombreParticular,residenciaParticular,telefonoParticular,cedulaParticular) VALUES (%s,%s,%s,%s)",(nombreParticular,residenciaParticular,telefonoParticular,cedulaParticular))
    conexion.commit()
    conexion.close()

def inicio_Secion_Particular(cedulaParticular):
    conexion = obtener_conexion()
    particular = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT cedulaParticular FROM particulares WHERE cedulaParticular = %s",(cedulaParticular))
        particular = cursor.fetchone()
    conexion.close()
    return particular

def registrar_Alquiler(nombreParticular,residenciaParticular,tiempoAlquiler,telefonoParticular,cantidadModulos,transporte,hora):
    conexion=obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO alquiler_Particulares(nombreParticular,residenciaParticular,tiempoAlquiler,telefonoParticular,cantidadModulos,transporte,hora)VALUES(%s,%s,%s,%s,%s,%s,%s)",(nombreParticular,residenciaParticular,tiempoAlquiler,telefonoParticular,cantidadModulos,transporte,hora))
    conexion.commit()
    cursor.close()

#Listar alquileres
def listar_alquileres_andamios(rut):
    conexion = obtener_conexion()
    rut2 = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM alquiler WHERE rut = %s",(rut))
        rut2 = cursor.fetchone()
    conexion.close()
    return rut2

    
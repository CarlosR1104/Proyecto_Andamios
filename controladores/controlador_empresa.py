from bd import obtener_conexion
from collections import Counter

def Registrar_Empresa(rut,nombreEmpresa,ubicacion,telefonoEmpresa,añosDeServicio,nombreAdministrador,telefonoAdministrador,cedulaAdministrador,correoAdministrador,contraseñaAdministrador):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO empresas(rut,nombreEmpresa,ubicacion,telefonoEmpresa,añosDeServicio,nombreAdministrador,telefonoAdministrador,cedulaAdministrador,correoAdministrador,contraseñaAdministrador) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(rut,nombreEmpresa,ubicacion,telefonoEmpresa,añosDeServicio,nombreAdministrador,telefonoAdministrador,cedulaAdministrador,correoAdministrador,contraseñaAdministrador))
    conexion.commit()
    conexion.close()

def inicio_Secion_Empresa(email):
    conexion = obtener_conexion()
    empresa = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT correoAdministrador, contraseñaAdministrador FROM empresas WHERE correoAdministrador = %s",(email))
        empresa = cursor.fetchone()
    conexion.close()
    return empresa

def registrar_Alquiler(nombreEmpresa,ubicacion,tiempoAlquiler,telefonoEmpresa,cantidadModulos,transporte,hora,RUT):
    conexion=obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO alquiler(nombreEmpresa,ubicacion,tiempoAlquiler,telefonoEmpresa,cantidadModulos,transporte,hora,RUT)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(nombreEmpresa,ubicacion,tiempoAlquiler,telefonoEmpresa,cantidadModulos,transporte,hora,RUT))
    conexion.commit()
    cursor.close()


# prueva de ranking
def ranking():
    conexion=obtener_conexion()
    ranking=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT  alquiler.rut as rut ,alquiler.nombreEmpresa as nombreEmpresa FROM andamios.alquiler" )
        ranking=cursor.fetchall()
    conexion.close
    return ranking

#Listar alquileres
def listar_alquileres_andamios(rut):
    conexion = obtener_conexion()
    rut2 = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM alquiler WHERE rut = %s",(rut))
        rut2 = cursor.fetchone()
    conexion.close()
    return rut2

def salidaAlquiler():
    conexion=obtener_conexion()
    salida=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT  alquiler.nombreEmpresa as nombreEmpresa,alquiler.telefonoEmpresa as telefonoEmpresa,alquiler.cantidadModulos,alquiler.tiempoAlquiler,alquiler.ubicacion,alquiler.hora,alquiler.transporte FROM andamios.alquiler" )
        salida=cursor.fetchall()  
    conexion.close
    return salida
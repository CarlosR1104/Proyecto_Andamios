from bd import obtener_conexion


def iniciar_sesion_Administrador (email):
    conexion = obtener_conexion()
    administrador = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT correoAdministrador, contraseñaAdministrador FROM administrador WHERE correoAdministrador = %s",(email))
        administrador = cursor.fetchone()
    conexion.close()
    return administrador
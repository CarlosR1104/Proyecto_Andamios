import pymysql 
def obtener_conexion():
	return pymysql.connect(host='localhost',
            user='root',
            password='3148202269',
            db='andamios')
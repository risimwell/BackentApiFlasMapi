from flask_mysqldb import MySQL
from app import nombre

def conectar():
    try:    
        app=nombre()
        conexion = MySQL(app)
        return conexion
    except Exception as ex:
        return False


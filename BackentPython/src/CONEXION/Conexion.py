from flask_mysqldb import MySQL
from app import *

def conectar():
    try:    
        conexion = MySQL(app)
        return conexion
    except Exception as ex:
        return False


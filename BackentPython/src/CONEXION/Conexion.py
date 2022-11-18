from flask_mysqldb import MySQL
from app import *

def conectar():
    conexion = MySQL(app)
    return conexion



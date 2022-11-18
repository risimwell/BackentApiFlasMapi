from CONEXION.Conexion import conectar
from flask import  request

def registro_acudiente(request):
    try:
        conexion=conectar()
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO acudiente (cedula_acudiente,nombre, apellido, telefono, clave) 
                VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')""".format(request.json['cedula_acudiente'],request.json['nombre'],request.json['apellido'],request.json['telefono'],request.json['clave'])
        print("codigo sql", sql)
        cursor.execute(sql)
        conexion.connection.commit()

        return True

    except Exception as ex:
        print(ex)
        return False


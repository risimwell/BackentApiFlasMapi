from CONEXION.Conexion import conectar

conexion=conectar()

def registro_acudiente(request):
    try :
        cursor = conexion.connection.cursor()
        sql = "CALL registro_acudiente('{0}', '{1}', '{2}', '{3}', '{4}')".format(request.json['cedula_acudiente'],request.json['nombre'],request.json['apellido'],request.json['telefono'],request.json['clave'])
        print("codigo sql", sql)
        cursor.execute(sql)
        conexion.connection.commit()
        return True
    except Exception as ex:
        return False





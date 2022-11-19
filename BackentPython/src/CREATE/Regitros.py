from datetime import date
from datetime import datetime
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


def registro_nino(request):
    try :
        cursor = conexion.connection.cursor()
        fecha_nacimiento = datetime.strptime(request.json['fecha_nacimiento'], '%Y-%m-%d')
        print(fecha_nacimiento)
        edad=(datetime.now()-fecha_nacimiento)/365
        print(edad)
        sql = "CALL registro_niño('{0}', '{1}', '{2}', '{3}','{4}', '{5}','{6}','{7}')".format(request.json['identificacion'],request.json['nombre'],request.json['apellido'],request.json['genero'],fecha_nacimiento,request.json['parentesco_acudiente'],request.json['cedula_acudiente'],request.json['codigo_grupo'])
        print("codigo sql", sql)
        # Ejecutar la sentencia SQL
        cursor.execute(sql)
        # Aceptar la sentencia SQL
        return True
    except Exception as ex:
        return False




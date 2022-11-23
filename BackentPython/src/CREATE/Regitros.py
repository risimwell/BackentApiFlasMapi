from datetime import datetime, date

def registro_acudiente(request):
    try :
        from CONEXION.Conexion import conectar #IMPORTAMOS EL METODO DE LA CONEXION
        conexion=conectar() #ESTABLECEMOS LA VARIABLE QUE CONTIENE LA RESPUESTA DEL METODO CONECTAR
        cursor = conexion.connection.cursor()  #INICIAMOS LA CONEXION
        #DECLARAM0S EL CODIGO SQL QUE SE EJECUTARA
        sql = "CALL registro_acudiente('{0}', '{1}', '{2}', '{3}', '{4}')".format(request.json['cedula_acudiente'],request.json['nombre'],request.json['apellido'],request.json['telefono'],request.json['clave'])
        print("codigo sql", sql) #IMPRIMIMOS LA EJECUSION SQL PARA VER QUE SE EJECURA
        cursor.execute(sql) #EJECUTAMOS LA SENTENCIA SQL
        conexion.connection.commit() #ACEPTAMOS LA SENTENCIA SQL
        return True #RETORNAMOS UN BOOL COMO INDICADOR 
    except Exception as ex:
        return False #RETORNAMOS UN BOOL COMO INDICADOR


def registro_nino(request):
    try :
        from CONEXION.Conexion import conectar #IMPORTAMOS EL METODO DE LA CONEXION
        conexion=conectar() #ESTABLECEMOS LA VARIABLE QUE CONTIENE LA RESPUESTA DEL METODO CONECTAR
        cursor = conexion.connection.cursor() #INICIAMOS LA CONEXION
        fecha_nacimiento = datetime.strptime(request.json['fecha_nacimiento'], '%Y-%m-%d') #HACEMOS UNS CASTING DE LA FECHA PARA QUE SEA TIPO DATE
        edad=(date.now()-fecha_nacimiento)/365 #CALCULAMOS LA EDAD 
        #DECLARAM0S EL CODIGO SQL QUE SE EJECUTARA
        sql ="CALL registro_niño('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(request.json['identificacion'],request.json['nombre'],request.json['apellido'],edad,request.json['genero'],request.json['fecha_nacimiento'],request.json['parentesco_acudiente'],request.json['cedula_acudiente'],request.json['codigo_grupo'])
        print("codigo sql", sql) #IMPRIMIMOS LA EJECUSION SQL PARA VER QUE SE EJECURA
        cursor.execute(sql) #EJECUTAMOS LA SENTENCIA SQL
        conexion.connection.commit() #ACEPTAMOS LA SENTENCIA SQL
        return True #RETORNAMOS UN BOOL COMO INDICADOR
    except Exception as ex:
        return False #RETORNAMOS UN BOOL COMO INDICADOR




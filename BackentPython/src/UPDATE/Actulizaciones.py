def actualizar_acudiente(request):
    try :
        from CONEXION.Conexion import conectar #IMPORTAMOS EL METODO DE LA CONEXION
        conexion=conectar() #ESTABLECEMOS LA VARIABLE QUE CONTIENE LA RESPUESTA DEL METODO CONECTAR
        cursor = conexion.connection.cursor()  #INICIAMOS LA CONEXION
        #DECLARAM0S EL CODIGO SQL QUE SE EJECUTARA
        sql = "CALL actualizar_informacio_acudiente('{0}', '{1}', '{2}', '{3}', '{4}')".format(request.json['cedula_acudiente'],request.json['nombre'],request.json['apellido'],request.json['telefono'],request.json['telefono_2'],request.json['acudiente_alternativo'])
        print("codigo sql", sql) #IMPRIMIMOS LA EJECUSION SQL PARA VER QUE SE EJECURA
        cursor.execute(sql) #EJECUTAMOS LA SENTENCIA SQL
        conexion.connection.commit() #ACEPTAMOS LA SENTENCIA SQL
        return True #RETORNAMOS UN BOOL COMO INDICADOR 
    except Exception as ex:
        return False #RETORNAMOS UN BOOL COMO INDICADOR

def actualizar_nino(request):
    try :
        from CONEXION.Conexion import conectar #IMPORTAMOS EL METODO DE LA CONEXION
        conexion=conectar() #ESTABLECEMOS LA VARIABLE QUE CONTIENE LA RESPUESTA DEL METODO CONECTAR
        cursor = conexion.connection.cursor()  #INICIAMOS LA CONEXION
        #DECLARAM0S EL CODIGO SQL QUE SE EJECUTARA
        sql = "CALL actualizar_informacion_niño('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(request.json['identificacion'],request.json['nombre'],request.json['apellido'],request.json['genero'],request.json['fecha_nacimiento'],request.json['parentesco'])
        print("codigo sql", sql) #IMPRIMIMOS LA EJECUSION SQL PARA VER QUE SE EJECURA
        cursor.execute(sql) #EJECUTAMOS LA SENTENCIA SQL
        conexion.connection.commit() #ACEPTAMOS LA SENTENCIA SQL
        return True #RETORNAMOS UN BOOL COMO INDICADOR 
    except Exception as ex:
        return False #RETORNAMOS UN BOOL COMO INDICADOR

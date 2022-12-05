def eliminar_acudiente(cedula_acudiente,conexion):
    try :
        cursor = conexion.connection.cursor()  #INICIAMOS LA CONEXION
        sql = "CALL eliminar_acudiente('{0}')".format(cedula_acudiente) #DECLARAM0S EL CODIGO SQL QUE SE EJECUTARA
        print("codigo sql", sql) #IMPRIMIMOS LA EJECUSION SQL PARA VER QUE SE EJECURA
        cursor.execute(sql) #EJECUTAMOS LA SENTENCIA SQL
        conexion.connection.commit() #ACEPTAMOS LA SENTENCIA SQL
        return True #RETORNAMOS UN BOOL COMO INDICADOR 
    except Exception as ex:
        return False #RETORNAMOS UN BOOL COMO INDICADOR


def eliminar_nino(identificacion,conexion):
    try :
        cursor = conexion.connection.cursor()  #INICIAMOS LA CONEXION
        sql = "CALL eliminar_niño('{0}')".format(identificacion) #DECLARAM0S EL CODIGO SQL QUE SE EJECUTARA
        print("codigo sql", sql) #IMPRIMIMOS LA EJECUSION SQL PARA VER QUE SE EJECURA
        cursor.execute(sql) #EJECUTAMOS LA SENTENCIA SQL
        conexion.connection.commit() #ACEPTAMOS LA SENTENCIA SQL
        return True #RETORNAMOS UN BOOL COMO INDICADOR 
    except Exception as ex:
        return False #RETORNAMOS UN BOOL COMO INDICADOR

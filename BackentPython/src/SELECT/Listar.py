
def listar_acudientes(conexion):
    try:
        cursor = conexion.connection.cursor()  #INICIAMOS LA CONEXION
        sql = "CALL listar_acudientes()" #DECLARAM0S EL CODIGO SQL QUE SE EJECUTARA
        cursor.execute(sql) #EJECUTAMOS LA SENTENCIA SQL
        print(sql)
        datos = cursor.fetchall() #.FETCHONE ACUMULA TODOS LOS DATOS QUE TRAIGA LA EJECUCION DEL CODIGO SQL
        print(datos)
        if datos != None: #CONDICION QUE COMPARA SI LA CONSULTA EN REALIDAD TRAJO DATOS 
            return datos #RETORNAMOS LA INFORMACION
        else:
            return None #RETORNAMOS EL VACIO 
    except Exception as ex:
        raise ex #RETORNAMOS LA EXCEPCION SI ALGO SALIO MAL 


def listar_ninos(conexion):
    try:
        cursor = conexion.connection.cursor()  #INICIAMOS LA CONEXION
        sql = "CALL listar_niños()" #DECLARAM0S EL CODIGO SQL QUE SE EJECUTARA
        cursor.execute(sql) #EJECUTAMOS LA SENTENCIA SQL
        print(sql)
        datos = cursor.fetchall() #.FETCHONE ACUMULA TODOS LOS DATOS QUE TRAIGA LA EJECUCION DEL CODIGO SQL
        print(datos)
        if datos != None: #CONDICION QUE COMPARA SI LA CONSULTA EN REALIDAD TRAJO DATOS 
            return datos #RETORNAMOS LA INFORMACION
        else:
            return None #RETORNAMOS EL VACIO 
    except Exception as ex:
        raise ex #RETORNAMOS LA EXCEPCION SI ALGO SALIO MAL 


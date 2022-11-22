def acudientes():
    try:
        from CONEXION.Conexion import conectar
        conexion=conectar()
        cursor = conexion.connection.cursor()
        sql = "CALL listar_acudientes()"
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            acudientes = {'cedula_acudiente': datos[0], 'nombre': datos[1], 'apellido': datos[2], 'telefono':datos[3],'telefono_2': datos[4], 'acudiente_alternativo':datos[5],'telefono_alternativo': datos[6], 'clave':datos[7]}
            return acudientes
        else:
            return None
    except Exception as ex:
        raise ex
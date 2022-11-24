#IMPORTACIO METODOS PROPIOS PARA QUE FUNCIONE EL API
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

#IMPORTACION CONFIGURACION DE LA BASE DE DATOS
from config import config


#IMPORTACION DE LOS METODOS DE CRUD BASICOS
from CREATE.Regitros import *
from DELETE.Eliminacion import *
from SELECT.Listar import *
from UPDATE.Actulizaciones import *
from VALIDACIONES.validaciones import *


app = Flask(__name__)

def nombre():
    return app

# CORS(app)
CORS(app, resources={r"/registro/*": {"origins": "http://localhost:4200"}})
CORS(app, resources={r"/login/*": {"origins": "http://localhost:4200"}})

conexion=MySQL(app)


#Metodos propios de mapi
@app.route('/login', methods=['POST'])
def iniciar_sesion():
    # Tomo los datos que provienen del JSON
    # request.json
    # Obtengo el correo y la contrasena de la base de datos usando el correo que me entregan por el JSON
    cedula = request.json['cedula']
    clave = request.json['clave']
    cursor = conexion.connection.cursor()
    sql = "SELECT nombre, clave FROM  acudiente WHERE  cedula_acudiente='%s'" %cedula
    cursor.execute(sql)
    resultado = cursor.fetchone()
    if resultado is not None:
        if (clave == resultado[0]):
            return jsonify({'usuario':"acudiente", 'exito': True,'nombre':resultado[1],'cedula':cedula}), 200
        else:
            return " Contraseña Incorrecta" 
    else:
        cursor = conexion.connection.cursor()
        sql = "SELECT nombre,clave FROM docente WHERE cedula_docente='%s'" %cedula
        cursor.execute(sql)
        resultado = cursor.fetchone()
        if resultado is not None:
            if (clave == resultado[0]):
                return jsonify({'usuario':"docente", 'exito': True,'nombre':resultado[1],'cedula':cedula}), 200
            else:
                return " Contraseña Incorrecta" 
        return "Usuario no registrado"


#CRUD acudiente
@app.route('/registroacudiente', methods=['POST'])
def registrar_acudiente():
        try:
            if registro_acudiente(request):
                return jsonify({'mensaje': "Acudiente registrado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar el registro", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400


@app.route('/listaracudientes', methods=['GET'])
def listar_acudientes():
        try:
            acudientes=listar_acudientes()
            if acudientes != None:
                for acudiente in acudientes:
                    print(acudiente)
                    #acudiente = {'cedula_acudiente': acudientes.cedula_acudiente, 'nombre': curso[1], 'apellido': curso[2], 'telefono':curso[3],'telefono_2': curso[4], 'acudiente_alternativo':curso[5],'telefono_alternativo': curso[6], 'clave':curso[7]}
                return jsonify({'curso': acudiente, 'mensaje': "Lista de acudientes.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "Acudientes no encontrado.", 'exito': False}), 400
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False}), 400


@app.route('/actualizaracudiente', methods=['PUT'])
def actualizar_acudiente():
        try:
            if actualizar_acudiente(request):
                return jsonify({'mensaje': "Acudiente actualizado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar la actualizacion", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400


@app.route('/eliminaracudiente/<cedula_acudiente>', methods=['DELETE'])
def eliminar_acudiente(cedula_acudiente):
        try:
            if eliminar_acudiente(cedula_acudiente):
                return jsonify({'mensaje': "Acudiente eliminado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo eliminar el acudiente", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400


#CRUD docente
@app.route('/registrodocente', methods=['POST'])
def registrar_docente():
        try:
            cursor = conexion.connection.cursor()
            sql = """INSERT INTO docente (cedula_docente,nombre, apellido, telefono,institucion, clave) 
            VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')""".format(request.json['cedula_docente'],request.json['nombre'],request.json['apellido'],request.json['telefono'],request.json['institucion'],request.json['clave'])
            print("codigo sql", sql)
            # Ejecutar la sentencia SQL
            cursor.execute(sql)
            # Aceptar la sentencia SQL
            conexion.connection.commit()  # Confirma la acción de inserción.
            return jsonify({'mensaje': "Acudiente registrado.", 'exito': True}), 200
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Error", 'exito': False}), 400

#CRUD grupos
@app.route('/registrogrupo', methods=['POST'])
def registrar_grupo():
        try:
            cursor = conexion.connection.cursor()
            sql = "CALL registragrpo ('{0}', '{1}', '{2}', '{3}', '{4}')".format(request.json['nombre_grupo'],request.json['codigo_grupo'],request.json['nombre_institucion'],request.json['fecha_creacion'],request.json['cedula_docente'])
            print("codigo sql", sql)
            # Ejecutar la sentencia SQL
            cursor.execute(sql)
            # Aceptar la sentencia SQL
            conexion.connection.commit()  # Confirma la acción de inserción.
            return jsonify({'mensaje': "Grupo Registrado.", 'exito': True}), 200
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Error", 'exito': False}), 400

#listar grupos
@app.route('/listargrupos', methods=['GET'])
def listar_grupos():
        try:
            acudientes=listar_acudientes()
            if acudientes != None:
                for grupos in grupos:
                    print(grupos)
                    #acudiente = {'cedula_acudiente': acudientes.cedula_acudiente, 'nombre': curso[1], 'apellido': curso[2], 'telefono':curso[3],'telefono_2': curso[4], 'acudiente_alternativo':curso[5],'telefono_alternativo': curso[6], 'clave':curso[7]}
                return jsonify({'curso': grupos, 'mensaje': "Lista de acudientes.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "Acudientes no encontrado.", 'exito': False}), 400
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False}), 400



#CRUD ninos
@app.route('/registronino', methods=['POST'])
def registrar_nino(): 
    try:
        if registro_nino(request):
            return jsonify({'mensaje': "Niño registrado.", 'exito': True}), 200
        else:
            return jsonify({'mensaje': "No se pudo realizar el registro", 'exito': False}), 400
    except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400


@app.route('/listarninos', methods=['GET'])
def listar_ninos():
        try:
            ninos=listar_ninos()
            if ninos != None:
                for nino in ninos:
                    print(nino)
                    #acudiente = {'cedula_acudiente': acudientes.cedula_acudiente, 'nombre': curso[1], 'apellido': curso[2], 'telefono':curso[3],'telefono_2': curso[4], 'acudiente_alternativo':curso[5],'telefono_alternativo': curso[6], 'clave':curso[7]}
                return jsonify({'curso': nino, 'mensaje': "Lista de niños.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "niños no encontrado.", 'exito': False}), 400
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False}), 400


@app.route('/actualizarnino', methods=['PUT'])
def actualizar_nino():
        try:
            if actualizar_nino(request):
                return jsonify({'mensaje': "niño actualizado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar la actualizacion", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400


@app.route('/eliminaracudiente/<identificacion>', methods=['DELETE'])
def eliminar_nino(identificacion):
        try:
            if eliminar_acudiente(identificacion):
                return jsonify({'mensaje': "Acudiente eliminado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo eliminar el acudiente", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400









# @cross_origin
@app.route('/cursos', methods=['GET'])
def listar_cursos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT codigo, nombre, creditos FROM curso ORDER BY nombre ASC"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursos = []
        for fila in datos:
            curso = {'codigo': fila[0], 'nombre': fila[1], 'creditos': fila[2]}
            cursos.append(curso)
        return jsonify({'cursos': cursos, 'mensaje': "Cursos listados.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def leer_curso_bd(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT codigo, nombre, creditos FROM curso WHERE codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            curso = {'codigo': datos[0], 'nombre': datos[1], 'creditos': datos[2]}
            return curso
        else:
            return None
    except Exception as ex:
        raise ex


@app.route('/cursos/<codigo>', methods=['GET'])
def leer_curso(codigo):
    try:
        curso = leer_curso_bd(codigo)
        if curso != None:
            return jsonify({'curso': curso, 'mensaje': "Curso encontrado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Curso no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


@app.route('/cursos/<codigo>', methods=['PUT'])
def actualizar_curso(codigo):
    if (validar_nombres(codigo) and validar_apellidos(request.json['nombre']) and validar_correo(request.json['creditos'])):
        try:
            curso = leer_curso_bd(codigo)
            if curso != None:
                cursor = conexion.connection.cursor()
                sql = """UPDATE curso SET nombre = '{0}', creditos = {1} 
                WHERE codigo = '{2}'""".format(request.json['nombre'], request.json['creditos'], codigo)
                cursor.execute(sql)
                conexion.connection.commit()  # Confirma la acción de actualización.
                return jsonify({'mensaje': "Curso actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Curso no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


@app.route('/cursos/<codigo>', methods=['DELETE'])
def eliminar_curso(codigo):
    try:
        curso = leer_curso_bd(codigo)
        if curso != None:
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM curso WHERE codigo = '{0}'".format(codigo)
            cursor.execute(sql)
            conexion.connection.commit()  # Confirma la acción de eliminación.
            return jsonify({'mensaje': "Curso eliminado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Curso no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()

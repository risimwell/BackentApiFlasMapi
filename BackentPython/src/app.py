from datetime import date
from datetime import datetime
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

from config import config
from VALIDACIONES.validaciones import *
from CREATE.Regitros import *
app = Flask(__name__)

# CORS(app)
CORS(app, resources={r"/registro/*": {"origins": "http://localhost:4200"}})
CORS(app, resources={r"/login/*": {"origins": "http://localhost:4200"}})
conexion = MySQL(app)

#Metodos propios de mapi

@app.route('/acudientes', methods=['GET'])
def leer_acudientes():
    try:
        curso=acudientes()
        if curso != None:
            return jsonify({'curso': curso, 'mensaje': "Sin acudientes.", 'exito': True})
        else:
            return jsonify({'mensaje': "Curso no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def acudientes():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM acudiente"
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            curso = {'cedula_acudiente': datos[0], 'nombre': datos[1], 'apellido': datos[2], 'telefono':datos[3],'telefono_2': datos[4], 'acudiente_alternativo':datos[5],'telefono_alternativo': datos[6], 'clave':datos[7]}
            return curso
        else:
            return None
    except Exception as ex:
        raise ex

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
            if validar_campo(request) :
                print (validar_campo(request.json['cedula_acudiente']))
                return jsonify({'mensaje': "Algun campo esta vacio", 'exito': False}), 400
            else:
                if registro_acudiente(request):
                    return jsonify({'mensaje': "Acudiente registrado.", 'exito': True}), 200
                else:
                    return jsonify({'mensaje': "Error", 'exito': False}), 400
               
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Error", 'exito': False}), 400


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


#CRUD ninos
@app.route('/registronino', methods=['POST'])
def registrar_nino():
        try:
            cursor = conexion.connection.cursor()
            nacimiento= request.json['fecha_nacimiento']
            print(nacimiento)
            ahora = datetime.strptime(nacimiento, '%Y-%m-%d')
            now = datetime.now()
            print(ahora)
            edad=now-ahora
            edad=edad/365
            print(edad)
            sql = "CALL crear_nino('{0}', '{1}', '{2}', '{3}','{4}', '{5}','{6}')".format(request.json['identificacion'],request.json['nombre'],request.json['apellido'],edad,request.json['genero'],request.json['fecha_nacimiento'],request.json['parentesco'])
            print("codigo sql", sql)
            # Ejecutar la sentencia SQL
            cursor.execute(sql)
            # Aceptar la sentencia SQL
            conexion.connection.commit()  # Confirma la acción de inserción.
            return jsonify({'mensaje': "niño registrado.", 'exito': True}), 200
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Error", 'exito': False}), 400


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

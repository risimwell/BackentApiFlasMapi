from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

from config import config
from validaciones import *

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


@app.route('/registroacudiente', methods=['POST'])
def registrar_acudienete():
        try:
            cursor = conexion.connection.cursor()
            sql = """INSERT INTO acudiente (cedula_acudiente,nombre, apellido, telefono, clave) 
            VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')""".format(request.json['cedula_acudiente'],request.json['nombre'],request.json['apellido'],request.json['telefono'],request.json['clave'])
            print("codigo sql", sql)
            # Ejecutar la sentencia SQL
            cursor.execute(sql)
            # Aceptar la sentencia SQL
            conexion.connection.commit()  # Confirma la acción de inserción.
            return jsonify({'mensaje': "Acudiente registrado.", 'exito': True}), 200
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Error", 'exito': False}), 400


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

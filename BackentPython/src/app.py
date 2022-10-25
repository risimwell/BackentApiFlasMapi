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


@app.route('/registro', methods=['POST'])
def registrar_curso():
    # print(request.json)
   
        try:
            cursor = conexion.connection.cursor()
            sql = """INSERT INTO usuarios (nombres, apellidos, cedula, clave, telefono) 
            VALUES ('{0}', '{1}', '{2}', '{3}', {4})""".format(request.json['nombres'],request.json['apellidos'],request.json['cedula'],request.json['clave'],request.json['telefono'])
            print("SENTENCIA", sql)
            # Ejecutar la sentencia SQL
            cursor.execute(sql)
            # Aceptar la sentencia SQL
            conexion.connection.commit()  # Confirma la acción de inserción.
            return jsonify({'mensaje': "Curso registrado.", 'exito': True}), 200
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Error", 'exito': False}), 400
    
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})

@app.route('/login', methods=['POST'])
def iniciar_sesion():
    # Tomo los datos que provienen del JSON
    # #  request.json
    # Obtengo el correo y la contrasena de la base de datos usando el correo que me entregan por el JSON
    cedula = request.json['cedula']
    clave = request.json['clave']
    cursor = conexion.connection.cursor()
    sql = "SELECT clave, nombres FROM usuarios WHERE cedula='%s'" %cedula
    cursor.execute(sql)
    resultado = cursor.fetchone()


    if resultado is not None:
        if (clave == resultado[0]):
            print("estoy adentro")
            return jsonify({'mensaje': "Login Exitoso.", 'exito': True,'nombre':resultado[1]}), 200
            
            
        else:
            
            return " Contrasena Incorrecta" 
    return " usuario no existe"
    
    
    
    

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

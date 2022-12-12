#IMPORTACIO METODOS PROPIOS PARA QUE FUNCIONE EL API
from flask import Flask, jsonify, request, session
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import jwt 
import bcrypt

#IMPORTACION CONFIGURACION DE LA BASE DE DATOS
from config import config


#IMPORTACION DE LOS METODOS DE CRUD BASICOS
from CREATE.Regitros import *
from DELETE.Eliminacion import *
from SELECT.Listar import *
from UPDATE.Actulizaciones import *
from VALIDACIONES.validaciones import *


app = Flask(__name__)

#COOKIE
app.secret_key='54SF4GHAFHGAS4' 

def nombre():
    return app

# CORS(app)
CORS(app, resources={r"/registro/*": {"origins": "http://localhost:4200"}})
CORS(app, resources={r"/login/*": {"origins": "http://localhost:4200"}})
CORS(app, resources={r"/listargrupos/*": {"origins": "http://localhost:4200"}})
CORS(app, resources={r"/listarninos/*": {"origins": "http://localhost:4200"}})

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
        print(clave,resultado[1])
        if (clave == resultado[1]):
            session["user"] = cedula
            return jsonify({'usuario':"acudiente", 'exito': True,'nombre':resultado[0],'cedula':cedula}), 200
        else:
            return " Contraseña Incorrecta" 
    else:
        cursor = conexion.connection.cursor()
        sql = "SELECT nombre,clave FROM docente WHERE cedula_docente='%s'" %cedula
        cursor.execute(sql)
        resultado = cursor.fetchone()
        if resultado is not None:
            if (clave == resultado[1]):
                session["user"] = cedula
                return jsonify({'usuario':"docente", 'exito': True,'nombre':resultado[0],'cedula':cedula}), 200
            else:
                return " Contraseña Incorrecta" 
        return "Usuario no registrado"

@app.route('/cerrarsesion', methods=['GET'])
def cerrar_sesion():
    if "user" in session:
    
        session.pop("user")
        return jsonify({'mensaje': "Sesion cerrada", 'exito': True}), 200
    return jsonify({'mensaje': "No se pudo cerrar sesion", 'exito': False}), 400


#CRUD acudiente
@app.route('/registroacudiente', methods=['POST'])
def registrar_acudiente():
        try:
            if registro_acudiente(request,conexion):
                return jsonify({'mensaje': "Acudiente registrado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar el registro", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400


@app.route('/listaracudientes', methods=['GET'])
def listar_acudiente():
        try:
            datos=listar_acudientes(conexion)
            lista_acudientes = []
            print(datos)
            if datos != None:
                for fila in datos:
                    acudiente = {'Cedula acudiente': fila[0], 'nombre': fila[1], 'apellido': fila[2], 'telefono': fila[3],'telefono_2': fila[4],'acudiente alternativo': fila[5],'telefono alternativo': fila[6],'clave': fila[7]}
                    print(acudiente)
                    lista_acudientes.append(acudiente)
                return jsonify({'usuarios': lista_acudientes, 'mensaje': "Usuarios listados.", 'exito': True}),200
            else:
                return jsonify({'mensaje': "niños no encontrado.", 'exito': False}), 400
        except Exception as ex:
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400


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


@app.route('/actualizaracudientecedula/<cedula_acudiente>', methods=['PUT'])
def actualizar_cedula(cedula_acudiente):
        try:
            if actualizar_acudiente_cedula(cedula_acudiente,request,conexion):
                return jsonify({'mensaje': "Acudiente actualizado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar la actualizacion", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400


@app.route('/eliminaracudiente/<cedula_acudiente>', methods=['DELETE'])
def eliminar_acudientes(cedula_acudiente):
        try:
            if eliminar_acudiente(cedula_acudiente,conexion):
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
            sql = "CALL registrar_Docente('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')""".format(request.json['cedula_docente'],request.json['nombre'],request.json['apellido'],request.json['telefono'],request.json['institucion'],request.json['clave'])
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
        cursor = conexion.connection.cursor()
        sql = "CALL listar_grupos()"
        cursor.execute(sql)
        datos = cursor.fetchall()
        grupos = []
        print(sql)
        for fila in datos:
            grupo = {'nombre_grupo': fila[0], 'codigo_grupo': fila[1], 'fecha_creacion': fila[2]}
            grupos.append(grupo)
        return jsonify({'cursos': grupos, 'mensaje': "Cursos listados.", 'exito': True}),200
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False}),400

   
#CRUD ninos
@app.route('/registronino', methods=['POST'])
def registrar_nino(): 
    try:
        print(request.json['identificacion'])
        
        if registro_nino(request,conexion):
            return jsonify({'mensaje': "Niño registrado.", 'exito': True}), 200
        else:
            return jsonify({'mensaje': "No se pudo realizar el registro", 'exito': False}), 400
    except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400


@app.route('/listarninos', methods=['GET'])
def listar_nino():
        try:
            datos=listar_ninos(conexion)
            lista_nino = []
            print(datos)
            if datos != None:
                for fila in datos:
                    nino = {'identificacion': fila[0], 'nombre': fila[1], 'apellido': fila[2], 'edad': fila[3], 'genero': fila[4], 'fecha_nacimiento': fila[5], 'codigo_grupo': fila[6]}
                    print(nino)
                    lista_nino.append(nino)
                return jsonify({'ninos': lista_nino, 'mensaje': "Usuarios listados.", 'exito': True}),200
            else:
                return jsonify({'mensaje': "niños no encontrado.", 'exito': False}), 400
        except Exception as ex:
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400


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


@app.route('/eliminarnino/<identificacion>', methods=['DELETE'])
def eliminar_ninos(identificacion):
        try:
            if eliminar_nino(identificacion,conexion):
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


@app.route('/comprar/<idproducto>',  methods=['GET'])
def comprar_f(idproducto):
    if "user" in session:
        email =  session["user"]
        return "Señor {} Ud ha comprado el articulo de id {}".format(email, idproducto)
    return "Por favor inicie sesión"

def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()

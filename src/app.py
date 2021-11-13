from flask import Flask, jsonify, request
from config import config
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

app=Flask(__name__)#para saber si esta es principal


#CORS(app)
CORS(app,resources={r"/curso/*":{'origins':'local host o ruta de pagina'}})
conexion=MySQL(app)
#@cross_origin
@app.route('/cursos', methods=['GET'])
def listar_cursos():
    try:
        cursor=conexion.connection.cursor()
        sql='select * from curso'
        cursor.execute(sql)
        data=cursor.fetchall()#guardamos lo que este en la base de datos 
        cursos=[]
        for fila in data:
            curso={'codigo':fila[0],'nombre':fila[1],'creditos':fila[2]}
            cursos.append(curso)
        return jsonify({'cursos':cursos,'mensaje':'Cursos listados.'})
    except Exception as ex:
        return jsonify({'mensaje':'Error ...'})

@app.route('/curso/<codigo>', methods=['GET'])
def leer_curso(codigo):
    try:
        cursor=conexion.connection.cursor()
        sql='select * from curso where codigo= "{0}"'.format(codigo)
        cursor.execute(sql)
        datos= cursor.fetchone()
        if datos != None:
            curso={'codigo':datos[0],'nombre':datos[1],'creditos':datos[2]}
            return jsonify({'cursos':curso,'mensaje':'Curso encotrado.'})
        else:
            return jsonify({'mensaje':'curso no encontrado'})
    except Exception as ex:
        return jsonify({'mensaje':'Error ...'})

@app.route('/cursos',methods=['POST'])
def registrar_cursos():
    try:
        #print(request.json)
        cursor= conexion.connection.cursor()
        sql='insert into curso values ("{0}","{1}",{2})'.format(request.json['codigo'],request.json['nombre'],request.json['creditos'])
        cursor.execute(sql)
        conexion.connection.commit() # confirma la accion de isersion
        return jsonify({'mensaje':'curso registrado'})
    except Exception as ex:
        return jsonify({'mensaje':'Error ...'})

@app.route('/cursos/<codigo>', methods=['DELETE'])
def eliminar_cursos(codigo):
    try:
        cursor= conexion.connection.cursor()
        sql="delete from curso where codigo='{}' ".format(codigo)
        cursor.execute(sql)
        conexion.connection.commit() # confirma la accion de isersion
        return jsonify({'mensaje':'curso eliminado'})
    except Exception as ex:
        return jsonify({'mensaje':'Error ...'})

@app.route('/curso/<codigo>', methods=['PUT'])
def actualizar_cursos(codigo):
    try:
        cursor= conexion.connection.cursor()
        sql="update curso set nombre='{0}', creditos={1} where codigo='{2}'".format(request.json['nombre'], request.json['creditos'],codigo)
        cursor.execute(sql)
        conexion.connection.commit() # confirma la accion de isersion
        return jsonify({'mensaje':'curso actualizado'})
    except Exception as ex:
        return jsonify({'mensaje':'Error ...!'})

def paguina_no__encontrada(error):
    return jsonify({'mensaje':'la pagina que itentas buscar no exixte ..'}),404

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,paguina_no__encontrada)
    app.run()
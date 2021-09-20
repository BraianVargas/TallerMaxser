from os import system
from flask import Flask, request, render_template, url_for, redirect, session
import hashlib
from datetime import date
from flask_sqlalchemy import SQLAlchemy
import time

from sqlalchemy.util.langhelpers import methods_equivalent

userExist = None

app = Flask(__name__)
app.config.from_pyfile("config.py")

from models import Usuarios, Equipos, db

# Section Methods
def burbuja(lista):
    cont=0
    ordenado=False
    tamano=len(lista)
    comparaciones=tamano
    for _ in range(0,tamano):
        if ordenado==True:
            break
        for j in range(0,comparaciones-1):
            ordenado=True
            cont=cont+1
            if lista[j].Fecha < lista[j+1].Fecha:
                ordenado=False
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
        comparaciones=comparaciones-1
    return lista






# Section Routes
@app.route('/form', methods = ['POST','GET'])
def form():
    if request.method == 'POST':
        userExist = Usuarios.query.filter_by(DNI=request.form['dni_numb']).first()
        if isinstance(userExist, Usuarios):
            equipo = Equipos(Marca = request.form['modelo'], Problema = request.form['problema'],
                             Tipo = request.form['tipo'], Accesorios = request.form['accesorios'],
                             Estado = "En espera", Password = request.form['password'], Backup = request.form['backup'],
                             Fecha = date.today(), Owner = userExist.DNI) #Toma los datos del formulario y crea un objeto Equipo basado en el modelo de la base de datos.
            db.session.add(equipo)
            db.session.commit()
            
            return redirect(url_for('modal', Nombre = str(userExist.Nombre), equipo = equipo.id))
            # return render_template("form.html",user = userExist, equi = equipo)

        else:
            user = Usuarios(Nombre = request.form['name'], DNI = request.form['dni_numb'],
                            Telefono = request.form['phone_numb']) #Toma los datos del formulario y crea un objeto usuario basado en el modelo de la base de datos. 
            
            equipo = Equipos(Marca = request.form['modelo'], Problema = request.form['problema'],
                             Tipo = request.form['tipo'], Accesorios = request.form['accesorios'],
                             Estado = "En espera", Password = request.form['password'], Backup = request.form['backup'],
                             Fecha = date.today(), Owner = user.DNI) #Toma los datos del formulario y crea un objeto Equipo basado en el modelo de la base de datos.
            db.session.add(user)
            db.session.add(equipo)
            db.session.commit()
            # db.session.close()
            print("LARGANDO MODAL")
            return redirect(url_for('modal', Nombre = user.Nombre, equipo = equipo.id))
            # return render_template("modal.html")
    else:
        return render_template("form.html")

@app.route('/modal <Nombre> <int:equipo>', methods=['POST', 'GET'])
def modal(Nombre, equipo):
    return render_template("modal.html", cli = Nombre, ID = equipo)

@app.route("/login", methods=['POST', 'GET'])
def PreLog():
    return render_template('loginAdmin.html')

@app.route('/administrator', methods=['POST'])
def login():
    username = request.form['user']
    password = request.form['password']

    if request.method == "POST":
        if username and password:
            usuario = Usuarios.query.filter_by(Nombre = username).first()
            if type(usuario) is not None:
                result = hashlib.md5(bytes(password, encoding='utf-8'))
                if usuario.Password == result.hexdigest():
                    session['DNI'] = usuario.DNI
                    return redirect(url_for('indexAdmin'))
                else:
                    return render_template('loginAdmin.html')
            else:
                return render_template('loginAdmin.html')
        else:
            return render_template('loginAdmin.html')
    else:
        return redirect(url_for("index"))

@app.route('/administrator/session/')
def indexAdmin():
    if "DNI" in session:
        return render_template("indexAdmin.html")
    else:
        return redirect(url_for('PreLog'))

@app.route('/buscaDNI/', methods=['POST', 'GET'])
def buscarDNI():
    if "DNI" in session and request.method == 'POST':
        dni = request.form['ToQuery']
        cons = db.session.query(Equipos).filter_by(Owner = dni).all() #Trae una lista de todos los equipos cargados
        if len(cons)>1:
            if len(cons)>3:
                consulta = cons[-(len(cons)-5):]
            consulta = burbuja(consulta)
        else:
            consulta = cons
        print(consulta)
        own = db.session.query(Usuarios).filter_by(DNI = dni).first()
        if own == None:
            return render_template("buscaDNI.html", owner = '' , equipos = '')
        else:
            return render_template("buscaDNI.html", owner = own , equipos = consulta)
    elif request.method == 'GET':
        print("METODO GET")
        return render_template("buscaDNI.html", owner = '', equipos = '')
    else:
        return redirect(url_for('PreLog'))


if __name__ == "__main__":
    app.run(debug=True)
    input()

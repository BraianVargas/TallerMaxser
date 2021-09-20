from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Usuarios(db.Model):
    __tablename__= "usuarios"
    Nombre = db.Column(db.String(50), nullable = False)
    Password = db.Column(db.String(100), nullable = True)
    DNI = db.Column(db.String(16),primary_key=True, nullable=False)
    Telefono = db.Column(db.String(15), nullable = False)
    Equipos = db.relationship('Equipos',backref='usuarios',cascade="all, delete-orphan",lazy='dynamic')
    
class Equipos(db.Model):
    __tablename__ = "equipos"
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    Marca = db.Column(db.String(15), nullable = False)
    Problema = db.Column(db.String(100), nullable = False)
    Tipo = db.Column(db.String(16),nullable=False)
    Accesorios = db.Column(db.String(20), nullable = False)
    Estado = db.Column(db.String(20), nullable = True)
    Password = db.Column(db.String(30), nullable = True)
    Backup = db.Column(db.String(10), nullable = True)
    Fecha = db.Column(db.Date, nullable = False)
    Owner = db.Column(db.Integer, db.ForeignKey('usuarios.DNI'))
    
from flask import render_template
from models import Usuario
from extensions import db
from config import app


@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_user/<nombre>/<email>')
def add_user(nombre, email):
    usuario = Usuario(nombre=nombre, email=email)
    db.session.add(usuario)
    db.session.commit()
    return f'Usuario {nombre} agregado con éxito.'

@app.route('/users')
def usuarios():
    usuarios = Usuario.query.all()
    return '<br>'.join([f'{u.id}. {u.nombre} - {u.email}' for u in usuarios])

if __name__ == '__main__':
    app.run(debug=True, port=8080)


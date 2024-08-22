from flask import Flask

\
app = Flask(__name__)

# Reemplaza 'username', 'password', 'localhost' y 'mi_flask_app' con tus propias credenciales
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin:admin1234@172.24.128.1:5432/api2_DB'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
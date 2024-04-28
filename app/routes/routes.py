from flask import Blueprint, jsonify,request

# Crear un objeto Blueprint para las rutas de la aplicación
app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def index():
    return 'Hola mundo'

# Rutas para estudiantes






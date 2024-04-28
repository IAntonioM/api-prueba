from flask import Blueprint, jsonify,request
from app.services.estudiantes_service import EstudiantesService


estudiantes_bp = Blueprint('estudiantes', __name__)
estudiantes_service = EstudiantesService()


@estudiantes_bp.route('/estudiante')
def listar_estudiantes():
    estudiantes =estudiantes_service.obtener_estudiantes()
    return estudiantes 

@estudiantes_bp.route('/estudiante/reconocimiento-facial', methods=['POST'])
def upload_img_student():
    print('paso 1')
    # Verificar si la solicitud contiene archivos
    if 'file' not in request.files:
        return jsonify({'error': 'No se encontró ningún archivo en la solicitud'}), 400
    print('paso 2')
    
    file = request.files['file']
    print('paso 3')
    codEstudiante = request.form.get('codigoEstudiante')
    nombCompletos = request.form.get('NombreCompleto')
    print('paso 4')
    
    # Verificar si el archivo está vacío
    if file.filename == '':
        return jsonify({'error': 'Nombre de archivo vacío'}), 400
    print('paso 5')
    
    # Guardar el archivo en la carpeta correspondiente
    img_path=estudiantes_service.guardar_imagen( file ,codEstudiante)
    print('paso 6')
    estudiantes_service.procesar_imagen(img_path)
    print('paso 7')
    # Devolver el nombre del archivo y la información del estudiante en la respuesta
    return jsonify({'codigoEstudiante': codEstudiante, 'NombreCompleto': nombCompletos}), 200







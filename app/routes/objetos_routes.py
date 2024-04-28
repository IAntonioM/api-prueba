from flask import Blueprint, jsonify,request

objetos_bp = Blueprint('objetos', __name__)

@objetos_bp.route('/objetos')
def listar_objetos():
    return 'Lista de objetos'


# @objetos_bp.route('/object/upload', methods=['POST'])
# def upload_img_object():
#     # Verificar si la solicitud contiene archivos
#     if 'file' not in request.files:
#         return jsonify({'error': 'No se encontró ningún archivo en la solicitud'}), 400
    
#     file = request.files['file']
    
#     # Verificar si el archivo está vacío
#     if file.filename == '':
#         return jsonify({'error': 'Nombre de archivo vacío'}), 400
    
#     # Obtener el nombre del archivo
#     filename = file.filename
    
#     # Devolver el nombre del archivo en la respuesta
#     return jsonify({'filename': filename}), 200
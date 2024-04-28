
import os
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN

class EstudiantesService:
    def __init__(self):
        # Aquí podrías inicializar cualquier cosa necesaria para tu servicio
        pass

    def obtener_estudiantes(self):
        # Aquí podrías realizar consultas a la base de datos u otras operaciones para obtener la lista de estudiantes
        estudiantes = [
            {"id": 1, "nombre": "Juan", "edad": 20},
            {"id": 2, "nombre": "María", "edad": 22},
            {"id": 3, "nombre": "Pedro", "edad": 21}
        ]
        return estudiantes

    def guardar_imagen(self,file, cod_estudiante):
        upload_folder = os.path.join('app', 'uploads', 'estudiante')
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        filename = cod_estudiante + '.jpg'
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return file_path

    def procesar_imagen(self,img_path):
        data = pyplot.imread(img_path)
        detector = MTCNN()
        caras = detector.detect_faces(data)
        for i, resultado in enumerate(caras):
            x1, y1, ancho, alto = resultado['box']
            x2, y2 = x1 + ancho, y1 + alto
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg, (150, 200), interpolation=cv2.INTER_CUBIC)
            cara_filename = os.path.splitext(os.path.basename(img_path))[0] + '.jpg'
            cv2.imwrite(os.path.join('app', 'uploads', 'estudiante', cara_filename), cara_reg)
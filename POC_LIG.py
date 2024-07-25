import tensorflow as tf
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import imghdr
from time import time
from threading import Thread
import re
import pytesseract
from pytesseract import Output
from concurrent.futures import ThreadPoolExecutor
from pdf2image import convert_from_bytes
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
model = tf.keras.models.load_model('models/model_full_data_v3.h5')
class_names = ['assinaturas', 'averbacao', 'lig']
padrao_matricula = r'(?i)\b(?:MATRÍCULA|matrícula|Matricula|matrícula\s*nº|matricula\s*nº|matriculafigha|matriculaficha|matricula\s*ficha|matriculanº|matriculado\s*sob\s*o\s*nº)\s*([\d.]+)\b'

padrao_numero_contrato = r"(?:CONTRATO\s*Nº|CONTRATO\s*Nº:|N(?:[ºo]|úmero)\s*|nº\s*|avenças\s*nº\s*|contrato\s*nº\s*|Nº\s*:?|número\s*)(10\d{9})"
seguro_clause = """SEGUROS - O Comprador pagará, juntamente com as prestações mensais, os prêmios dos
seguros obrigatórios, cujos valores nesta data estão indicados nos itens 6.C e 6.D e são devidos à
seguradora indicada no item 10.A. A cobertura securitária iniciará na data de assinatura deste Contrato
e, no vencimento da primeira prestação, o Comprador pagará os prêmios dos seguros
correspondentes ao primeiro e ao segundo mês de vigência da cobertura."""

from concurrent.futures import ThreadPoolExecutor

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def corregir_angulo_imagen(imagen):
    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar detección de bordes con Canny
    bordes = cv2.Canny(imagen_gris, 50, 150, apertureSize=3)

    # Obtener líneas utilizando la transformada de Hough
    lineas = cv2.HoughLines(bordes, 1, np.pi / 180, 200)

    # Calcular el ángulo promedio de las líneas detectadas
    angulo_promedio = 0.0
    num_lineas = len(lineas)

    for linea in lineas:
        for rho, theta in linea:
            angulo_promedio += theta

    angulo_promedio /= num_lineas

    # Convertir el ángulo a grados y obtener la rotación requerida
    angulo_grados = np.rad2deg(angulo_promedio)
    rotacion = int(angulo_grados) % 360

    # Rotar la imagen a la posición correcta
    altura, ancho = imagen.shape[:2]
    centro = (ancho // 2, altura // 2)
    matriz_rotacion = cv2.getRotationMatrix2D(centro, rotacion, 1.0)
    imagen_rotada = cv2.warpAffine(imagen, matriz_rotacion, (ancho, altura), flags=cv2.INTER_LINEAR)

    return imagen_rotada


def search_paragraphs(text, query):
    # Vetorização dos textos usando TF-IDF        
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text, query])

    # Encontrar o trecho mais semelhante
    sections = text.split("\n\n")
    max_similarity = 0

    for section in sections:
        section_vector = vectorizer.transform([section])
        section_similarity = cosine_similarity(vectors[1], section_vector)[0][0]
        if section_similarity > max_similarity:
            max_similarity = section_similarity
        if max_similarity > 0.5:
            return True
    return False
    
def pdf_to_images(folder_path):
    
    # load all pdfs in the folder lote and convert each page to tiff
    for file in os.listdir(folder_path):
        try:
            if file.endswith('.pdf'):
                file_path = os.path.join(folder_path, file)
                
                
                print(f'convertendo {file_path}')
                arquivo_pdf = open(file_path, 'rb').read()
                
                images = convert_from_bytes(arquivo_pdf, dpi=200, thread_count=4)
                images = [cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) for image in images]
                os.makedirs(f'output/{file}', exist_ok=True)
                file_name = file_path.split('/')[-1]
                for i, image in enumerate(images):
                    
                    tiff_path = os.path.join(f'output/{file_name}', f'{file_name}_page_{i+1}.png')
                    cv2.imwrite(tiff_path, image)
        except Exception as e:
            print(e)    
            continue

    return {"message": "pdf convertido para png"}

def image_to_array(image_path):
    images = []
    for image in os.listdir(image_path):
        if image.endswith('.png'):
            image = cv2.imread(os.path.join(image_path, image))
            image = cv2.resize(image, (256, 256))
            images.append(image)
    return images

def get_image_class(images: list, model: tf.keras.models.Model):
    predictions = model.predict(np.array(images))
    predictions = np.argmax(predictions, axis=1)
    return [class_names[pred] for pred in predictions]
    

def tesseract_ocr(image_path):
    text = pytesseract.image_to_string(Image.open(image_path), lang="por")
    return text


def get_numero_matricula(averbacao: list, INPUT_DRIR: str):
    text = ''

    for image in averbacao:

        text += tesseract_ocr(os.path.join(INPUT_DRIR, image))
        resultado = re.search(padrao_matricula, text)

        if resultado:
            numero_matricula_averbacao = resultado.group(1)
            return numero_matricula_averbacao

        else:
            return None
        
def get_numero_contrato(lig: list, INPUT_DRIR: str):
    text = ''
    matricula = False
    num_contrato = False
    seguro = False
    lig.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))

    
    for image in lig:
        if num_contrato and matricula and seguro:
            return num_contrato.group(), matricula.group(1), seguro

        text += tesseract_ocr(os.path.join(INPUT_DRIR, image))
        if not num_contrato:
            num_contrato = re.search(padrao_numero_contrato, text)
        if not matricula:
            matricula = re.search(padrao_matricula, text)
        
        if not seguro:
            seguro = search_paragraphs(text, seguro_clause)
            
    return num_contrato, matricula, seguro

ss = time()
i = 0
for contrato in os.listdir('lote_teste'):
    start = time()
    print(f'contrato: {i} de {len(os.listdir("lote_teste"))}')
    folder_path = f'lote_teste/{contrato}'
    pdf_to_images(folder_path) # convert pdf to images
    print('tiempo pdf_to_images: ',time() - start)
    images = image_to_array(f'output/{contrato}.pdf') # convert images to array
    
    
    predictions = get_image_class(images, model) # get image class
    images_class = dict(zip(os.listdir(f'output/{contrato}.pdf'), predictions))


    lig = [k for k, v in images_class.items() if v == 'lig']
    assinaturas = [k for k, v in images_class.items() if v == 'assinaturas']
    averbacao = [k for k, v in images_class.items() if v == 'averbacao']

    s_mat = time()
    matricula = get_numero_matricula(averbacao, f'output/{contrato}.pdf')
    print('tiempor_matricula: ',time() - s_mat)

    s_con = time()
    numero_contrato, mat, seg = get_numero_contrato(lig,  f'output/{contrato}.pdf')
    print('tiempor_contrato: ',time() - s_con)

    # Detetar contrato assinado
    # Assinado = get_assinatura(assinaturas) -> True/False

    print(matricula, numero_contrato, mat, seg)
    print(f'tempo contrato {i}: ',time() - start)
    print('\n ---------------------------------------')
    i += 1
print('tiempo total',time() - ss)
import tensorflow as tf
import os
import cv2
import numpy as np
import imghdr
from time import time
from threading import Thread
import re
import pytesseract
from pytesseract import Output
from pdf2image import  convert_from_path
from pdf2image.generators import counter_generator
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PIL
from concurrent.futures import ThreadPoolExecutor

def tesseract_ocr(image_path):
    text = pytesseract.image_to_string(Image.open(image_path), lang="por")
    return text


def get_image_class(images: list, model: tf.keras.models.Model):
    predictions = model.predict(np.array(images))
    predictions = np.argmax(predictions, axis=1)
    return [class_names[pred] for pred in predictions]




# model = tf.keras.models.load_model('models/model_full_data_v3.h5')
class_names = ['assinaturas', 'averbacao', 'lig']
padrao_matricula = r'(?i)\b(?:MATRÍCULA|matrícula|Matricula|matrícula\s*nº|matricula\s*nº|matriculafigha|matriculaficha|matricula\s*ficha|matriculanº|matriculado\s*sob\s*o\s*nº)\s*([\d.]+)\b'
model = tf.keras.models.load_model('models/model_full_data_v7.h5')

padrao_numero_contrato = r"(?:CONTRATO\s*Nº|CONTRATO\s*Nº:|N(?:[ºo]|úmero)\s*|nº\s*|avenças\s*nº\s*|contrato\s*nº\s*|Nº\s*:?|número\s*)(10\d{9})"
seguro_clause = """SEGUROS - O Comprador pagará, juntamente com as prestações mensais, os prêmios dos
seguros obrigatórios, cujos valores nesta data estão indicados nos itens 6.C e 6.D e são devidos à
seguradora indicada no item 10.A. A cobertura securitária iniciará na data de assinatura deste Contrato
e, no vencimento da primeira prestação, o Comprador pagará os prêmios dos seguros
correspondentes ao primeiro e ao segundo mês de vigência da cobertura."""


def get_numero_contrato(lig: list, INPUT_DRIR: str):
    text = ''
    matricula = False
    no_contrato = False
    # seguro = False
    lig.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))
    for image in lig:
        if no_contrato and matricula:
            return no_contrato.group(), matricula.group(1)

        text += tesseract_ocr(os.path.join(INPUT_DRIR, image))
        if not no_contrato:
            no_contrato = re.search(padrao_numero_contrato, text)
        if not matricula:
            matricula = re.search(padrao_matricula, text)
        
        # if not seguro:
        #     seguro = search_paragraphs(text, seguro_clause)
            
    return no_contrato, matricula


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
        
def convert_pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path, dpi=250, fmt='png', thread_count=4, output_folder='async_output')
    return images

def resize_images(images):
    images_resized = [image.resize((256, 256)) for image in images]
    return images_resized

path = 'lote_teste/10130455109/10130455109.pdf'

import time
start = time.time()
print ('start')
images = convert_pdf_to_images(path)
print ('images ', time.time()- start)
resized_images = resize_images(images)
print(f'resize_images: {time.time() - start} from path')
images_array = [np.array(image) for image in resized_images]
print ('images_array ', time.time()- start)

predictions = get_image_class(images_array, model)
print ('predictions ', time.time()- start)


textos = []

# Hacer el tessaract en paralelo
with ThreadPoolExecutor(max_workers=4) as executor:
    pool = executor.map(tesseract_ocr, [os.path.join('async_output', image) for image in os.listdir('async_output')])

for i in pool:
    textos.append(i)
    print ('i ', i)

print ('tesseract_ocr ', time.time()- start)

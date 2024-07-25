import asyncio
from pdf2image import convert_from_path, convert_from_bytes

def convert_pdf_to_images(pdf_path):
    number = [i for i in range(1, 100)]
    images = convert_from_path(pdf_path, dpi=300, fmt='png', output_folder='async_output', thread_count=4, output_file='contrato_teste',)
    return images

def convert_pdf_to_images_from_bytes(pdf_bytes):
    images = convert_from_bytes(pdf_bytes, dpi=300, fmt='png', output_folder='async_output', thread_count=4, output_file='contrato_teste_2', first_page=1)
    return images

path = 'lote_teste/10130455109/10130455109.pdf'

import time
start = time.time()
images = convert_pdf_to_images(path)
print(f'Time: {time.time() - start} from path')
print(images)

start = time.time()
with open(path, 'rb') as f:
    pdf_bytes = f.read()
images = convert_pdf_to_images_from_bytes(pdf_bytes)
print(f'Time: {time.time() - start} from bytes')

# SmartContractParser

ContractVision es una herramienta de Machine Learning diseñada para procesar documentos PDF digitalizados, clasificar las páginas y extraer información relevante utilizando OCR (Reconocimiento Óptico de Caracteres). Este proyecto utiliza una red neuronal convolucional (CNN) para clasificar las páginas en diferentes categorías, como "hoja de firma", "hoja de cláusulas" y "hoja de propiedad".

## Características

- **Procesamiento de PDFs**: Divide documentos PDF en páginas individuales.
- **Clasificación de Páginas**: Utiliza una CNN para clasificar cada página en "hoja de firma", "hoja de cláusulas" y "hoja de propiedad".
- **Extracción de Información**: Realiza OCR en cada página y extrae información relevante basada en el tipo de página.

## Requisitos

- Python 3.7+
- TensorFlow
- PyPDF2
- OpenCV
- Tesseract OCR
- NumPy
- pandas


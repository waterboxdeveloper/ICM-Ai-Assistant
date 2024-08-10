import PyPDF2

def combinar_pdfs(lista_de_pdfs, salida):
    # Crear un objeto PdfMerger
    combinador = PyPDF2.PdfMerger()

    # Agregar cada archivo PDF a la lista
    for pdf in lista_de_pdfs:
        combinador.append(pdf)

    # Escribir el archivo PDF combinado en un nuevo archivo
    with open(salida, 'wb') as archivo_salida:
        combinador.write(archivo_salida)

# Lista de archivos PDF a combinar
lista_de_pdfs = ['archivo1.pdf', 'archivo2.pdf', 'archivo3.pdf']

# Nombre del archivo PDF de salida
salida = 'combinado.pdf'

# Llamar a la función para combinar los PDFs
combinar_pdfs(lista_de_pdfs, salida)
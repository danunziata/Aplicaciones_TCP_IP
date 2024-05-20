import os

def create_project_structure(markdown_file):
    # Leer el archivo Markdown
    with open(markdown_file, 'r') as f:
        md_content = f.readlines()

    # Crear la carpeta principal en la ubicación deseada
    base_path = '/home/gianni/Aplicaciones_TCP_IP/Puntapie/03-Python/giannitibaldi'
    course_name = os.path.splitext(os.path.basename(markdown_file))[0]
    course_path = os.path.join(base_path, course_name)
    os.makedirs(course_path, exist_ok=True)

    # Template para los temas (sin acentos)
    template = '''# Titulo del Tema

## Resumen

Aqui puedes proporcionar un resumen breve del tema.

## Introduccion

Aqui puedes introducir el tema y proporcionar contexto o informacion relevante.

## Desarrollo

Aqui puedes desarrollar el contenido del tema en detalle.

## Cierre

Aqui puedes hacer un resumen o conclusion del tema.

## Actividad
'''
    # Procesar el contenido del archivo Markdown
    current_module = ''
    current_topic = ''
    for line in md_content:
        line = line.strip()
        if line.startswith('## Modulo'):  # Encabezado de modulo
            current_module = line.replace('## ', '').strip()
            print(f'Detectado modulo: {current_module}')
            module_path = os.path.join(course_path, current_module)
            os.makedirs(module_path, exist_ok=True)
        elif line.startswith('### Tema'):  # Encabezado de tema
            current_topic = line.replace('### ', '').strip()
            print(f'Detectado tema: {current_topic}')
            topic_path = os.path.join(module_path, current_topic)
            os.makedirs(topic_path, exist_ok=True)
            # Crear archivo Markdown para el tema
            with open(os.path.join(topic_path, f'{current_topic}.md'), 'w') as md_file:
                md_file.write(template)
            # Crear carpeta "assets" dentro del tema
            os.makedirs(os.path.join(topic_path, 'assets'), exist_ok=True)

    # Imprimir la ubicacion donde se genero la estructura de archivos
    print(f"La estructura de archivos y directorios ha sido creada exitosamente en: {os.path.abspath(course_path)}")

if __name__ == "__main__":
    markdown_file = input("Ingrese el nombre del archivo Markdown: ")
    create_project_structure(markdown_file)
import os
import shutil
import markdown


def parse_markdown_file(file_path):
    # Se abre el archivo Markdown y se lee su contenido
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Se convierte el contenido Markdown a HTML
        html_content = markdown.markdown(content)
        # Se dividen las líneas del HTML para procesarlas
        lines = html_content.split('\n')

        # Se inicializa la estructura del curso
        structure = {}
        current_module = None
        current_topic = None

        # Se recorren las líneas del HTML
        for line in lines:
            # Se verifica si la línea corresponde al título del curso
            if line.startswith('<h1>'):
                structure['course'] = line.replace('<h1>', '').replace('</h1>', '').strip()
            # Se verifica si la línea corresponde al título de un módulo
            elif line.startswith('<h2>'):
                current_module = line.replace('<h2>', '').replace('</h2>', '').strip()
                structure[current_module] = {}
            # Se verifica si la línea corresponde al título de un tema
            elif line.startswith('<h3>'):
                current_topic = line.replace('<h3>', '').replace('</h3>', '').strip()
                # Se inicializa la estructura del tema
                structure[current_module][current_topic] = {
                    "sections": {  # Secciones del tema
                        "Resumen": ["Aquí puedes proporcionar un resumen breve del tema."],
                        "Introducción": ["Aquí puedes introducir el tema y proporcionar contexto o información relevante."],
                        "Desarrollo": ["Aquí puedes desarrollar el contenido del tema en detalle."],
                        "Cierre": ["Aquí puedes hacer un resumen o conclusión del tema."],
                        "Actividad": []
                    }
                }
        return structure


def create_folder_structure(structure):
    # Se obtiene el nombre del curso
    course_name = structure['course']
    # Se crea la carpeta principal del curso
    os.makedirs(course_name, exist_ok=True)

    # Se recorren los módulos y temas para crear las carpetas correspondientes
    for module, topics in structure.items():
        if module != 'course':
            module_path = os.path.join(course_name, module)
            os.makedirs(module_path, exist_ok=True)
            for topic, details in topics.items():
                topic_path = os.path.join(module_path, topic)
                os.makedirs(topic_path, exist_ok=True)
                assets_path = os.path.join(topic_path, 'assets')
                os.makedirs(assets_path, exist_ok=True)

                topic_file_path = os.path.join(topic_path, f"{topic}.md")
                with open(topic_file_path, 'w', encoding='utf-8') as topic_file:
                    topic_file.write(f"# {topic}\n\n")
                    for section, content in details['sections'].items():
                        topic_file.write(f"## {section}\n\n")
                        for line in content:
                            topic_file.write(f"{line}\n\n")

def main(markdown_file):
    # Se analiza el archivo Markdown y se obtiene la estructura
    structure = parse_markdown_file(markdown_file)
    # Se crea la estructura de carpetas y archivos
    create_folder_structure(structure)
    print("Estructura de carpetas y archivos creada con éxito.")


if __name__ == "__main__":
    # Se solicita al usuario ingresar la ruta del archivo Markdown
    markdown_file = input("Ingrese la ruta del archivo Markdown: ")
    # Se llama a la función principal del programa
    main(markdown_file)

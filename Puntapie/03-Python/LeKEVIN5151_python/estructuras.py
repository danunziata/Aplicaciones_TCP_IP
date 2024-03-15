import os


def parse_markdown_file(md_file):
    with open(md_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        course_structure = {}
        modules = []
        current_module = None

        for line in lines:
            line = line.strip()
            if line.startswith("## Módulo"):
                current_module = {'name': line.replace(
                    "## ", ''), 'topics': []}
                modules.append(current_module)
            elif line.startswith("- Tema"):
                current_module['topics'].append(
                    {'name': line.replace("- ", '')})

        course_structure['modules'] = modules
    return course_structure


def create_course_structure(course_structure):
    course_name = "Curso de Programación Avanzada"  # Nombre del curso

    # Crear la carpeta principal del curso
    os.makedirs(course_name, exist_ok=True)

    # Iterar sobre los módulos y temas
    for module in course_structure['modules']:
        module_name = module['name']
        module_path = os.path.join(course_name, module_name)
        os.makedirs(module_path, exist_ok=True)

        for topic in module['topics']:
            topic_name = topic['name']
            topic_path = os.path.join(module_path, topic_name)
            os.makedirs(topic_path, exist_ok=True)

            # Copiar el archivo de template
            template_file = 'template_tema.md'
            with open(template_file, 'r', encoding='utf-8') as template:
                template_content = template.read()

            # Guardar el archivo de tema
            topic_md_file = os.path.join(topic_path, 'nombredeltema.md')
            with open(topic_md_file, 'w', encoding='utf-8') as topic_md:
                topic_md.write(template_content)

            # Crear la carpeta "assets"
            assets_path = os.path.join(topic_path, 'assets')
            os.makedirs(assets_path, exist_ok=True)


def main():
    md_file = 'markdown_referencia.md'  # Nombre de tu archivo Markdown
    course_structure = parse_markdown_file(md_file)
    create_course_structure(course_structure)


if __name__ == "__main__":
    main()

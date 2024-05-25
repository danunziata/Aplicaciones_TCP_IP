import os
import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension

class HeaderTreeprocessor(Treeprocessor):
    def run(self, root):
        structure = []
        current_module = None
        current_topic = None
        for element in root.iter():
            if element.tag == 'h1':
                # Principal carpeta del curso
                current_module = {'name': element.text, 'topics': []}
                structure.append(current_module)
            elif element.tag == 'h2' and current_module:
                # Módulos
                current_topic = {'name': element.text, 'subtopics': []}
                current_module['topics'].append(current_topic)
            elif element.tag == 'li' and current_topic:
                # Temas
                current_topic['subtopics'].append(element.text)
        return structure

class HeaderExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(HeaderTreeprocessor(md), 'headertree', 15)

def parse_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    md = markdown.Markdown(extensions=[HeaderExtension()])
    structure = md.convert(text)
    return structure

def create_structure(structure, template_content):
    for module in structure:
        module_name = module['name']
        os.makedirs(module_name, exist_ok=True)
        
        for topic in module['topics']:
            topic_name = topic['name']
            topic_path = os.path.join(module_name, topic_name)
            os.makedirs(topic_path, exist_ok=True)
            
            for subtopic in topic['subtopics']:
                subtopic_name = subtopic
                subtopic_path = os.path.join(topic_path, subtopic_name)
                os.makedirs(subtopic_path, exist_ok=True)
                
                # Crear archivo del tema
                file_path = os.path.join(subtopic_path, 'nombredeltema.md')
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(template_content)
                
                # Crear carpeta assets
                assets_path = os.path.join(subtopic_path, 'assets')
                os.makedirs(assets_path, exist_ok=True)

def main(markdown_file, template_file):
    structure = parse_markdown(markdown_file)
    with open(template_file, 'r', encoding='utf-8') as file:
        template_content = file.read()
    create_structure(structure, template_content)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Generador de estructuras de archivos a partir de un archivo Markdown")
    parser.add_argument('markdown_file', type=str, help='Archivo Markdown que define la estructura deseada')
    parser.add_argument('template_file', type=str, help='Archivo de template para los temas')
    
    args = parser.parse_args()
    main(args.markdown_file, args.template_file)

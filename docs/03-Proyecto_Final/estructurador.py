import os
import json
import sys

def crear_estructura(base_path, estructura):
    for nombre, contenido in estructura.items():
        ruta_actual = os.path.join(base_path, nombre)
        if isinstance(contenido, dict):
            # Crea el directorio
            os.makedirs(ruta_actual, exist_ok=True)
            # Llama recursivamente para crear el contenido del directorio
            crear_estructura(ruta_actual, contenido)
        else:
            # Crea el archivo
            with open(ruta_actual, 'w') as archivo:
                archivo.write(contenido)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python crear_estructura.py <archivo_json>")
        sys.exit(1)

    archivo_json = sys.argv[1]

    if not os.path.exists(archivo_json):
        print(f"El archivo {archivo_json} no existe.")
        sys.exit(1)

    with open(archivo_json, 'r') as f:
        estructura = json.load(f)

    base_path = '.'
    crear_estructura(base_path, estructura)

    print("Estructura de proyecto creada exitosamente.")

# Introducción a Python: Automatización y scripting


Python es un lenguaje de programación versátil y poderoso que se ha convertido en una herramienta fundamental en el campo de la automatización y scripting. Con su sintaxis clara y legible, Python facilita la creación de scripts y programas que pueden realizar tareas repetitivas o complejas de manera más eficiente.

La automatización se refiere a la capacidad de automatizar procesos y tareas mediante la escritura de código. Python ofrece una amplia gama de bibliotecas y módulos que permiten interactuar con el sistema operativo, manipular archivos, realizar solicitudes web, enviar correos electrónicos y mucho más. Esto hace que Python sea ideal para automatizar tareas rutinarias, como procesar archivos en lotes, realizar copias de seguridad programadas o extraer información de páginas web.

El scripting se refiere a la capacidad de escribir scripts, que son programas pequeños y específicos diseñados para realizar una tarea determinada. Python es un lenguaje de scripting muy popular debido a su facilidad de uso y a su amplia gama de bibliotecas y módulos disponibles. Los scripts de Python se utilizan para una variedad de propósitos, como procesamiento de datos, generación de informes, administración de sistemas y mucho más.

Algunas de las ventajas de utilizar Python para la automatización y scripting son:

- **Sintaxis legible:** Python tiene una sintaxis clara y fácil de entender, lo que facilita la escritura y el mantenimiento del código.
- **Amplia biblioteca estándar:** Python cuenta con una amplia biblioteca estándar que proporciona módulos y funciones para realizar una variedad de tareas, lo que acelera el desarrollo de scripts.
- **Compatibilidad multiplataforma:** Python se puede ejecutar en diferentes sistemas operativos, lo que permite que los scripts sean portables y funcionen en diferentes entornos.
- **Integración con otros lenguajes:** Python se puede combinar fácilmente con otros lenguajes de programación, lo que permite aprovechar el código existente y utilizar las fortalezas de cada lenguaje.

Puedes encontrar la documentación oficial de Python en el siguiente enlace: [Documentación oficial de Python](https://www.python.org/)

## ACTIVIDADES

### Actividad 1

```markdown 

# Historia de usuario: Generador de estructuras de archivos a partir de un archivo Markdown

Como desarrollador, necesito automatizar la creación de una estructura de archivos y directorios para un proyecto basado en un archivo Markdown que define la estructura deseada. Quiero un script en Python que pueda leer el archivo Markdown, interpretar los encabezados y generar automáticamente los directorios y archivos correspondientes.

## Criterios de aceptación:

- Como usuario, quiero poder proporcionar un archivo Markdown que define la estructura deseada.
- Como usuario, quiero que el script genere los directorios y archivos correspondientes según la estructura definida en el archivo Markdown.
- Como usuario, quiero que el script cree una carpeta principal con el nombre del curso.
- Como usuario, quiero que el script cree carpetas para cada módulo dentro de la carpeta principal.
- Como usuario, quiero que el script cree carpetas para cada tema dentro de cada módulo.
- Como usuario, quiero que el script copie archivos de templates disponibles en cada tema.
- Como usuario, quiero que el script cree una carpeta "assets" dentro de cada tema.

## Requisitos técnicos:

- Implementar el script en Python.
- Utilizar el módulo `markdown` de Python para leer y procesar el archivo Markdown.
- Utilizar el módulo `os` de Python para crear directorios y archivos.
- Validar la estructura del archivo Markdown para asegurarse de que está en el formato esperado antes de generar los directorios y archivos.
```

--------------------------------------------------
**Entrada: Archivo markdown de referencia**

```markdown 
# Curso de Programación Avanzada

## Módulo 1 - Introducción
- Tema 1 - Conceptos fundamentales
- Tema 2 - Estructuras de datos

## Módulo 2 - Programación Orientada a Objetos
- Tema 1 - Clases y objetos
- Tema 2 - Herencia y polimorfismo
```
**Salida: Estructura de archivos de  referencia**

```shell
Curso de Programación Avanzada/
├── Módulo 1 - Introducción/
│   ├── Tema 1 - Conceptos fundamentales/
│   │   └── nombredeltema.md
│   │   └── assets/
│   └── Tema 2 - Estructuras de datos/
│       └── nombredeltema.md
│       └── assets/
└── Módulo 2 - Programación Orientada a Objetos/
    ├── Tema 1 - Clases y objetos/
    │   └── nombredeltema.md
    │   └── assets/
    └── Tema 2 - Herencia y polimorfismo/
        └── nombredeltema.md
        └── assets/
```

**Template de referencia para los temas**

```markdown 
# Título del Tema

## Resumen

Aquí puedes proporcionar un resumen breve del tema.

## Introducción

Aquí puedes introducir el tema y proporcionar contexto o información relevante.

## Desarrollo

Aquí puedes desarrollar el contenido del tema en detalle.

## Cierre

Aquí puedes hacer un resumen o conclusión del tema.

## Actividad
´´´



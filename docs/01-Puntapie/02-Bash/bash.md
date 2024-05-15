# Introducción a Bash: Automatización

Herramienta fundamental, Bash (Bourne Again SHell), es un lenguaje de scripting y un intérprete de comandos ampliamente utilizado en sistemas Unix-like, como Linux y macOS.

Para aprovechar al máximo nuestro tiempo y recursos, Bash les brinda la capacidad de automatizar tareas repetitivas y monótonas. Ya sea procesar grandes volúmenes de datos, realizar análisis complejos o administrar sistemas, Bash puede ser un aliado confiable.

La automatización de tareas en Bash permitirá:

1. **Procesamiento eficiente de datos**: Con Bash, podrán manipular y transformar fácilmente conjuntos de datos utilizando comandos y expresiones regulares. Podrán filtrar, combinar y procesar grandes cantidades de información en segundos, lo que les permitirá realizar análisis más profundos y obtener resultados precisos.
2. **Administración de sistemas**: Bash les proporciona las herramientas necesarias para administrar sistemas de manera eficiente. Podrán escribir scripts para configurar y mantener servidores, monitorear recursos del sistema, realizar copias de seguridad y automatizar tareas de mantenimiento. Esto les permitirá ahorrar tiempo y minimizar errores en la gestión de infraestructuras tecnológicas.
3. **Desarrollo de software**: Bash es un lenguaje de scripting poderoso que les permitirá automatizar flujos de trabajo en el desarrollo de software. Podrán escribir scripts para compilar, probar y desplegar aplicaciones, lo que agilizará el ciclo de desarrollo y optimizará la calidad del software.


Para obtener más información sobre Bash y comenzar a explorar todas sus características y funcionalidades, les recomiendo consultar la documentación oficial de Bash en el siguiente enlace: [Documentación de Bash](https://www.gnu.org/software/bash/manual/bash.html).

## Actividades:

Para realizar las actividades requeridas, sigue la siguiente secuencia:

1. Realizar un Fork del Repositorio:
2. Crear un Issue con la Actividad Correspondiente:
3. Realizar la Actividad y Completarla:
4. Pase a revisión la actividad completa a colaborador
5. Solicitar un Pull Request al Repositorio Principal:

### Actividad 1: Obtener información del sistema en formato JSON utilizando un script Bash

#### Historia de usuario:

Como usuario de Ubuntu, quiero ejecutar un script Bash que me permita obtener información del sistema en formato JSON. Esto me brindará una forma conveniente de recopilar los detalles del sistema, como el sistema operativo, el kernel, la CPU, la memoria total, el espacio en disco, la versión de Bash y la versión de Python.

#### Criterios de aceptación:

- Como usuario de Ubuntu, quiero poder ejecutar el script Bash desde la línea de comandos en mi sistema.
- El script debe recopilar automáticamente la información del sistema requerida, 
  siguientes claves y valores (estos son de ejemplo):
    - "sistema_operativo": "Ubuntu 20.04"
    - "kernel": "5.4.0-86-generic"
    - "cpu": "Intel Core i7-8700K"
    - "memoria_total": "16 GB"
    - "espacio_disco": "500 GB"
    - "version_bash": "5.0.17"
    - "version_python": "3.8.10" (por ejemplo, si la versión de Python instalada es 3.8.10)
- El script debe imprimir el objeto JSON resultante en la salida estándar.
- El script debe guardar la salida como objeto JSON, con el nombre de archivo sistem_info.json

#### Definición de terminado:

- Se ha creado un script Bash llamado "system_info.sh" que cumple con los criterios de aceptación.
- El script ha sido probado con éxito en Ubuntu y produce un objeto JSON con la información del sistema requerida.
- El objeto JSON impreso en la salida estándar coincide con las claves y valores especificados anteriormente.
- Se ha documentado claramente cómo ejecutar y probar el script en el repositorio designado, incluyendo cualquier dependencia o configuración adicional que pueda ser necesaria.
- versionado en github en el repositorio original

#### Resultado esperado:
- script en el repositorio original
- archivo con la informacion del sistema del usuario sistem_info.json en el repositorio original



## Actividad 2: Verificación del Estado de Sitios Web

#### Historia de usuario:

Como usuario, quiero tener un script de Bash que me permita verificar el estado de un sitio web individual o realizar una verificación en masa de varios sitios web.

#### Criterios de Aceptación

1. Puedo ejecutar el script de Bash con una URL específica y obtener el código de estado del sitio web.
2. Si no proporciono una URL específica, el script utilizará una URL por defecto.
3. Puedo ejecutar el script con la opción `-f` seguida de un archivo válido que contenga una lista de sitios web.
4. Cuando ejecuto el script con la opción `-f` y un archivo válido, el script muestra el código de estado de cada sitio web en la lista.
5. El script muestra "UP!" si el código de estado es 200, y "DOWN" si es diferente de 200.

#### Definición de Terminado

El script de Bash cumple con los siguientes criterios:

1. Puede verificar el estado de un sitio web específico.
2. Puede utilizar una URL por defecto si no se proporciona una específica.
3. Puede realizar una verificación en masa utilizando la opción `-f` seguida de un archivo válido que contenga una lista de sitios web.
4. Muestra el código de estado de cada sitio web en la lista.
5. Muestra "UP!" si el código de estado es 200, y "DOWN" si es diferente de 200.
6. Versionado en github en el repositorio original

#### Resultado esperado:
- script en el repositorio original


#### Tareas

Las tareas involucradas en el desarrollo de esta historia de usuario podrían ser:

1. Crear un script de Bash.
2. Implementar la lógica para verificar el estado de un sitio web específico.
3. Implementar la lógica para utilizar una URL por defecto si no se proporciona una específica.
4. Implementar la lógica para leer un archivo válido que contiene una lista de sitios web.
5. Implementar la lógica para iterar sobre los sitios web en el archivo y mostrar el código de estado de cada uno.
6. Implementar la lógica para mostrar "UP!" si el código de estado es 200, y "DOWN" si es diferente de 200.
7. Probar el script con casos de prueba para asegurar su correcto funcionamiento.
8. Realizar pruebas adicionales y solucionar cualquier problema identificado.
9. Documentar el script y proporcionar instrucciones de uso.

#### Output posible

```shell
2024-03-10 08:30:00 - https://www.example1.com - 200 - UP!
2024-03-10 08:30:00 - https://www.example2.com - 404 - DOWN
2024-03-10 08:30:00 - https://www.example3.com - 200 - UP!
```

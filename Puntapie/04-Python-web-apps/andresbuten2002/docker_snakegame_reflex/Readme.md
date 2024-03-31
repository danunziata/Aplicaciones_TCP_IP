# SnakeGame con Reflex
Reflex es una herramienta innovadora que permite a los desarrolladores de Python crear aplicaciones web utilizando solo Python. Al eliminar la necesidad de aprender múltiples lenguajes y herramientas, Reflex simplifica el proceso de desarrollo y permite a los desarrolladores centrarse en escribir código limpio y eficiente.

Es un framework de desarrollo web moderno para Python que permite construir aplicaciones web de manera rápida y sencilla utilizando Python puro.

Este repositorio demuestra cómo utilizar Reflex para implementar un juego clásico de Snake en una aplicación web. El juego de Snake es un proyecto popular para principiantes que les permite familiarizarse con los conceptos básicos de la programación y la lógica de juego.

## Instalación
Reflex requiere Python 3.8+.

Es muy recomendable crear un entorno virtual para su proyecto. venv es la opción estándar.

Procediendo con el entorno venv, se debe crear un nuevo directorio para empezar.
```shell
mkdir my_app_name
cd my_app_name
```
Reemplazar my_app_name con el nombre de tu proyecto. Cambiar al nuevo directorio.

Luego, se debe configuar el entorno virtual.
```shell
python3 -m venv .venv
source .venv/bin/activate
```

Después, se procede a instalar Reflex, el cual esta disponible como un paquete pip.
```shell
pip install reflex
```
## Proyecto
Para inicializar un proyecto:
```shell
reflex init
```
Reflex tiene una aplicación por defecto cuando se inicializa el proyecto. Para correr esa aplicación, se debe ejecutar:
```shell
reflex run
```
Tu aplicación se ejecuta en http://localhost:3000 .

Inicializar tu proyecto crea un directorio con el mismo nombre que tu app. Aquí es donde escribirás la lógica de tu app.

Reflex genera una app por defecto en `my_app_name/my_app_name.py`.
Este es el archivo que debes modificar con programación en Python para crear una pagina web.

## Ejemplo
Se ha desarrollado un ejemplo en el que se muestra un clock tanto analógico como digital con programación Python en Reflex. El archivo que debes modificar se encuentra dentro de `my_app_name/my_app_name.py` al cual se ha trabajado con un entorno virtual venv para aislar librerias y dependencias.

En el directorio del repositorio de GitHub donde se encuentra este Readme.md está el archivo `app.py` que contiene la programación correspondiente al clock. Si te copias ese archivo e instalas las librerias y paquetes necesarios para correr tal aplicación mediante el archivo `requirements.txt` que se encuentra allí también, podrás ejecutar la app dentro de tu entorno virtual o de tu host local.

```shell
pip install -r requirements.txt
```

Una vez que tienes instalado lo necesario, para ejecutar el programa debes hacer:
```shell
reflex run
```
La aplicación se ejecuta en http://localhost:3000.
## Dockerfile

Este readme proporciona el enlace a un repositorio de DockerHUb donde se encuentra un archivo de Dockerfile. El Dockerfile es un archivo de texto que contiene una serie de instrucciones que Docker utiliza para construir una imagen de contenedor.

¿Por qué usar contenedores?
Los contenedores ofrecen varias ventajas significativas para el desarrollo y la implementación de aplicaciones:

- Portabilidad: Los contenedores encapsulan toda la aplicación y sus dependencias, lo que los hace altamente portátiles. Puedes ejecutar los mismos contenedores en diferentes entornos de desarrollo, pruebas y producción sin preocuparte por las diferencias en la configuración del sistema operativo o las bibliotecas.

- Aislamiento: Los contenedores proporcionan un entorno aislado para ejecutar aplicaciones, lo que significa que cada contenedor tiene su propio sistema de archivos, red y procesos. Esto ayuda a prevenir conflictos entre las aplicaciones y garantiza que una aplicación no afecte negativamente a otras que se ejecuten en el mismo host.

- Escalabilidad: Los contenedores son ligeros y rápidos de iniciar, lo que los hace ideales para escalar aplicaciones según la demanda. Puedes implementar múltiples instancias de un contenedor para manejar cargas de trabajo variables y distribuir la carga de manera eficiente.

- Consistencia: Al utilizar contenedores, puedes garantizar que todas las instancias de una aplicación se ejecuten de la misma manera, independientemente del entorno. Esto facilita la configuración y la administración de aplicaciones, ya que no hay sorpresas inesperadas debido a diferencias en la configuración del sistema.

- Despliegue rápido: Los contenedores permiten empaquetar y distribuir aplicaciones de manera rápida y eficiente. Puedes implementar nuevas versiones de aplicaciones con facilidad y revertir a versiones anteriores en caso de problemas, lo que facilita la entrega continua y la integración continua.

En el caso de que requieras clonar el repositorio y obtener los archivos debes generar la imagen, antes del contenedor, a partir de los archivos que se encuentran en esta carpeta, principalmente el Dockerfile. Para hacerlo, debes ejecutar los siguientes comandos:

```shell
git clone git@github.com:andresbuten2002/Aplicaciones_TCP_IP.git
cd Aplicaciones_TCP_IP/Puntapie/04-Python-web-apps/andresbuten2002/docker_snakegame_reflex/
docker built -t "nombre de la imagen" .
```
Con la imagen ya creada, procedes a crear el contenedor. Para ello debes implementar el siguiente comando:
```shell
docker run -it --network host bocha2002/snake:latest
```
El contenedor ya se levanta y la app corre por si sola. En la dirección de (http://localhost:3000) ya tienes tu app corriendo. Puedes acceder desde otro dispositivo mediante la dirección IP correspondiente y el puerto 3000.

La tercer manera de correr la aplicación es accediendo a la imagen ya creada en DockerHub. El repositorio se encuentra en: [bocha2002/snake](https://hub.docker.com/repository/docker/bocha2002/snake/general). Allí deber implementar el siguiente comando para obtener el archivo de Dockerfile. Recuerda que debes haber iniciado sesión con `docker login` en tu terminal.

```shell
docker pull bocha2002/snake:latest
```

Una vez que ya tienes la imagen descargada solo debes levantar el contenedor. Para ello debes implementar el siguiente comando:
```shell
docker run -it --network host bocha2002/snake:latest
```
El contenedor ya se levanta y la app corre por si sola. En la dirección de (http://localhost:3000) ya tienes tu app corriendo. Puedes acceder desde otro dispositivo mediante la dirección IP correspondiente y el puerto 3000.
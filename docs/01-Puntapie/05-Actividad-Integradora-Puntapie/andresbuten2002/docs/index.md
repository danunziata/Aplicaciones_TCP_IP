
# Python Project Template

A low dependency and really simple to start project template for Python Projects.

Streamlit es un marco de desarrollo de código abierto que permite crear aplicaciones web interactivas utilizando solo Python. Es especialmente popular en el campo de la ciencia de datos y el aprendizaje automático debido a su facilidad de uso y su capacidad para crear aplicaciones web rápidamente sin tener que escribir código HTML, CSS o JavaScript.

Streamlit proporciona una amplia variedad de widgets interactivos que los usuarios pueden usar para crear interfaces de usuario intuitivas y atractivas. Estos widgets incluyen controles deslizantes, botones, cuadros de texto y más, que permiten a los usuarios interactuar con los datos y ajustar los parámetros de la aplicación en tiempo real.

Una de las características más destacadas de Streamlit es su capacidad para actualizar automáticamente la interfaz de usuario en función de los cambios en el código subyacente. Esto significa que los desarrolladores pueden hacer cambios en su código y ver los resultados instantáneamente en la aplicación web sin tener que recargar la página.

Por otro lado, se integra perfectamente con bibliotecas populares de visualización de datos en Python, como Matplotlib, Plotly y Altair. Esto permite a los usuarios crear gráficos y visualizaciones de datos de alta calidad y mostrarlos en sus aplicaciones web con solo unas pocas líneas de código.

Una vez que se ha creado una aplicación en Streamlit, desplegarla en línea es fácil

Este repositorio demuestra cómo utilizar Streamlit para implementar algunas apps.


### What is included on this template?  
- 🤖 A [Makefile](Makefile) with the most useful commands to install, test, lint, format and release your project.
- 📃 Documentation structure using [mkdocs](http://www.mkdocs.org)
- 💬 Auto generation of change log using **gitchangelog** to keep a HISTORY.md file automatically based on your commit history on every release.
- 🐋 A simple [Containerfile](Containerfile) to build a container image for your project.  
  `Containerfile` is a more open standard for building container images than Dockerfile, you can use buildah or docker with this file.
- 🧪 Testing structure using [pytest](https://docs.pytest.org/en/latest/)
- 🛳️ Automatic release to [PyPI](https://pypi.org) using [twine](https://twine.readthedocs.io/en/latest/) and github actions.
- 🔄 Continuous integration using [Github Actions](.github/workflows/) with jobs to lint, test and release your project on Linux, Mac and Windows environments.



## Instalación
1. Clonar el repositorio
```shell
git clone git@github.com:andresbuten2002/Proyecto-Integrador-Final.git
docker built -t "nombre de la imagen:tag" .
```
2. Instalar Streamlit localmente. Esto es opcional, ya que hay tres formas de usar las aplicaciones, tal como se demuestra más abajo.
```shell
pip install streamlit
streamlit hello #Validar instalación
```
3. Instalar requerimientos. Dentro del mismo se encuentra streamlit y psutils (necesario para una de las apps). Como contiene streamlit, se puede obviar el paso 2.
```shell
pip install -r requirements.txt
```

Streamlit requiere Python 3.8+.

## Creación Entorno Virtual
Es muy recomendable usar un entorno virtual para su proyecto porque instalar o actualizar un paquete de Python puede causar efectos no intencionales en otro paquete. venv es la opción estándar.

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

## Usage
Este repositorio dispone de tres programas para utilizar. `app.py` muestra una barra de progreso que se actualiza dinámicamente para mostrar el progreso de una larga tarea de computación. La aplicación correspondiente al archivo `pc.py` muestra algo de información de tu máquina en tiempo real(cada vez que recargues la página). Por otro lado, La aplicación correspondiente al archivo `uber_pickups.py` permite visualizar los datos de recogida de Uber en la ciudad de Nueva York. Puedes seleccionar la hora mediante una barra deslizadora.

Hay varias maneras de usar, igualmente válidas si se usan entornos virtuales o no.
1. Para inicializar un proyecto debes crear un archivo `archivo.py` y modificarlo según el programa que desees crear. Aquí es donde escribirás la lógica de tu app. Puedes copiar los archivos `.py` que estan en este repositorio.
Para correr esa aplicación, se debe ejecutar:
```shell
streamlit run "archivo".py
```
2. Utilizar el archivo de Containerfile. En el caso de que requieras clonar el repositorio y obtener los archivos debes generar la imagen, antes del contenedor, a partir del [Containerfile](https://github.com/andresbuten2002/Proyecto-Integrador-Final/blob/main/Containerfile) que se encuentran en esta carpeta, principalmente el Dockerfile. Para hacerlo, debes ejecutar los siguientes comandos:

```shell
docker built -t "nombre de la imagen:tag" .
```

Con la imagen ya creada, procedes a crear el contenedor. Para ello debes implementar el siguiente comando:
```shell
docker run -it --network host "nombre de la imagen:tag"
```
Para correr algunas de las apps, debes ejecutar el siguiente comando:

```shell
streamlit run "archivo".py
```

La aplicación ya debería correr en la dirección IP de tu localhost y el puerto 8501. Puedes acceder desde otro dispositivo mediante la dirección IP correspondiente y el puerto 8501.

3. La tercer manera de correr la aplicación es accediendo a la imagen ya creada en DockerHub. El repositorio se encuentra en: [bocha2002/streamlit](https://hub.docker.com/repository/docker/bocha2002/streamlit/general). Allí deber implementar el siguiente comando para obtener el archivo de Dockerfile. Recuerda que debes haber iniciado sesión con `docker login` en tu terminal.

```shell
docker pull bocha2002/streamlit:1.0
```

Una vez que ya tienes la imagen descargada solo debes levantar el contenedor. Para ello debes implementar el siguiente comando:
```shell
docker run -it --network host bocha2002/streamlit:1.0
```
De la misma manera que antes, debes elegir que app ejecutar, modificar o crear una nueva. Después, en la dirección de (http://localhost:8501) ya tienes tu app corriendo. Puedes acceder desde otro dispositivo mediante la dirección IP correspondiente y el puerto 8501.


## Development

Read the [CONTRIBUTING.md](https://github.com/andresbuten2002/Proyecto-Integrador-Final/blob/main/CONTRIBUTING.md) file.

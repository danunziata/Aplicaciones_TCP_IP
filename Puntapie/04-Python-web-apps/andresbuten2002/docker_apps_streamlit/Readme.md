# Apps con Streamlit
Streamlit es un marco de desarrollo de código abierto que permite crear aplicaciones web interactivas utilizando solo Python. Es especialmente popular en el campo de la ciencia de datos y el aprendizaje automático debido a su facilidad de uso y su capacidad para crear aplicaciones web rápidamente sin tener que escribir código HTML, CSS o JavaScript.

Streamlit proporciona una amplia variedad de widgets interactivos que los usuarios pueden usar para crear interfaces de usuario intuitivas y atractivas. Estos widgets incluyen controles deslizantes, botones, cuadros de texto y más, que permiten a los usuarios interactuar con los datos y ajustar los parámetros de la aplicación en tiempo real.

Una de las características más destacadas de Streamlit es su capacidad para actualizar automáticamente la interfaz de usuario en función de los cambios en el código subyacente. Esto significa que los desarrolladores pueden hacer cambios en su código y ver los resultados instantáneamente en la aplicación web sin tener que recargar la página.

Por otro lado, se integra perfectamente con bibliotecas populares de visualización de datos en Python, como Matplotlib, Plotly y Altair. Esto permite a los usuarios crear gráficos y visualizaciones de datos de alta calidad y mostrarlos en sus aplicaciones web con solo unas pocas líneas de código.

Una vez que se ha creado una aplicación en Streamlit, desplegarla en línea es fácil

Este repositorio demuestra cómo utilizar Streamlit para implementar algunas apps.

## Dockerfile

Este readme proporciona el enlace a un repositorio de DockerHUb donde se encuentra un archivo de Dockerfile. El Dockerfile es un archivo de texto que contiene una serie de instrucciones que Docker utiliza para construir una imagen de contenedor.

¿Por qué usar contenedores?
Los contenedores ofrecen varias ventajas significativas para el desarrollo y la implementación de aplicaciones:

- Portabilidad: Los contenedores encapsulan toda la aplicación y sus dependencias, lo que los hace altamente portátiles. Puedes ejecutar los mismos contenedores en diferentes entornos de desarrollo, pruebas y producción sin preocuparte por las diferencias en la configuración del sistema operativo o las bibliotecas.

- Aislamiento: Los contenedores proporcionan un entorno aislado para ejecutar aplicaciones, lo que significa que cada contenedor tiene su propio sistema de archivos, red y procesos. Esto ayuda a prevenir conflictos entre las aplicaciones y garantiza que una aplicación no afecte negativamente a otras que se ejecuten en el mismo host.

- Escalabilidad: Los contenedores son ligeros y rápidos de iniciar, lo que los hace ideales para escalar aplicaciones según la demanda. Puedes implementar múltiples instancias de un contenedor para manejar cargas de trabajo variables y distribuir la carga de manera eficiente.

- Consistencia: Al utilizar contenedores, puedes garantizar que todas las instancias de una aplicación se ejecuten de la misma manera, independientemente del entorno. Esto facilita la configuración y la administración de aplicaciones, ya que no hay sorpresas inesperadas debido a diferencias en la configuración del sistema.

- Despliegue rápido: Los contenedores permiten empaquetar y distribuir aplicaciones de manera rápida y eficiente. Puedes implementar nuevas versiones de aplicaciones con facilidad y revertir a versiones anteriores en caso de problemas, lo que facilita la entrega continua y la integración continua.

El repositorio se encuentra en: [bocha2002/streamlit](https://hub.docker.com/repository/docker/bocha2002/streamlit/general). Allí deber implementar el siguiente comando para obtener el archivo de Dockerfile. Recuerda que debes haber iniciado sesión con `docker login` en tu terminal.

```shell
docker pull bocha2002/streamlit:1.0
```

Una vez que ya tienes la imagen descargada solo debes levantar el contenedor. Para ello debes implementar el siguiente comando:
```shell
docker run -it --network host bocha2002/streamlit:1.0
```

Una vez que ya tienes el contenedor en marcha y estas situado dentro de la carpeta `/app`, debes correr algunas de las tres aplicaciones correspondientes a los archivos de Python.

Para correr la `app.py`, la cual muestra una barra de progreso que se actualiza dinámicamente para mostrar el progreso de una larga tarea de computación, debes ejecutar el siguiente comando:

```shell
streamlit run app.py
```

La aplicación ya debería correr en la dirección IP de tu localhost y el puerto 8501. Puedes acceder desde otro dispositivo mediante la dirección IP correspondiente y el puerto 3000.

Lo mismo con las otras aplicaciones que estan disponibles en este repositorio. Debes colocar el nombre del archivo `.py` correspondiente.

```shell
streamlit run "archivo.py"
```

La aplicación correspondiente al archivo `pc.py` muestra algo de información de tu máquina en tiempo real(cada vez que recargues la página).

Por otro lado, La aplicación correspondiente al archivo `uber_pickups.py` permite visualizar los datos de recogida de Uber en la ciudad de Nueva York. Puedes seleccionar la hora mediante una barra deslizadora.

En el caso de que requieras clonar el repositorio y obtener los archivos debes generar la imagen, antes del contenedor, a partir de los archivos que se encuentran en esta carpeta, principalmente el Dockerfile. Para hacerlo, debes ejecutar los siguientes comandos:

```shell
git clone git@github.com:andresbuten2002/Aplicaciones_TCP_IP.git
cd Aplicaciones_TCP_IP/Puntapie/04-Python-web-apps/andresbuten2002/docker_apps_streamlit/
docker built -t "nombre de la imagen" .
```
Con la imagen ya creada, puedes implementar el mismo paso descripto anteriormente para levantar el contenedor.

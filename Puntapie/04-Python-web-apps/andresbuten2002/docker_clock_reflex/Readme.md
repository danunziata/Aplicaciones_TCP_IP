# Clock con Reflex
Reflex es una herramienta innovadora que permite a los desarrolladores de Python crear aplicaciones web utilizando solo Python. Al eliminar la necesidad de aprender múltiples lenguajes y herramientas, Reflex simplifica el proceso de desarrollo y permite a los desarrolladores centrarse en escribir código limpio y eficiente.

Es un framework de desarrollo web moderno para Python que permite construir aplicaciones web de manera rápida y sencilla utilizando Python puro.

Este repositorio demuestra cómo utilizar Reflex para implementar un reloj analógico y digital en el que puedes elegir la zona horaria.

## Dockerfile

Este readme proporciona el enlace a un repositorio de DockerHUb donde se encuentra un archivo de Dockerfile. El Dockerfile es un archivo de texto que contiene una serie de instrucciones que Docker utiliza para construir una imagen de contenedor.

¿Por qué usar contenedores?
Los contenedores ofrecen varias ventajas significativas para el desarrollo y la implementación de aplicaciones:

- Portabilidad: Los contenedores encapsulan toda la aplicación y sus dependencias, lo que los hace altamente portátiles. Puedes ejecutar los mismos contenedores en diferentes entornos de desarrollo, pruebas y producción sin preocuparte por las diferencias en la configuración del sistema operativo o las bibliotecas.

- Aislamiento: Los contenedores proporcionan un entorno aislado para ejecutar aplicaciones, lo que significa que cada contenedor tiene su propio sistema de archivos, red y procesos. Esto ayuda a prevenir conflictos entre las aplicaciones y garantiza que una aplicación no afecte negativamente a otras que se ejecuten en el mismo host.

- Escalabilidad: Los contenedores son ligeros y rápidos de iniciar, lo que los hace ideales para escalar aplicaciones según la demanda. Puedes implementar múltiples instancias de un contenedor para manejar cargas de trabajo variables y distribuir la carga de manera eficiente.

- Consistencia: Al utilizar contenedores, puedes garantizar que todas las instancias de una aplicación se ejecuten de la misma manera, independientemente del entorno. Esto facilita la configuración y la administración de aplicaciones, ya que no hay sorpresas inesperadas debido a diferencias en la configuración del sistema.

- Despliegue rápido: Los contenedores permiten empaquetar y distribuir aplicaciones de manera rápida y eficiente. Puedes implementar nuevas versiones de aplicaciones con facilidad y revertir a versiones anteriores en caso de problemas, lo que facilita la entrega continua y la integración continua.

El repositorio se encuentra en: [bocha2002/clock_reflex](https://hub.docker.com/repository/docker/bocha2002/clock_reflex/general). Allí deber implementar el siguiente comando para obtener el archivo de Dockerfile. Recuerda que debes haber iniciado sesión con `docker login` en tu terminal.

```shell
docker pull bocha2002/clock_reflex:latest
```

Una vez que ya tienes la imagen descargada solo debes levantar el contenedor. Para ello debes implementar el siguiente comando:
```shell
docker run -it --network host bocha2002/clock_reflex:latest
```
El contenedor ya se levanta y la app corre por si sola. En la dirección de (http://localhost:3000) ya tienes tu app corriendo. Puedes acceder desde otro dispositivo mediante la dirección IP correspondiente y el puerto 3000.

En el caso de que requieras clonar el repositorio y obtener los archivos debes generar la imagen, antes del contenedor, a partir de los archivos que se encuentran en esta carpeta, principalmente el Dockerfile.

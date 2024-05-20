<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />


<div align="center">
  <a href="https://github.com/danunziata/Aplicaciones_TCP_IP">
    <img src="assets/logotcpip.jpeg" alt="Logo" width="80" height="80">
  </a>
<h3 align="center">Aplicaciones TCP IP - 2024</h3>

  <p align="center">
    Diseño e implementación stack IOT
    <br />
    <a href="https://danunziata.github.io/Aplicaciones_TCP_IP/"><strong>Mira la Documentación completa »</strong></a>
    <br />
    <br />
  </p>

</div>


<!-- TABLE OF CONTENTS -->

  <summary>Tabla de Contenidos</summary>
  <ol>
    <li>
      <a href="#sobre-el-proyecto">Sobre el proyecto</a>
      <ul>
        <li><a href="#Componentes">Componentes</a></li>
      </ul>
    </li>
    <li>
      <a href="#para-comenzar">Para Comenzar</a>
      <ul>
        <li><a href="#prerequisitos">Prerequisitos</a></li>
        <li><a href="#instalación">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contribuir">Contribuir</a></li>
    <li><a href="#licencia">Licencia</a></li>
    <li><a href="#contacto">Contacto</a></li>
  </ol>


<!-- ABOUT THE PROJECT -->

## Sobre el proyecto


La materia Aplicaciones TCP IP, se centra en la formación profesional y laboral del egresado, la asignatura instruye a los estudiantes en las técnicas de diseño, construcción y monitoreo que se utilizan en las arquitecturas de redes de información y la toma de decisiones y análisis ingenieril de los sistemas que la componen. El elemento central de la asignatura es Internet, núcleo, componentes fundamentales para el funcionamiento y servicios. El proceso de enseñanza se basa en conceptos teórico/práctico que son implementados en prácticos de laboratorio, las evaluaciones parciales preparan al alumno para el examen final.


<p align="right">(<a href="#readme-top">Volver al Inicio</a>)</p>

### Componentes



- [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

- [![InfluxDB](https://img.shields.io/badge/InfluxDB-22ADF6?style=for-the-badge&logo=influxdb&logoColor=white)](https://www.influxdata.com/)

- [![EMQX](https://img.shields.io/badge/EMQX-0072C6?style=for-the-badge&logo=emqx&logoColor=white)](https://www.emqx.com/)

- [![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)](https://grafana.com/)

- [![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=black)](https://www.python.org/)

- [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://www.streamlit.io/)

- [![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)

- [![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

<p align="right">(<a href="#readme-top">Volver al Inicio</a>)</p>

<!-- GETTING STARTED -->

## Para Comenzar

Este repositorio tiene como objetivo proporcionarte la información necesaria para comenzar rápidamente a trabajar con el proyecto en cuestión. Ya seas un desarrollador experimentado o nuevo en el proyecto, esta guía te ayudará a empezar en poco tiempo.

### Prerequisitos

Tener instaladas las siguientes herramientas

- Docker: Necesitarás Docker instalado en tu sistema para poder ejecutar los contenedores de los servicios del servidor y cualquier contenedor de los clientes que utilices en el desarrollo.
- Python: Se requiere Python para ejecutar scripts y herramientas relacionadas con el desarrollo del servidor y los clientes.
- Curl: Curl es útil para realizar solicitudes HTTP desde la línea de comandos y puede ser útil durante el desarrollo y las pruebas.
- Git: Necesitarás Git para clonar el monorepo desde un repositorio remoto, así como para colaborar con otros miembros del equipo y realizar el control de versiones del código.


### Instalación

Acá se listan todo lo que se debe descargar para luego poder instalar y hacer funcionar el proyecto
* Python
  
  ```sh
  sudo apt update
  sudo apt install python
  ```

- Instalar las librerias necesarias

  ```sh
  python3 -m venv venv #Crea un nuevo entorno virtual donde se guardan todas las librerias a utilizar
  source venv/bin/activate
  pip install -r requirements.txt
  ```

<p align="right">(<a href="#readme-top">Volver al Inicio</a>)</p>

<!-- USAGE EXAMPLES -->

## Uso

Para ejemplos e información, por favor diríjase a la [Documentación](https://github.com/danunziata/Aplicaciones_TCP_IP)

<p align="right">(<a href="#readme-top">Volver al Inicio</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [ ] Investigar stacks IOT
- [ ] Desplegar un entorno de laboratorio local que permita realizar pruebas y experimentos.
- [ ] Seleccionar, evaluar e implementar un stack IOT 
- [ ] Realizar pruebas y evaluación del entorno
- [ ] Documentar el proceso, las configuraciones y los resultados de las pruebas realizadas.

<p align="right">(<a href="#readme-top">Volver al Inicio</a>)</p>

<!-- CONTRIBUTING -->
## Contribuir

### Flujo de Trabajo

El proceso que seguiremos implica utilizar la rama `main` como la rama de **producción** del proyecto. Cualquier nueva funcionalidad o corrección de errores se realizará creando nuevas ramas.

Para incorporar una función en la rama `main`,  simplemente se crea un "PR" (Pull Request), que deberá ser aprobado por algún colaborador, cualquier colaborador puede hacerlo, o bien, si no requiere revisión, puede ser aceptado por quien esté incluyendo la  funcionalidad.

Es crucial que el nombre de las ramas creadas sea lo más descriptivo  posible. Por ejemplo, si trabajamos en una nueva funcionalidad  relacionada con la API, la rama se debe llamar como referencia a la funcionalidad en cuestión. En el caso de tratarse de la corrección de un error en el código de la API, la llamaremos `fix-api`.

Además, se contarán con ramas específicas para la documentación del proyecto denominada `docs`, esta rama sera utilizada para registrar toda la documentación ya sea de la carpeta `docs` o el mismo `README.md`.

Los pasos para contribuir en este proyecto como miembro del mismo son:

1. Clonar el repositorio (`git clone`)
2. Crear una nueva rama para la función (`git checkout -b feature/AmazingFeature`)
3. Publicar la rama en el repositorio remoto(`git push --set-upstream origin <nombre-de-la-nueva-rama>`)
4. Commit los cambios (`git commit -m 'Add some AmazingFeature'`)
5. Push a la rama (`git push origin feature/AmazingFeature`)
6. Abrir un Pull Request dirigido a la rama `develop`

### Commits

Los commits convencionales nos permiten mantener la organización al realizar los commits y facilitan la creación de `releases` de forma automatizada.

Se basan en el uso de palabras clave al inicio del mensaje de cada commit, de la siguiente manera:

- **feat(tema de la modificación): Breve explicación**: Para cambios significativos o nuevas características.
- **fix(tema de la modificación): Breve explicación**: Para correcciones pequeñas.
- **chore(tema de la modificación): Breve explicación**: Para cambios menores insignificantes para el usuario.
- **docs: Breve explicación**: Para cambios que se realizan a la documentación.

<p align="right">(<a href="#readme-top">Volver al Inicio</a>)</p>

<!-- LICENSE -->

## Licencia

Este proyecto se distribuye bajo los términos de la  Licencia Pública General de GNU, versión 3.0 (GNU General Public  License, version 3.0). Consulta el archivo [LICENSE](https://github.com/danunziata/Aplicaciones_TCP_IP/blob/main/LICENSE) para obtener detalles completos.

### Resumen de la Licencia

La Licencia Pública General de GNU, versión 3.0 (GNU GPL-3.0), es una licencia de código abierto que garantiza la libertad de uso, modificación y distribución del software bajo los términos estipulados en la licencia. Requiere que cualquier software derivado se distribuya bajo los mismos términos de la GPL-3.0. Consulta el archivo [LICENSE](https://github.com/danunziata/Aplicaciones_TCP_IP/blob/main/LICENSE) para más información sobre los términos y condiciones.

### Aviso de Copyright

El aviso de copyright para este proyecto se encuentra detallado en el archivo [LICENSE](https://github.com/danunziata/Aplicaciones_TCP_IP/blob/main/LICENSE).

<p align="right">(<a href="#readme-top">Volver al Inicio</a>)</p>

<!-- CONTACT -->

## Contacto

Aplicaciones TCP IP - danunziata@ing.unrc.edu.ar, psolivellas@ing.unrc.edu.ar

Link del Proyecto: [https://github.com/danunziata/Aplicaciones_TCP_IP](https://github.com/danunziata/Aplicaciones_TCP_IP)

<p align="right">(<a href="#readme-top">Volver al Inicio</a>)</p>

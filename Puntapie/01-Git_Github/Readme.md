# Introducción a Git: Control de versiones y colaboración

Git es un sistema de control de versiones distribuido ampliamente utilizado en el desarrollo de software. Proporciona una forma eficiente y confiable de gestionar el historial de cambios en tus proyectos.

La principal función de Git es rastrear y registrar los cambios realizados en tus archivos a lo largo del tiempo. Esto te permite tener un control preciso sobre las diferentes versiones de tu proyecto y facilita la colaboración con otras personas.

Algunas de las ventajas de utilizar Git incluyen:

- **Control de versiones**: Git te permite mantener un historial completo de todos los cambios realizados en tu proyecto. Puedes ver qué cambios se hicieron, quién los hizo y cuándo se realizaron. Esto facilita la identificación y solución de problemas, así como la reversión a versiones anteriores si es necesario.

- **Trabajo en equipo y colaboración**: Git es especialmente útil cuando trabajas en equipo. Permite que varios desarrolladores trabajen en paralelo en diferentes ramas de desarrollo y fusionen sus cambios de manera controlada. Además, facilita la resolución de conflictos cuando varios desarrolladores modifican la misma parte de un archivo.

- **Ramificación y fusiones**: Con Git, puedes crear fácilmente ramas para trabajar en nuevas características o experimentar sin afectar la rama principal de desarrollo. Esto te permite mantener un flujo de trabajo organizado y seguro. Luego, puedes fusionar tus cambios en la rama principal una vez que estén listos y probados.

- **Recuperación de errores**: Git ofrece herramientas poderosas para deshacer cambios no deseados o revertir a una versión anterior de tu proyecto. Esto te permite corregir errores rápidamente y minimizar el impacto en tu trabajo.

- **Distribución y respaldo**: Git es un sistema de control de versiones distribuido, lo que significa que todos los desarrolladores tienen una copia completa del historial del proyecto en sus sistemas locales. Esto permite trabajar sin conexión a Internet y proporciona una capa adicional de seguridad y respaldo.

Git es una herramienta esencial para cualquier desarrollador de software. Aprender a utilizar Git te permitirá mantener un flujo de trabajo eficiente, colaborar de manera efectiva y tener un control completo sobre el historial de cambios en tus proyectos.

Además, Git se combina perfectamente con GitHub, una plataforma de alojamiento de código basada en Git que ofrece características adicionales para facilitar la colaboración y el trabajo en equipo. Algunas de las características importantes de GitHub incluyen:

- **Repositorios remotos**: GitHub proporciona una plataforma en la nube para alojar tus repositorios Git de forma segura y accesible desde cualquier lugar.

- **Solicitudes de extracción**: Permite que los desarrolladores propongan cambios en un repositorio y soliciten que se revisen y fusionen en la rama principal.

- **Issues**: Proporciona una forma de realizar un seguimiento de tareas, mejoras o errores en tu proyecto y facilita la colaboración entre desarrolladores para resolverlos.

- **Acciones**: Permite crear flujos de trabajo automatizados para compilar, probar y desplegar tu código de manera eficiente.

En resumen, Git y GitHub ofrecen herramientas esenciales para el control de versiones, la colaboración en proyectos de software y el trabajo en equipo. Aprovechar estas herramientas te ayudará a mejorar tu flujo de trabajo, aumentar la productividad y tener un control completo sobre el desarrollo y evolución de tus proyectos.

Si deseas obtener más información sobre Git y comenzar a explorar todas sus características y funcionalidades, te recomiendo consultar la [documentación oficial de Git](https://git-scm.com/doc). Para aprender más sobre cómo utilizar GitHub, puedes consultar la [documentación oficial de GitHub](https://docs.github.com/).


![github flow](assets/git-and-github-workflow.png)


## Conceptos Básicos de Git
A continuación se presentan algunos conceptos básicos de Git, junto con enlaces a la documentación oficial para obtener más información:

Git Clone: Clona un repositorio existente en tu máquina local. Documentación # Introducción a Git: Control de versiones y colaboración


### Crear una cuenta e iniciar sesión con clave SSH

1. Crear una cuenta en una plataforma de alojamiento de repositorios, como GitHub o GitLab.
   - GitHub: [https://github.com](https://github.com)
   - GitLab: [https://gitlab.com](https://gitlab.com)

2. Generar una clave SSH en tu máquina local.
   - Sigue las instrucciones oficiales para generar una clave SSH según tu sistema operativo:
     - [Generar una clave SSH en Windows](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
     - [Generar una clave SSH en macOS y Linux](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

3. Agregar la clave SSH generada a tu cuenta en la plataforma de alojamiento de repositorios.
   - Sigue las instrucciones oficiales para agregar tu clave SSH a tu cuenta:
     - [Agregar una clave SSH a tu cuenta de GitHub](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
     - [Agregar una clave SSH a tu cuenta de GitLab](https://docs.gitlab.com/ee/ssh/)

4. Configurar Git para usar la clave SSH.
   - Abre una terminal y ejecuta los siguientes comandos, reemplazando `tu-correo-electronico` con tu dirección de correo electrónico asociada a la cuenta de la plataforma de alojamiento de repositorios:

     ```shell
     git config --global user.email "tu-correo-electronico"
     git config --global user.name "Tu Nombre"
     ```

5. Verificar la configuración correcta de la clave SSH.
   - Ejecuta el siguiente comando en la terminal:

     ```shell
     ssh -T git@github.com
     ```

     Asegúrate de recibir un mensaje de autenticación exitosa.

6. ¡Listo! Ahora puedes iniciar sesión en la plataforma de alojamiento de repositorios utilizando la clave SSH.

### Conceptos Básicos de Git

A continuación se presentan algunos conceptos básicos de Git, junto con enlaces a la documentación oficial para obtener más información:

- **Git Clone**: Clona un repositorio existente en tu máquina local. [Documentación](https://git-scm.com/docs/git-clone)
- **Git Init**: Crea un nuevo repositorio vacío en tu máquina local. [Documentación](https://git-scm.com/docs/git-init)
- **Git Fork**: Crea una copia de un repositorio en tu cuenta en la plataforma de alojamiento de repositorios. [Documentación de GitHub](https://docs.github.com/es/get-started/quickstart/fork-a-repo) | [Documentación de GitLab](https://docs.gitlab.com/ee/user/project/repository/forking_workflow.html)
- **Git Add**: Agrega archivos o cambios al área de preparación (staging area) para ser incluidos en el siguiente commit. [Documentación](https://git-scm.com/docs/git-add)
- **Git Commit**: Guarda los cambios realizados en el repositorio como una nueva versión. [Documentación](https://git-scm.com/docs/git-commit)
- **Git Branch**: Crea, lista o elimina ramas en el repositorio. [Documentación](https://git-scm.com/docs/git-branch)
- **Git Checkout**: Cambia la rama o el commit actual en el repositorio. [Documentación](https://git-scm.com/docs/git-checkout)
- **Git Reset**: Deshace los cambios realizados en el repositorio a un estado anterior. [Documentación](https://git-scm.com/docs/git-reset)




## Actividades
- En el repositorio forkeado carga como issues cada una de las actividades.
- Agregue un colaborador al resositorio para asignarle la revision.

### Actividad: Creación de perfil en GitHub
La creación de un perfil en GitHub te permite mostrar tus proyectos y habilidades de manera atractiva y profesional. A continuación, se detallan los 
[setting up your profile in github](https://docs.github.com/en/get-started/start-your-journey/setting-up-your-profile)

#### Resumen
La actividad consiste en crear un perfil en GitHub y personalizarlo utilizando un generador de README en línea. Esto te permitirá agregar una descripción personalizada, mostrar tus proyectos y resaltar tus contribuciones.

#### Pasos a seguir
- **Crea un nuevo repositorio en GitHub:** Inicia sesión en tu cuenta de GitHub y crea un repositorio con el mismo nombre que tu usuario. Asegúrate de configurarlo como público.

- **Inicializa el repositorio con un archivo README.md:** Durante la creación del repositorio, selecciona la opción "Initialize this repository with a README" para crear automáticamente un archivo README.md.

- **Edita el archivo README.md:** Abre el archivo README.md en tu repositorio y agrega una descripción personalizada y cualquier otra información que desees mostrar en tu perfil. Guarda los cambios.

- **Utiliza generadores de README en línea**: Visita uno de los siguientes enlaces: 
   - [GitHub Profile ReadMe Generator](https://rahuldkjain.github.io/gh-profile-readme-generator/)
   - [readme.so](https://readme.so/)
   - [GPRM : GitHub Profile ReadMe Maker](https://gprm.itsvg.in/#google_vignette)
   - [Github Profilinator](https://profilinator.rishav.dev/)

- **Genera el contenido deseado:** Utiliza la herramienta seleccionada para generar el contenido de tu archivo README. Personaliza el diseño, agrega secciones específicas y muestra tus habilidades y proyectos de manera atractiva.

- **Copia y adapta el código generado:** Copia el código generado por la herramienta y pégalo en tu archivo README.md en GitHuby adaptalo a tu necesidad. Esto mejorará la apariencia de tu perfil y resaltará tu trabajo y contribuciones.


### Actividad: Completa y Muestra la Encuesta de Habilidades

#### Descripción:

Como Project Manager, te pido que completes la encuesta de habilidades en nombre de tu equipo de colaboradores. Es importante recopilar esta información para comprender las habilidades y conocimientos existentes en el equipo y poder asignar tareas de manera efectiva.

#### Pasos a seguir:

- Accede al repositorio forkeado del proyecto.
- Crea una carpeta con el nombre de usuario de GitHub
- Dentro de la carpeta, crea un archivo llamado "encuesta.md".
- Copia el siguiente template y responde la encuesta.

#### Encuesta de Herramientas - Git, GitHub, Bash y Python

```markdown
# Encuesta de habilidades

Nivel de conocimiento y habilidades en el uso de las siguientes herramientas, utilizando una escala del 1 al 5, donde:

1 = No tengo conocimiento
2 = Conocimiento básico
3 = Conocimiento intermedio
4 = Conocimiento avanzado
5 = Experto

**Nombre de usuario de GitHub**: [Nombre de usuario de GitHub del colaborador]
**Link profile usuario de GitHub**: [link al profile del usuario]
**Python**: [Valoración del 0 al 5]
**Bash**: [Valoración del 0 al 5]
**Git/GitHub**: [Valoración del 0 al 5]
```

- Realiza un commit en el repositorio forkeado con el mensaje "encuesta completa".
- Crea un pull request para enviar tus cambios al repositorio original.

#### Resultado esperado:

- Encuesta contestada por cada usuario en el repositorio original 

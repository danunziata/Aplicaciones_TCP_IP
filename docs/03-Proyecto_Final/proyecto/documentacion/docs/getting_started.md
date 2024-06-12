<!-- GETTING STARTED -->
# Getting Started

Este documento proporciona instrucciones para configurar y ejecutar el proyecto localmente. Para obtener una copia local en funcionamiento, siga estos sencillos pasos.

## Prerequisites

Para ejecutar este proyecto, necesitas tener instalado Docker y Docker Compose en tu máquina.

### Docker
Puedes usar el instalador que se encuentra en este link, el cual permite instalar Docker y otros programas que desees instalar: [Script Instalador](https://unrc.gitlab.io/labredes/scripts/)


### Docker Compose:
Descarga la última versión de Docker Compose del repositorio de GitHub oficial. Ejecuta el siguiente comando en tu terminal:
```sh
$ curl -SL https://github.com/docker/compose/releases/download/v2.17.2/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
```
A continuación, otorga permisos de ejecución a Docker Compose:
```sh
$ sudo chmod +x /usr/local/bin/docker-compose
```
La opción --version te permite comprobar si Compose se ha instalado correctamente.
```sh
$ docker-compose --version
```

## Installation
Sigue los siguientes pasos para instalar y configurar el proyecto:
1. Clona el repositorio
```sh
git clone git@github.com:danunziata/Aplicaciones_TCP_IP.git
```
2. Te situas en la carpeta server:
```sh
cd Aplicaciones_TCP_IP/docs/03-Proyecto_Final/proyecto/server/
```
3. Levantas los contenedores:
```sh
docker-compose up --build
```

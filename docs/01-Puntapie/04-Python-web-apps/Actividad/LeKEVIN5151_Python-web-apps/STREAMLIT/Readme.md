# Aplicación STREAMLIT

A continuación se explicará como se inicia una aplicación hecha en Streamlit la cual está dockerizada.

## Ejecución

1. [Asegúrate de tener Docker instalado en tu sistema.](https://unrc.gitlab.io/labredes/Docker/Docker_Instalacion/)

2. Los Archivos necesarios los encontrarás en el siguiente [link.](https://github.com/danunziata/Aplicaciones_TCP_IP/tree/main/docs/01-Puntapie/04-Python-web-apps/Actividad/LeKEVIN5151/STREAMLIT)

3. Construye la imagen Docker:

   ```bash
   docker build -t nombre_de_la_imagen
   ```

4. Ejecuta el contenedor Docker en modo host:

   ```bash
   docker run --network host nombre_de_la_imagen
   ```

5. Accede a la aplicación en tu navegador web en `http://localhost:8051`.

# APP BTC

## Requisitos

- Python 3.x
- Docker (opcional)

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu_usuario/tu_proyecto.git
    ```

2. Ve al directorio del proyecto:

    ```bash
    cd tu_proyecto
    ```

3. Instala las dependencias de Python:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

### Ejecución sin Docker

1. Asegúrate de que las dependencias de Python están instaladas (ver el paso de instalación).

2. Ejecuta la aplicación de Streamlit:

    ```bash
    streamlit run AppWebStreamlit.py
    ```

3. Accede a la aplicación en tu navegador web en `http://localhost:8501`.

### Ejecución con Docker

1. Asegúrate de tener Docker instalado en tu sistema (ver requisitos).

2. Construye la imagen Docker:

    ```bash
    docker build -t nombre_de_la_imagen .
    ```

3. Ejecuta el contenedor Docker en modo host:

    ```bash
    docker run --network host nombre_de_la_imagen
    ```

4. Accede a la aplicación en tu navegador web en `http://localhost:8501`.




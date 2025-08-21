# PeopleAppBackend

## Requisitos

- Python 3.10 o superior
- pip
- PostgreSQL

## Instalación

1. Clonar el repositorio:

    ```sh
    git clone https://github.com/kjduy/PeopleAppBackend.git
    cd PeopleAppBackend
    ```

2. Crear y activar un entorno virtual:

    ```sh
    python3 -m venv venv
    source venv/bin/activate (Linux o Mac)
    venv\Scripts\activate (Windows)
    ```

3. Instalar las dependencias:

    ```sh
    pip install -r requirements.txt
    ```

4. Copiar el archivo de entorno y configurar las variables:

    ```sh
    Crear archivo .env en base al archivo .env.example
    ```

## Uso

1. Ejecutar la aplicación:

    ```sh
    uvicorn app.main:app --reload
    ```

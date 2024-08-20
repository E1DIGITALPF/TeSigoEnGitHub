# Seguimiento masivo en Github

Este script permite seguir a una lista de usuarios en GitHub usando la API de GitHub. Está diseñado para facilitar el seguimiento masivo de usuarios mediante un archivo de configuración y un archivo de usuarios en formato JSON.

## Contenido

- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Estructura de Archivos](#estructura-de-archivos)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Instalación

1. Clona el repositorio:

   ```bash
   git clone 
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd tu_repositorio
   ```

3. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv
   ```

4. Activa el entorno virtual:

   En Windows:
   ```bash
   venv\Scripts\activate
   ```

   En macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

5. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

## Configuración

1. Crea un archivo `.env` en el directorio raíz del proyecto.

2. Agrega tus [credenciales de GitHub](https://github.com/settings/tokens) en el archivo `.env` con el siguiente formato:

   ```env
   GITHUB_USERNAME=tu_usuario
   GITHUB_TOKEN=tu_token
   ```

   Asegúrate de reemplazar `tu_usuario` y `tu_token` con tu nombre de usuario de GitHub y tu token de acceso personal.

## Uso

1. Prepara el archivo de usuarios en formato JSON.

2. Crea un archivo llamado `usuarios.json` en la carpeta `static/` con el siguiente formato:

   ```json
   {
     "usuarios": [
       "usuario1",
       "usuario2",
       "usuario3"
     ]
   }
   ```

   Reemplaza "usuario1", "usuario2", "usuario3" con los nombres de usuario de GitHub que deseas seguir.

3. Ejecuta el script:

   ```bash
   python main.py
   ```

   El script seguirá a los usuarios listados en `static/usuarios.json` uno por uno, con una pausa de 1 segundo entre cada solicitud para evitar exceder los límites de la API de GitHub.

## Estructura de Archivos

- `main.py`: Script principal que sigue a los usuarios.
- `static/usuarios.json`: Archivo JSON que contiene la lista de usuarios a seguir.
- `.env`: Archivo de configuración para las credenciales de GitHub.
- `requirements.txt`: Lista de dependencias del proyecto.
- `README.md`: Este archivo.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.

2. Crea una rama para tus cambios:

   ```bash
   git checkout -b mi-nueva-funcionalidad
   ```

3. Realiza tus cambios y haz commit:

   ```bash
   git commit -am 'Añade nueva funcionalidad'
   ```

4. Empuja los cambios a tu repositorio:

   ```bash
   git push origin mi-nueva-funcionalidad
   ```

5. Crea un Pull Request en el repositorio original.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.
# Seguimiento masivo en Github

Estos scripts permiten seguir a una lista de usuarios en GitHub usando la API de GitHub. Están diseñados para facilitar el seguimiento masivo de usuarios mediante un archivo de configuración y un archivo de usuarios en formato JSON.

A su vez se agrega un script filtro que ayuda a extrar los usuarios correctamente formateados de un archivo convencional de texto convirtiéndolos en una lista diccionario en formato .json.

Allá en el pasado quedaron esas largas horas siguiendo a tus desarrolladores, empresas, industrias y personas favoritas en GitHub. Utilizando correctamente estos scripts formar tu red rápidamente es un hecho. Sigue a todo lo que te interesa en GitHub en cuestión de minutos y sin riesgos.

## Contenido

- [Instalación](#instalación)
- [Configuración](#configuración)
- [Estructura de Archivos](#estructura-de-archivos)
- [Optimización del flujo](#optimización-del-flujo)
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

## Preparando las listas de usuarios

   Es posible [conseguir listas públicas](https://github.com/best-of-lists/best-of) de usuarios de GitHub tomando en cuenta aficiones, localización, industrias(...) Esto te servirá como punto de partida para escrapear los enlaces a los perfiles. Una vez tengas enlaces a tu disposición crea un archivo de texto llamado `piloto.txt` dentro de la carpeta `/static` y pega todo el contenido de las listas que encontraste ahi dentro del archivo de texto.
   
   En la raiz del proyecto hay un script llamado `extraeUsuarios.py` que hará el trabajo de extraer hacia el archivo nuevo `static/usuarios.json` todos los usuarios de Github del archivo de texto `piloto.txt` que acabamos de crear y llenar con los datos de las listas. Es importante que sepas que el script `extraeUsuarios.py` limpia y refina completamente el archivo `piloto.txt` convirtiéndolo en el archivo `usuarios.json` con todos los datos necesarios.

   Una vez prepares tu `usuarios.json` con todos los usuarios a seguir procede a la siguiente fase.


## Configuración

1. Crea un archivo `.env` en el directorio raíz del proyecto.

2. Agrega tus [credenciales de GitHub](https://github.com/settings/tokens) en el archivo `.env` con el siguiente formato:

   ```env
   GITHUB_USERNAME=tu_usuario
   GITHUB_TOKEN=tu_token
   ```

   Asegúrate de reemplazar `tu_usuario` y `tu_token` con tu nombre de usuario de GitHub y tu token de acceso personal ()

3. Ejecuta el script:

   ```bash
   python seguir_github.py
   ```

   El script seguirá a los usuarios listados en `static/usuarios.json` uno por uno, con una pausa de 1 segundo entre cada solicitud para evitar exceder los límites de la API de GitHub.

## Estructura de Archivos

- `seguir_github.py`: Script principal que sigue a los usuarios.
- `static/usuarios.json`: Archivo JSON que contiene la lista de usuarios a seguir.
- `extraeUsuarios.py`: Script para procesar nombres de usuarios desde un archivo de texto.
- `.env`: Archivo de configuración para las credenciales de GitHub.
- `requirements.txt`: Lista de dependencias del proyecto.
- `README.md`: Este archivo.

## Optimización del flujo
Este script está diseñado para manejar de forma inteligente los límites de tasa de la API de GitHub:

- Pausas aleatorias: Se introducen pausas aleatorias entre solicitudes para reducir la posibilidad de ser bloqueado por la API.
- Reintentos automáticos: Los usuarios que no pueden ser seguidos debido a errores como el código 429 son reintentados automáticamente.
- Lotes de usuarios: El script sigue a los usuarios en lotes, con pausas extendidas entre cada lote para evitar exceder los límites de tasa.
- Gestión de errores: Los usuarios fallidos se guardan en un archivo separado para reintentar más tarde.

### A tomar en cuenta:

No se recomienda modificar la velocidad de seguimiento y los timeouts en el script para evitar bans (rate limit es lo más "barato" que podría pasar). Es mejor evitar antes que lamentar. Ya de por sí lanza error 429 cuando las listas son de miles, pero hace una pausa razonable cuando toca por primera vez ese límite para evitar disgustos posteriores.

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

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles. Se considera importante mencionar también que este script no representa spam ni ningún otro tipo de software malicioso. Seguir a personas en redes sociales no se considera una mala práctica, hacerlo de manera masiva solamente es, sin más, un "enhancement" dentro de los límites impuestos en los Términos de Uso de dicha red.

## A futuro
Puede que lo compile a un ejecutable para Windows o le haga una interfaz universal sencilla. Por ahora anda bien y cumple con el propósito.
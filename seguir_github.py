# Script principal para el seguimiento masivo de usuarios. Si es irresponsivo dale un repaso
# al archivo readme.md. Probablemente tengas que utilizar el script extraeUsuarios.py para
# crear tu diccionario de usuarios o necesites instalar las variables de entorno.
import requests
from requests.auth import HTTPBasicAuth
from time import sleep, time
import json
import os
from dotenv import load_dotenv
from random import randint

load_dotenv()

USERNAME = os.getenv('GITHUB_USERNAME')
TOKEN = os.getenv('GITHUB_TOKEN')

def load_users(filename):
    """Carga la lista de usuarios desde un archivo JSON."""
    with open(filename, 'r') as file:
        data = json.load(file)
    return data.get('usuarios', [])

def is_user_followed(username):
    """Verifica si ya sigues a un usuario en GitHub."""
    url = f'https://api.github.com/user/following/{username}'
    try:
        response = requests.get(url, auth=HTTPBasicAuth(USERNAME, TOKEN))
        if response.status_code == 204:
            return True
        elif response.status_code == 404:
            return False
        else:
            print(f'Error al verificar si sigues a {username}. Código de estado: {response.status_code}')
            return False
    except requests.RequestException as e:
        print(f'Error al verificar a {username}: {e}')
        return False

def follow_user(username, failed_users):
    """Sigue a un usuario en GitHub usando la API y maneja límites de tasa."""
    if is_user_followed(username):
        print(f'Ya sigues a: {username}. Saltando...')
        return

    url = f'https://api.github.com/user/following/{username}'
    try:
        response = requests.put(url, auth=HTTPBasicAuth(USERNAME, TOKEN))
        if response.status_code == 204:
            print(f'Seguido: {username}')
        elif response.status_code == 404:
            print(f'No se encuentra: {username}')
        elif response.status_code == 403:
            rate_limit_reset = int(response.headers.get('X-RateLimit-Reset', 0))
            wait_time = max(0, rate_limit_reset - time())
            print(f'Rate limit excedido. Esperando {wait_time / 60:.2f} minutos.')
            sleep(wait_time)
            failed_users.append(username)
        elif response.status_code == 429:
            rate_limit_reset = int(response.headers.get('X-RateLimit-Reset', 0))
            wait_time = max(0, rate_limit_reset - time())
            print(f'Error 429: demasiadas solicitudes. Esperando {wait_time / 60:.2f} minutos antes de reintentar.')
            sleep(wait_time)
            failed_users.append(username)
        else:
            print(f'Error al seguir a {username}. Código de estado: {response.status_code}')
            failed_users.append(username)
    except requests.RequestException as e:
        print(f'Error siguiendo a {username}: {e}')
        failed_users.append(username)

def save_failed_users(failed_users):
    """Guarda la lista de usuarios que no se pudieron seguir para reintentar más tarde."""
    if failed_users:
        output_dir = 'static'
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, 'failed_users.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({"usuarios": failed_users}, f, indent=2, ensure_ascii=False)
        print(f'Usuarios fallidos guardados en: {output_file}')

def main():
    """Función principal que carga los usuarios, los sigue en lotes y maneja límites de tasa."""
    users_to_follow = load_users('static/usuarios.json')
    failed_users = []
    
    if not users_to_follow:
        print('No se encontraron usuarios para seguir.')
        return
    
    for user in users_to_follow:
        follow_user(user, failed_users)
        sleep(randint(1, 5))
    
    save_failed_users(failed_users)

if __name__ == "__main__":
    main()
import requests
from requests.auth import HTTPBasicAuth
from time import sleep
import json
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('GITHUB_USERNAME')
TOKEN = os.getenv('GITHUB_TOKEN')

def load_users(filename):
    """Carga la lista de usuarios desde un archivo JSON."""
    with open(filename, 'r') as file:
        data = json.load(file)
    return data.get('usuarios', [])

def follow_user(username):
    """Sigue a un usuario en GitHub usando la API."""
    url = f'https://api.github.com/user/following/{username}'
    try:
        response = requests.put(url, auth=HTTPBasicAuth(USERNAME, TOKEN))
        if response.status_code == 204:
            print(f'Seguido: {username}')
        elif response.status_code == 404:
            print(f'No se encuentra: {username}')
        elif response.status_code == 403:
            print(f'Límites excedidos o prohibido para: {username}')
        else:
            try:
                response_json = response.json()
            except ValueError:
                response_json = None
            print(f'Error al seguir a {username}. Código de estado: {response.status_code}, Respuesta: {response_json if response_json else response.text}')
    except requests.RequestException as e:
        print(f'Error siguiendo a {username}: {e}')

def main():
    """Función principal que carga los usuarios y los sigue uno por uno."""
    users_to_follow = load_users('static/usuarios.json')
    
    if not users_to_follow:
        print('No se encontraron usuarios para seguir.')
        return
    
    for user in users_to_follow:
        follow_user(user)
        sleep(1)

if __name__ == "__main__":
    main()

# Mediante este script se pueden scrapear usuarios de Github de cualquier 
# archivo de texto que contenga enlaces URL a los perfiles. Bota un
# archivo .json en la carpeta static llamado usuarios.json que contiene todos
# los usuarios de github encontrados en el archivo, correctamente formateados
# ya listos para ser usados con el script seguir_github.py
import re
import os
import json

# aqui colocas el archivo de texto con todos los enlaces
with open('static/piloto.txt', 'r', encoding='utf-8') as file:
    content = file.read()

usernames = re.findall(r'github\.com/([a-zA-Z0-9_-]+)', content)

unique_usernames = sorted(set(usernames))

json_data = {
    "usuarios": unique_usernames
}

output_dir = 'static'
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'usuarios.json')

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)

print(f'Archivo guardado en: {output_file}')
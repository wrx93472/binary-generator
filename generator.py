import json
import os
from jinja2 import Environment, FileSystemLoader

# 1. Wczytaj dane
with open('schema/interface.json', 'r') as f:
    data = json.load(f)

# 2. Skonfiguruj środowisko Jinja2
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('class_template.jinja2')

# 3. Wygeneruj kod
output_code = template.render(data)

# 4. Zapisz w folderze output
if not os.path.exists('output'):
    os.makedirs('output')

with open('output/generated_model.py', 'w') as f:
    f.write(output_code)

print("Kod wygenerowany pomyślnie w output/generated_model.py")
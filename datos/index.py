import pandas as pd

# Cargar el archivo Excel
df = pd.read_excel('delitos.xlsx')

# Convertir el DataFrame a JSON
df.to_json('delitos.json', orient='records', lines=False)

print("Archivo JSON generado correctamente.")


# Generar un nuevo archivo JSON con la estructura deseada
import json

# Leer el archivo JSON existente
with open('delitos.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extraer los campos relevantes y generar una nueva estructura
result = []

for item in data:
    # Usar unicode_escape para manejar caracteres especiales en tipoDelito
    tipo_delito = item["DELITO"].encode('latin1').decode('unicode_escape')
    
    formatted_item = {
        "tipoDelito": tipo_delito,
        "fecha": item["FECHA DE LOS HECHOS"],
        "hora": item["HORA DE LOS HECHOS"],
        "lat": item["COORD. Y"],
        "lng": item["COORD. X"]
    }
    result.append(formatted_item)

# Guardar el nuevo JSON con la estructura deseada
with open('delitos_procesados.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

print("Archivo JSON generado correctamente.")

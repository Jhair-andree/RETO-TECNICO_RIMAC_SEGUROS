from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Endpoint para obtener información sobre personajes de Star Wars
@app.route('/starwars/characters/<int:character_id>', methods=['GET'])
def get_starwars_character(character_id):
    # URL de la API de Star Wars
    api_url = f'https://swapi.dev/api/people/{character_id}/'

    # Realizar una solicitud GET a la API de Star Wars
    response = requests.get(api_url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Convertir la respuesta a formato JSON
        character_data = response.json()
        
        # Devolver la información del personaje en formato JSON
        return jsonify(character_data)
    else:
        # Si la solicitud no fue exitosa, devolver un mensaje de error
        return jsonify({'error': 'No se pudo obtener la información del personaje'}), 500

if __name__ == '__main__':
    # Ejecutar la aplicación en el puerto 5000
    app.run(debug=True)

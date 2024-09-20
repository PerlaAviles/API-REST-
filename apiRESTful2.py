from flask import Flask, request, jsonify  # Importamos Flask y las herramientas necesarias
import requests  # Importamos la librería requests para hacer solicitudes HTTP

app = Flask(__name__)  # Inicializamos la aplicación Flask

# URL de la base de datos en MockAPI
BASE_URL = "https://66eb01ee55ad32cda47b4f5d.mockapi.io/IotCarStatus"  # Esta es la URL de la API MockAPI donde se almacenan los estados de los autos

# Crear un nuevo recurso (POST)
@app.route('/carstatus', methods=['POST'])
def create_car_status():
    new_status = request.json  # Obtenemos los datos enviados en formato JSON por el cliente
    response = requests.post(BASE_URL, json=new_status)  # Hacemos una solicitud POST a MockAPI con los datos recibidos

    if response.status_code == 201:  # Si el código de respuesta es 201 (Creado)...
        return jsonify(response.json()), 201  # Devolvemos los datos que MockAPI haya creado en formato JSON con el código 201
    return jsonify({"error": "No se pudo crear el estado del auto"}), response.status_code  # Si hay un error, lo devolvemos con el código correspondiente

# Leer todos los recursos (GET)
@app.route('/carstatus', methods=['GET'])
def get_all_car_status():
    response = requests.get(BASE_URL)  # Hacemos una solicitud GET a MockAPI para obtener todos los estados de autos

    if response.status_code == 200:  # Si la solicitud es exitosa (código 200)...
        return jsonify(response.json()), 200  # Devolvemos los datos en formato JSON con el código 200
    return jsonify({"error": "No se pudo obtener los estados de los autos"}), response.status_code  # Si hay un error, lo devolvemos

# Leer un recurso por ID (GET)
@app.route('/carstatus/<int:id>', methods=['GET'])
def get_car_status(id):
    response = requests.get(f"{BASE_URL}/{id}")  # Hacemos una solicitud GET a MockAPI para obtener un estado específico de un auto usando su ID

    if response.status_code == 200:  # Si la solicitud es exitosa...
        return jsonify(response.json()), 200  # Devolvemos los datos del auto en formato JSON con el código 200
    return jsonify({"error": f"No se encontró el estado del auto con id {id}"}), response.status_code  # Si no se encuentra el recurso, devolvemos un error

# Actualizar un recurso por ID (PUT)
@app.route('/carstatus/<int:id>', methods=['PUT'])
def update_car_status(id):
    updated_status = request.json  # Obtenemos los datos enviados en formato JSON por el cliente para actualizar el estado del auto
    response = requests.put(f"{BASE_URL}/{id}", json=updated_status)  # Hacemos una solicitud PUT a MockAPI con los datos actualizados

    if response.status_code == 200:  # Si la actualización es exitosa...
        return jsonify(response.json()), 200  # Devolvemos los datos actualizados con el código 200
    return jsonify({"error": f"No se pudo actualizar el estado del auto con id {id}"}), response.status_code  # Si hay un error, lo devolvemos

# Eliminar un recurso por ID (DELETE)
@app.route('/carstatus/<int:id>', methods=['DELETE'])
def delete_car_status(id):
    response = requests.delete(f"{BASE_URL}/{id}")  # Hacemos una solicitud DELETE a MockAPI para eliminar un estado específico del auto usando su ID

    if response.status_code == 200:  # Si la eliminación es exitosa...
        return jsonify({"message": f"El estado del auto con id {id} ha sido eliminado"}), 200  # Devolvemos un mensaje confirmando la eliminación con el código 200
    return jsonify({"error": f"No se pudo eliminar el estado del auto con id {id}"}), response.status_code  # Si hay un error, lo devolvemos

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)  # Ejecutamos la aplicación en modo debug para facilitar el desarrollo y depuración
# holaaa
from flask import Flask

app = Flask(__name__)

# Método GET: Responde con un saludo simple
@app.route('/saludo', methods=['GET'])
def saludo_get():
    return "¡Hola, bienvenido a tu API!", 200  # Código 200: OK

# Método POST: Responde sin necesidad de datos en el body
@app.route('/saludo', methods=['POST'])
def saludo_post():
    return "¡Hola, tu solicitud POST ha sido recibida!", 201  # Código 201: Creado

# Método PUT: Actualiza un saludo sin necesidad de datos en el body
@app.route('/saludo', methods=['PUT'])
def saludo_put():
    return "El saludo ha sido actualizado exitosamente", 200  # Código 200: OK

# Método DELETE: Elimina un saludo sin necesidad de datos en el body
@app.route('/saludo', methods=['DELETE'])
def saludo_delete():
    return "El saludo ha sido eliminado", 200  # Código 200: OK

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)

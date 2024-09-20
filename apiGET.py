from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta principal, método GET
@app.route('/saludo', methods=['GET'])
def saludo():
    return "¡Hola, bienvenido a tu API!"

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)
    # hola

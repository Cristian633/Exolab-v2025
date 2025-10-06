from flask import Flask, send_from_directory
import os

# Crear la aplicación Flask y definir la carpeta estática
app = Flask(__name__, static_folder='public')

# Ruta principal que sirve index.html
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Ruta genérica para servir cualquier archivo dentro de 'public'
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

# Ejecutar la aplicación en el puerto definido por Azure
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)


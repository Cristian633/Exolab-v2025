from flask import Flask, send_file, send_from_directory

# Sirve estáticos desde /public
app = Flask(__name__, static_folder="public", static_url_path="")

# Raíz -> muestra public/index.html
@app.route("/")
def index():
    return send_file("public/index.html")

# Cualquier otro archivo dentro de /public (html, jpg, css, js, etc.)
@app.route("/<path:path>")
def serve_public(path):
    return send_from_directory("public", path)

# Para pruebas locales (opcional)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

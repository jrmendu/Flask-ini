from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
@app.route("/hello")
# ruta dinamica amb parametre name
@app.route("/hello/<name>")
def hello(name = "pepitu"):
    return f"Hola {name}"

@app.route("/user")
@app.route("/user/<string:user>")   # per si necessito rebre un string. Amb int es veu més clar l'exemple
def user(user = ""):
    return f"Hola usuario {user}"

@app.route("/products")
@app.route("/products/<string:_category>")
@app.route("/products/<string:_category>/<int:_id>")
def products(_category = "Per defecte", _id = 1):
    return render_template("routes.html", category=_category, id=_id)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5003, debug = True)
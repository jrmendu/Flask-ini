from flask import Flask, render_template, request, session, abort
app = Flask(__name__)

@app.route("/")
@app.route("/hello")
# ruta dinamica amb parametre name
@app.route("/hello/<name>")
def hello(name = "pepitu"):
    return f"Hola {name}"
    
@app.route("/user")
@app.route("/user/<string:user>")   # per si necessito rebre un string
def user(user = "pepitu"):
    return f"Hola usuario {user}"

# 5003
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5003, debug = True)
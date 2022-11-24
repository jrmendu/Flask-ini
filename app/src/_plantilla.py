from flask import Flask, render_template, request
app = Flask(__name__)

# 127.0.0.1:5003
# 80.240.127.173:5003
@app.route("/")
def hello():
    return "<h1>Bienvenid@ a la plantilla</h1>"

# 5003
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5003, debug = True)
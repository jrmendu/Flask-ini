from flask import Flask, render_template, request
app = Flask(__name__)

# 127.0.0.1:5003
# 80.240.127.173:5003
@app.route("/")
def hello():
    return "<h1>Bienvenido a mi app</h1>"

@app.route("/form", methods=["GET", "POST"])
def form():
    name = None
    age = 0
    if request.method == "POST":
        name = request.form['name']
        age = request.form['age']
        print(name, age)
    return render_template("form.html", name=name, age=age)

# 5003
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5003, debug = True)
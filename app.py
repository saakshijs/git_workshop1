from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    age = ""

    if request.method == "POST":
        year = int(request.form["year"])
        age = 2026 - year

    return render_template("index.html", age=age)

app.run(debug=True)

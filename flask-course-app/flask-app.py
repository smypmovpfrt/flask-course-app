from flask import Flask, render_template
from arguments import site_name, output_menu

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title = site_name)

@app.route("/about")
def about():
    return "<h1>SASI!!!</h1>"

if __name__ == "__main__":
    app.run(debug=True)

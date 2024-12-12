from flask import Flask, render_template, url_for
from arguments import site_name, output_menu, site_menu

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title = site_name, site_menu=site_menu)

@app.route("/index")
def kek():
    return render_template("index.html", title = site_name, site_menu=site_menu)

@app.route("/links")
def about():
    return render_template("links.html", title = "Сокращатель ссылок", site_menu=site_menu)

if __name__ == "__main__":
    app.run(debug=True)


#with app.test_request_context():
# print(url_for("index"))
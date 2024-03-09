from flask import Flask, render_template

from core import dao

name = "Sale app"
app = Flask(name)


@app.route("/")
def index():
    categories = dao.get_Categories()
    return render_template('index.html',categories=categories)


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)

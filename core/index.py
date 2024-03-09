from flask import Flask, render_template

name = "Sale app"
app = Flask(name)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)

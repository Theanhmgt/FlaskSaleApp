from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

name = "Sale app"
app = Flask(name)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:%s@localhost/saledb' % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

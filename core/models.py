from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

from __init__ import db, app


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

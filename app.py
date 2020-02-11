from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgres://postgres:r9=`Z_2q4(E^fFU@127.0.0.1:5432/flask_rest'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)


# Product Model
class Prodcut(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, *args):
        name, description, price, qty = args
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


# Product Schema
class ProdcutSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')


# Init schema
product_chema = ProdcutSchema()
products_chema = ProdcutSchema(many=True)

# Create a Product
@app.route('/product', methods=['POST'])
def add_product():
    pass


if __name__ == "__main__":
    app.run(debug=True)

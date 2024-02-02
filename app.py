from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# connect to the database 

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://ecommerce_dev:123456@localhost:5432/oct_ecommerce"

db = SQLAlchemy(app)

#Model - table in our database
class Product(db.Model):
    #tablename
    __tablename__ = "products"
    #define the primary key
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100))
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)

#CLI command
@app.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created")
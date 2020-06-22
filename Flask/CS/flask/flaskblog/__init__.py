from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initializing a flask app
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b4e1625f044394f9b68507161f4f5e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# # Initialized SQLAlchemy db
db = SQLAlchemy(app)

# To avoid circular import
from flaskblog import routes

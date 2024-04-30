from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'
app.debug = True

db = SQLAlchemy(app)
toolbar = DebugToolbarExtension(app)

# Import routes after initializing app and db
from . import routes

if __name__ == '__main__':
    app.run(debug=True)

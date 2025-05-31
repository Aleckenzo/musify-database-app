# musica.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

cscf = CSRFProtect(app)

from views_musica import *
from views_usuario import *

if __name__ == '__main__':
    app.run(debug=True)

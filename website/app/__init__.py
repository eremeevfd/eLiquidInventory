from flask import Flask
from flask.ext.login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('website.config')
db = SQLAlchemy(app)

# lm = LoginManager()
# lm.init_app(app)
# lm.login_view = 'login'

from website.app import views, models

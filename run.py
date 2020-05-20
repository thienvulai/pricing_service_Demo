from flask import Flask, render_template
from common.database import Database
import os

app = Flask(__name__)
app.secret_key = os.urandom(64)
app.config.from_object('config.py')


@app.before_first_request
def init_db():
    Database.intialize()


@app.route('/')
def home():
    return render_template('home.html')


from flask import Flask, render_template
from views.stores import store_blueprint
from views.alerts import alert_blueprint
from views.users import user_blueprint

app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(store_blueprint, url_prefix="/stores")
app.register_blueprint(user_blueprint, url_prefix="/users")

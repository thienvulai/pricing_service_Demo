# from models.item import Item
#
# url = "https://www.johnlewis.com/2020-apple-ipad-pro-12-9-inch-a12z-bionic-ios-wi-fi-cellular-512gb/space-grey/p4949083"
# tag_name = "p"
# query = {"class": "price price--large"}
#
# ipad = Item(url, tag_name, query)
# ipad.save_to_mongo()
#
# items_loaded = Item.all()
# print(items_loaded)
# print(items_loaded[0].load_price())

# from models.alert import Alert
#
# alert = Alert("43013b8ca0bf4a879c4a15081314dd41", 2000)
# alert.save_to_mongo()
import os
from flask import Flask, render_template
from views.stores import store_blueprint
from views.alerts import alert_blueprint
from views.users import user_blueprint

app = Flask(__name__)
app.secret_key = os.urandom(64)
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)


@app.route('/')
def home():
    return render_template('home.html')


app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(store_blueprint, url_prefix="/stores")
app.register_blueprint(user_blueprint, url_prefix="/users")

if __name__ == '__main__':
    app.run(debug=True)

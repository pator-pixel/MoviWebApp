from flask import Flask
from data_manager import DataManager
from models import db, Movie

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moviweb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

data_manager = DataManager()


@app.route('/')
def home():
    return "Welcome to MoviWeb App!"


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
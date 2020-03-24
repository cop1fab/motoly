from flask import Flask
from database.db import initialize_db


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/motors'
}
initialize_db(app)


@app.route("/", methods=['GET'])
def home():
    return "Welcome to motoly, your #1 app to manage electric vehicle business in Rwanda"


if __name__ == '__main__':
    app.run(port=5000, debug=True)
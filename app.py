from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST', 'PUT'])
def home():
    return "Yaaay! Here we are, now let's start building!!"


if __name__ == '__main__':
    app.run(port=5000, debug=True)
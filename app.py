from flask import Flask, render_template
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'flask_app',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

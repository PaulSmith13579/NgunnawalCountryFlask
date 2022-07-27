from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)

app.config.from_object(Config)  # loads the configuration for the database
db = SQLAlchemy(app)            # creates the db object using the configuration

@app.route('/')
def Homepage():  # put application's code here
    return render_template("index.html", title="Ngunnawal Country")

if __name__ == '__main__':
    app.run()

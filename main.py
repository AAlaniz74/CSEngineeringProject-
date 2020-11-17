import sqlalchemy
from flask import Flask           # import flask
from flask_sqlalchemy import SQLAlchemy

#Following code is used from a tutorial online

app = Flask(__name__)             # create an app instance


@app.route("/")                   # at the end point /
def hello():                      # call method hello
    print(sqlalchemy.__version__)
    return "Hello World!"         # which returns "hello world"


if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app

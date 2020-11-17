import sqlalchemy
from flask import Flask           # import flask
from flask_sqlalchemy import SQLAlchemy
import tempfile
import os.path
import database

#Following code is used from a tutorial online

app = Flask(__name__)             # create app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    tempfile.gettempdir(), 'test.db')  #creates the file where the database is stored locally
db = SQLAlchemy(app)


@app.route("/")                   # at the end point /
def hello():                      # call method hello
     print(sqlalchemy.__version__)

    temp = database.User()  #
    list = temp.displayAllUsers()
    
    user = temp.getIDInfo(1)
    return user.username         # which returns "hello world"


if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app

import sqlalchemy
from flask import Flask           # import flask
from flask_sqlalchemy import SQLAlchemy
import tempfile
import os.path


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    tempfile.gettempdir(), 'test.db')
db = SQLAlchemy(app)

 

class User(db.Model):
    identifier = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = False, nullable = False)
    password = db.Column(db.String(50), unique = False,  nullable = False)
    admintype = db.Column(db.String(20), unique = False, nullable = False)
    idVal = 1 
    def __repr__(self):
        return '<User %r>' % self.username


    def createUser(self,user,passwrd,admin):
        #from database import User
        test = User(identifier = self.idVal,username = user,password = passwrd, admintype = admin)

        self.idVal = self.idVal + 1
        db.session.add(test)
        db.session.commit()
    def getIDInfo(self, id): #Gets user based on ID
        temp = User.query.filter_by(identifier = id).first()
        return temp

    def getUserInfo(self,user): #Gets yser based on username
        temp = User.query.filter_by(username = user).first()
        return temp
    
    def removeAllTable(self): #This is bug fix thing, basically a clean reset
        db.drop_all(bind = None)
    
    def deleteUser(self, user):
        temp = getUserInfo(user)
        db.session.delete(temp)
        db.session.commit()

    def displayAllUsers(self):

        return User.query.all()


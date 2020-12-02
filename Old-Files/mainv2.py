# import sqlalchemy
from flask import Flask, redirect, url_for, render_template, request, session

# from flask_sqlalchemy import SQLAlchemy

# Following code is used from a tutorial online
app = Flask(__name__)  # create an app instance
app.secret_key = "hello"

@app.route("/")  # at the end point /
def home():  # call method hello
    return render_template("index.html")  # which returns "hello world

"""
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user"))
    else:
        return render_template("login.html")
"""

@app.route('/login', methods=["POST", "GET"])
def login():
    error = None
    if request.method == "POST":
        if ((request.form["username"] == "admin" and request.form["password"] == "admin") or
                (request.form["username"] == "adminFinance" and request.form["password"] == "adminFinance") or
                    (request.form["username"] == "adminSales" and request.form["password"] == "adminSales") or
                        (request.form["username"] == "adminHR" and request.form["password"] == "adminHR") or
                            (request.form["username"] == "adminTech" and request.form["password"] == "adminTech")):
            user = request.form["username"]
            return redirect(url_for("user", usr=user))
        else:
            error = "Invalid Credentials. Please try again."
    return render_template("login.html", error=error)


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

"""
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!"))
"""

if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)  # run the flask app

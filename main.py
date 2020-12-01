from flask import Flask, redirect, url_for, render_template, request, session


app = Flask(__name__)  # create an app instance
app.secret_key = "er3412we5234"

@app.route("/", methods=["POST", "GET"])
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


@app.route("/<usr>", methods=["GET", "POST"])
def user(usr):
    if request.method == "POST":
        usr = "null"
    if usr=="admin":
        return render_template("admin.html")
    elif usr=="adminFinance":
       return render_template("finance.html")
    elif usr=="adminSales":
       return render_template("sales.html")
    elif usr=="adminHR":
       return render_template("HR.html")
    elif usr=="adminTech":
       return render_template("tech.html")
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":  # on running python app.py
    app.run(debug=True, port=5001)  # run the flask app
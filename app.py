from flask import Flask, render_template, request, redirect, session
from flask.cli import with_appcontext
import os, click, json
from src import conversions
from src.object import Object
from src.db import Database
from dotenv import load_dotenv

proj_folder = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder= proj_folder + "/templates")
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")

@click.command("init-db")
@with_appcontext
def init_db_command():
        db.init_db()

with app.app_context():
    db = Database("app.db", proj_folder)
    app.teardown_appcontext(db.close_db)
    app.cli.add_command(init_db_command)

@app.route("/login", methods=["GET", "POST"])
def login():
    if "username" in session:
        return redirect(f"calculator/{session['username']}")
    if request.method == "POST":
        username = request.form.get("username")
        print(db.login_valid(username, request.form.get("password")))
        if db.login_valid(username, request.form.get("password")):
            session["username"] = username
            return redirect(f"/calculator/{username}")
        else:
            return render_template("login.html", page_title="Login", error="That login is invalid", logged_in=False)
    return render_template("login.html", page_title="Login", logged_in=False)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if "username" in session:
        return redirect(f"calculator/{session['username']}")
    if request.method == "POST":
        username = request.form.get("username")
        if db.value_unique("users", "username", username) and username != "guest":
            db.add_data("users", request.form.to_dict())
            session["username"] = username
            return redirect(f"/calculator/{username}")
        else:
            return render_template("signup.html", page_title="Create an Account", error="That username is taken", logged_in=False)
    return render_template("signup.html", page_title="Create an Account", logged_in=False)

@app.route("/calculator/<username>", methods=["GET", "POST"])
def calculator(username):
    if username != "guest" and username != session["username"]:
        return redirect("/")
    if request.method == "POST":
        values = {}
        for value in request.form:
            values[value] = request.form.get(value)
        standard_values = conversions.convert_to_standards(values)
        obj = Object(standard_values)
        obj.simulate()
        restored_data = conversions.round_dict(conversions.convert_from_standards(values, obj.data), 1)
        return render_template("calculator.html", 
        page_title="Physics Calculator", 
        logged_in="username" in session, 
        data=restored_data,
        settings=json.dumps(values)
        )
    
    return render_template("calculator.html", 
    page_title="Physics Calculator", 
    logged_in="username" in session,
    settings=json.dumps({
        "mass":"1",
        "mass-units":"kg",
        "x":"0",
        "x-units":"m",
        "y":"0",
        "y-units":"m",
        "vel":"0",
        "vel-units":"m/s",
        "ang":"0",
        "ang-units":"rd",
        "time":"1",
        "time-units":"s"
    })
    )

@app.route("/calculator/<username>", methods=["GET", "POST"])
def history(username):
    return render_template("history.html")

@app.route("/")
def index():
    if "username" in session:
        return redirect(f"calculator/{session['username']}")
    return redirect("/calculator/guest")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("calculator/guest")


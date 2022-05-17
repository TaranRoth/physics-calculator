from flask import Flask, render_template, request
import os
from src import conversions
from src.object import Object

proj_folder = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder= proj_folder + "/templates")

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        values = {}
        for value in request.form:
            values[value] = request.form.get(value)
        standard_values = conversions.convert_to_standards(values)
        obj = Object(standard_values)
        obj.simulate()
        print(obj.data)
    return render_template("calculator.html", page_title="Physics Calculator", to_sec=conversions.to_sec)
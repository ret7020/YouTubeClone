from flask import Blueprint, render_template, abort, request

base_bl = Blueprint('main', __name__)

@base_bl.route("/")
def home_page():
    return render_template("index.html")

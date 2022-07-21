from flask import Blueprint, render_template, abort, request

base_bl = Blueprint('api', __name__)

@base_bl.route("/api/get_videos_home")
def home_page():
    return render_template("index.html")

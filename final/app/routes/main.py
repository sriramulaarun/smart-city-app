from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route("/")
def home():
    return render_template("home.html")

@bp.route("/report")
def report():
    return render_template("report.html")

@bp.route("/track")
def track():
    return render_template("track.html")

@bp.route("/analytics")
def analytics():
    return render_template("analytics.html")

@bp.route("/profile")
def profile():
    return render_template("profile.html")

@bp.route("/auth")
def auth():
    return render_template("auth.html")

@bp.route("/map")
def city_map():
    return render_template("map.html")

@bp.route("/feed")
def feed():
    return render_template("feed.html")

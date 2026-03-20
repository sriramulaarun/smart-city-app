from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('admin', __name__)

@bp.route("/admin")
def admin():
    return render_template("admin_login.html")

@bp.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")

@bp.route("/admin-login", methods=["POST"])
def admin_login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data"}), 400

    if data.get("username") == "admin" and data.get("password") == "admin123":
        return jsonify({"message": "Admin login success"})

    return jsonify({"error": "Invalid credentials"}), 401
